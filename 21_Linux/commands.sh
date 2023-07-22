# install Python 3
apt install build-essential libbz2-dev libdb-dev libreadline-dev libffi-dev libg
dbm-dev liblzma-dev libncursesw5-dev libsqlite3-dev libssl-dev zlib1g-dev uuid-d
ev tk-dev
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz
tar xJf Python-3.9.2.tar.xz
cd Python-3.9.2
./configure
make
make install

# prepare venv
# c.f.) https://hirooka.pro/python-venv-ubuntu-20-04/
apt install -y python3-venv

# install jupyter notebook
# c.f.) https://qiita.com/zono_0/items/49eb8605ef4d841b2c26
apt install jupyter-notebook

# python path
alias python=python3

#Python venv activate
source ./kaminogovenv/bin/activate
######----------------VI----------------######
# 行削除
shift v → d

######----------------Jupyter Commands----------------######
# No1 jupyter の設定ファイル作成
jupyter notebook --generate-config
# No2 jupyter の設定ファイルを更新
> vi .jupyter/jupyter_notebook_config.py
c.NotebookApp.ip = 'localhost' ⇒c.NotebookApp.ip = '*'
# No3 jupyter 実行
# 通常実行時：
jupyter notebook
# 　ルート実行時：
jupyter notebook --allow-root
# No4 URLをブラウザに打ち込む
http://10.102.189.30:31202/(token)

# No5 Tokenを外して実行する方法
jupyter notebook  --allow-root --NotebookApp.token=''

# JupyterLab
jupyter-lab --ip='0.0.0.0' --allow-root

######----------------Kedro commands----------------######
    pip install kedro==0.16.5
    pip install kedro[pandas]==0.16.5 # Pandas is installed separately due a bug with pip.
    pip install kedro-viz scipy matplotlib
    kedro new
        project-name
  
    #Add data 
    companies:
    type: pandas.CSVDataSet
    filepath: data/01_raw/dummy_data_add_na_inf.csv

    #Add Nodes



######----------------docker commands----------------######
$ sudo docker cp my.cnf <コンテナID>:/etc/my.cnf




