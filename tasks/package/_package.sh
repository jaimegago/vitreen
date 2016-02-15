#!/usr/bin/env bash
set -x
set -e

ARTIFACTS="${1:-artifacts}"

# Packaging using FPM effing pkg mgmt
description="Vitreen a Graphite Events front end"
dependencies=""
license="MIT license"
maintainer="Jaime Gago"
name="vitreen"
prefix="/opt/vitreen"
provides="${name}"
url="https://github.com/jaimegago/vitreen"
vendor="Vitreen"
version=$(grep 'VITREEN_VERSION =' app/__init__.py|cut -d\' -f2)

# Dependencies
## virtualenv deps
rm -rf env
virtualenv env
./env/bin/pip install -r requirements.txt
##  Hard system deps (will be coded as debian package deps)
fpm_dependencies=""
for dependency in $dependencies; do
  fpm_dependencies="$(echo $fpm_dependencies) -d $dependency"
done

# Create the package
fpm \
  -s dir \
  -t deb \
  -a "all" \
  -n "${name}" \
  -v "${version}" \
  --provides "${provides}" \
  --description "${description}" \
  --maintainer "${maintainer}" \
  --vendor "${vendor}" \
  --url "${url}" \
  --exclude "tasks/package/artifacts" \
  --exclude ".git" \
  --exclude "tmp" \
  --license "${license}" \
  ./tasks/package/vitreen.sh=/usr/local/bin/vitreen \
  "./=$prefix"

dpkg -i *.deb
ls -la /opt/vitreen
echo '{}' > vitreen-config.json
vitreen version

mkdir -p $ARTIFACTS
mv *.deb $ARTIFACTS