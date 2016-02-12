#!/bin/bash
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
version=$(grep 'VITREEN_VERSION =' /vitreen/app/__init__.py|cut -d\' -f2)

# Dependencies
## virtualenv deps
virtualenv env
./env/bin/pip install -r /vitreen/requirements.txt
##  Hard system deps (will be coded as debian package deps)
fpm_dependencies=""
for dependency in $dependencies; do
  fpm_dependencies="$(echo $fpm_dependencies) -d $dependency"
done

# Create the package
fpm --verbose --debug \
  -s dir \
  -t deb \
  -a "all" \
  -n "${name}" \
  -v "${version}" \
  --prefix "${prefix}" \
  --provides "${provides}" \
  --description "${description}" \
  --maintainer "${maintainer}" \
  --vendor "${vendor}" \
  --url "${url}" \
  --exclude "*.md" \
  --exclude "requirements.txt" \
  --exclude "LICENSE" \
  --exclude "packaging" \
  --exclude "*.deb" \
  --exclude ".git" \
  --exclude ".gitignore" \
  --exclude "tmp" \
  --license "${license}" \
  ${fpm_dependencies} \
  .
