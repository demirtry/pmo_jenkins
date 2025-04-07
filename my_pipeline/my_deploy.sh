#!/bin/bash

echo "Start deploy model"
cd /var/lib/jenkins/workspace/my_download/
. ./my_env/bin/activate
cd ./my_pipeline
export BUILD_ID=dontKillMe
export JENKINS_NODE_COOKIE=dontKillMe
path_model=$(cat my_model.txt)
mlflow models serve -m $path_model -p 5003 --no-conda &
