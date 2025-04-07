#№1. download
python3 -m venv ./my_env #создать виртуальное окружение в папку
. ./my_env/bin/activate   #активировать виртуальное окружение
python3 -m ensurepip --upgrade
pip3 install setuptools
pip3 install -r requirements.txt
cd ./my_pipeline    #перейти в директорию
python3 my_download.py    #запустить python script