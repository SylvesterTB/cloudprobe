#!/bin/sh
set -e
aws s3 ls s3://cloudprobe-dashboard

ls -l output/results.json
aws s3 cp output/results.json s3://cloudprobe-dashboard/results.json

python -m cloudprobe.cli --config sample-test.json --no-exit-on-fail






