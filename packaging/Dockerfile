FROM sczizzo/trusty-tool
MAINTAINER Jaime Gago <contact@jaimegago.com>
ENV DEBIAN_FRONTEND=noninteractive

COPY . /vitreen

RUN cd /vitreen \
 && packaging/create_package.sh \
 && mkdir /packaging \
 && mv *.deb /packaging

VOLUME /packaging

CMD ["python", "--version"]
