#!/usr/bin/env bash
set -x
set -e

project="$(basename `pwd`)"
artifacts="${1:-tasks/package/artifacts}"
artifacts_vol_in_docker="${artifacts_vol_in_docker:-/artifacts}"
maintainer="${2:-Jaime Gago <contact@jaimegago.com>}"
task_name="${3:-$project-package-$(date +%s)}"
base_image="${4:-sczizzo/trusty-tool}"
dockerfile="${5:-tasks/package/Dockerfile}"

rm -f "${dockerfile}"
cat << DOCKERFILE > "${dockerfile}"
FROM ${base_image}
MAINTAINER ${maintainer}
ENV DEBIAN_FRONTEND=noninteractive
ARG BUILD_NUMBER=${BUILD_NUMBER:-1}

COPY . /build

RUN cd /build && tasks/package/_package.sh "${artifacts_vol_in_docker}" "${maintainer}"

VOLUME ${artifacts_vol_in_docker}
DOCKERFILE

cleanup() {
  docker stop "$task_name"
  docker rm "$task_name"
  docker rmi "$task_name"
  rm "${dockerfile}"
}

trap cleanup EXIT

rm -rf "$artifacts"
docker pull "$base_image"
docker build -t "$task_name" -f "$dockerfile" .
docker run --name "$task_name" -dt "$task_name"
docker cp "${task_name}":"${artifacts_vol_in_docker}"  "${artifacts}"
