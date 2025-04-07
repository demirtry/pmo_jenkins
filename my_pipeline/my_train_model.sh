#!/bin/bash

echo "Start train model"
cd /var/lib/jenkins/workspace/my_download/
. ./my_env/bin/activate
cd ./my_pipeline
python3 my_train_model.py > my_model.txt