#!/usr/bin/env bash
set -x
set -e

artifacts="${1:-packaging/artifacts}"
dockerfile="${2:-packaging/Dockerfile}"
task_name="${3:-vitreen-packaging-$(date +%s)}"

cleanup() {
  docker stop "$task_name"
  docker rm "$task_name"
}

trap cleanup EXIT

rm -rf "$artifacts"
docker build -t "$task_name" -f "$dockerfile" .
docker run --name "$task_name" -dt "$task_name"
docker cp "$task_name":/packaging "$artifacts"
