#!/usr/bin/env bash
set -x
set -e

#TODO test CLI arg
reports_vol_in_docker="${reports_vol_in_docker:-/reports}"
tests_dir="${tests_dir:-tests/}"
project="$(basename `pwd`)"
reports="${reports:-tasks/test/reports}"
dockerfile="${2:-tasks/test/Dockerfile}"
task_name="${3:-$project-test-$(date +%s)}"
base_image="${4:-sczizzo/trusty-tool}"
maintainer="${5:-Jaime Gago <contact@jaimegago.com>}"

rm -f "${dockerfile}"
cat << DOCKERFILE > "${dockerfile}"
FROM ${base_image}
MAINTAINER ${maintainer}
ENV DEBIAN_FRONTEND=noninteractive

COPY . /build

RUN cd /build && tasks/test/_tests.sh ${tests_dir} ${reports_vol_in_docker}

VOLUME ${reports_vol_in_docker}
DOCKERFILE

cleanup() {
  docker stop "${task_name}"
  docker rm "${task_name}"
  docker rmi "${task_name}"
  rm "${dockerfile}"
}

trap cleanup EXIT

rm -rf "${artifacts}"
docker pull "${base_image}"
docker build -t "${task_name}" -f "${dockerfile}" .
docker run --name "${task_name}" -dt "${task_name}"
docker cp "${task_name}":"${reports_vol_in_docker}"  "${reports}"
