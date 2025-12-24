ARG BUILD_FROM=error
FROM $BUILD_FROM

LABEL org.opencontainers.image.source=https://github.com/twasilczyk/mdns-republisher-ha
CMD [ "/sbin/mdns-republisher.sh" ]

RUN apk add avahi avahi-tools dbus

COPY rootfs /
