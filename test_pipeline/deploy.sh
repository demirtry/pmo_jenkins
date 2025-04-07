#3. deploy
cd /var/lib/jenkins/workspace/download/
. ./my_env/bin/activate   #активировать виртуальное окружение
cd ./MLOPS/lab3		   #перейти в директорию ./MLOPS/lab3
export BUILD_ID=dontKillMe            #параметры для jenkins чтобы не убивать фоновый процесс для mlflow сервиса
export JENKINS_NODE_COOKIE=dontKillMe #параметры для jenkins чтобы не убивать фоновый процесс для mlflow сервиса
path_model=$(cat best_model.txt) #прочитать путь из файла в bash переменную
mlflow models serve -m $path_model -p 5003 --no-conda & #запуск mlflow сервиса на порту 5003 в фоновом режиме
#------------------------