#№2. train_model
echo "Start train model"
cd /var/lib/jenkins/workspace/download/
. ./my_env/bin/activate   #активировать виртуальное окружение
cd ./MLOPS/lab3		   #перейти в директорию ./MLOPS/pwd
python3 train_model.py > best_model.txt #обучение модели запись лога в файл best_model
#------------------------