#№1. download
python3 -m venv ./my_env #создать виртуальное окружение в папку
. ./my_env/bin/activate   #активировать виртуальное окружение
cd ./MLOPS/lab3		   #перейти в директорию ./MLOPS/lab3
python3 -m ensurepip --upgrade
pip3 install setuptools
pip3 install -r requirements.txt    #установить пакеты python
python3 download.py    #запустить python script