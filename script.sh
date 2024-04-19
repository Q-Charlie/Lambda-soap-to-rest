#!/bin/bash

current_dir=$(pwd)

target_folder="package"
zip_name="deployment.zip"

if ! command -v pipreqs &> /dev/null; then
    pip3 install pipreqs
fi

if ! command -v zip &> /dev/null; then
    sudo apt-get install zip
fi

create_zip(){
  pip3 install -r requirements.txt -t $target_folder/
  cd $target_folder && zip -r ../$zip_name .
  cd .. && zip -g $zip_name schemas/*
  zip -g $zip_name lambda_function.py
  echo "Process successful"
}

if [ ! -d "$current_dir/$target_folder" ]; then
  mkdir "$current_dir/$target_folder"
  create_zip

else
  create_zip
fi