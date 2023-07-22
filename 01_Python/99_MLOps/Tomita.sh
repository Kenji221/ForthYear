# catboost_test

## Overview
MLopsインフラチームにおける、以下のツール連携確認用です。
* Git
* DVC
* Kedro
* mlflow

## 動作確認手順
### テスト用のディレクトリの作成
```commandline
# <user_name>には適当な文字を入れてください
aim2@aim2:~$ docker exec -it mlops_infra /bin/bash
root@mlops:/# cd /mnt/infra/test_users/
root@mlops:/mnt/infra/test_users# mkdir <user_name>
root@mlops:/mnt/infra/test_users# cd <user_name>
```
### Gitサーバからソースコードの取得
```commandline
root@mlops:/mnt/infra/test_users# git clone /mnt/infra/common/test_server/git_server/catboost_test.git
```
### Python仮想環境の構築・有効化
```commandline
root@mlops:/mnt/infra/test_users/hoge# python3 -m venv myenv
root@mlops:/mnt/infra/test_users/hoge# source myenv/bin/activate
(myenv) root@mlops:/mnt/infra/test_users/hoge# cd catboost_test/
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# pip install -r requirements.txt
```

### DVCサーバからデータの取得
```commandline
# .dvcファイルのみで、データの実体はないことの確認
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# ls data/02_intermediate/
df.parquet.dvc  features.pkl.dvc  importance_df.parquet.dvc

# DVCのサーバからデータの実体の取得
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# dvc pull
A       data/06_models/model_1.pkl
A       data/06_models/model_2.pkl
A       data/02_intermediate/importance_df.parquet
A       data/02_intermediate/df.parquet
A       data/02_intermediate/features.pkl
A       data/07_model_output/importance_1.parquet
A       data/07_model_output/importance_2.parquet
7 files added and 7 files fetched

# 取得したデータの確認
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# ls data/02_intermediate/
df.parquet  df.parquet.dvc  features.pkl  features.pkl.dvc  importance_df.parquet  importance_df.parquet.dvc
```

### kedroの実行
```commandline
# パイプラインの実行
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# kedro run
As an open-source project, we collect usage analytics.
...
  INFO     Pipeline execution completed successfully.
(myenv) root@mlops:/mnt/infra/test_users/hoge/catboost_test# kedro viz
```
### mlflowによる実験結果の確認（実装中...）

***
# サーバ設定のメモ

## Git
```commandline
# 設定
$ git remote add origin /mnt/infra/common/test_server/git_server/hello.git
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
# add->commit->push
$ git add .
$ git commit -m "first commit"
$ git push origin master
```

## DVC
```commandline
# 設定
$ dvc remote add -d myremote /mnt/infra/common/test_server/dvc_server/dvcstore1