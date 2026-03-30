"""Static mDNS component for Home Assistant."""

from __future__ import annotations

from ipaddress import ip_address
import logging
from typing import Any

import voluptuous as vol
from zeroconf import ServiceInfo

from homeassistant.components import zeroconf as zc_comp
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

DOMAIN = "static_mdns"

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.All(
            cv.ensure_list,
            [
                vol.Schema(
                    {
                        vol.Required("hostname"): cv.string,
                        vol.Required("address"): cv.string,
                    }
                )
            ],
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    if DOMAIN not in config:
        return True

    aiozc = await zc_comp.async_get_async_instance(hass)

    for host_def in config[DOMAIN]:
        hostname = host_def["hostname"].strip().removesuffix(".local").rstrip(".")
        address = host_def["address"].strip()

        if not hostname:
            _LOGGER.warning("Skipping empty hostname entry: %s", host_def)
            continue

        try:
            ip_address(address)
        except ValueError:
            _LOGGER.warning(
                "Skipping invalid address %s for host %s", address, hostname
            )
            continue

        service_info = ServiceInfo(
            "_ipp._tcp.local.",
            f"{hostname}._ipp._tcp.local.",
            server=f"{hostname}.local.",
            port=0,
            parsed_addresses=[address],
        )

        try:
            await aiozc.async_register_service(service_info)
            _LOGGER.info("Registered mDNS A record %s -> %s", hostname, address)
        except Exception:
            _LOGGER.exception(
                "Failed to register mDNS entry for %s (%s)", hostname, address
            )

    return True

