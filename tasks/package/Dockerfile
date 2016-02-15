FROM sczizzo/trusty-tool
MAINTAINER Jaime Gago <contact@jaimegago.com>
ENV DEBIAN_FRONTEND=noninteractive

COPY . /build

RUN cd /build && tasks/package/_package.sh /artifacts

VOLUME /artifacts