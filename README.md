## 概要
Cloud Pub/SubにpublishされたJSON形式のデータがBigQueryへストリーミングインサートされていきます。

## 利用するGCPのコンポーネント
- [Cloud Pub/Sub](https://cloud.google.com/pubsub/?hl=ja)
- [BigQuery](https://cloud.google.com/bigquery/?hl=ja)
- [Google App Engine](https://cloud.google.com/appengine/?hl=ja)

## セットアップ
- 開発環境の構築
- Cloud Pub/Subにトピックを作成
- BigQueryにDatasetとTableを作成
- GAEでpushサブスクリプション用のエンドポイントを作成
- Cloud Pub/Subにpushサブスクリプションの作成

### 開発環境の構築
- Python27の環境
  - pyenvやvirtualvenvなどお好みに合わせて
- [Goolge-Cloloud-SDK](https://cloud.google.com/sdk/?hl=ja)のインストール
  - [認証などのセットアップ](https://cloud.google.com/sdk/docs/initializing?hl=ja)を行う
- リポジトリのクローン
```
$ git clone git@github.com:rindai87/streaming-insert-sample.git
```
- Virtualenvによる環境の構築
```
$ pip install virtualenv
$ cd streaming-insert-sample
$ virtualenv env
$ source env/bin/activate
$ pip install -t lib -r requirements.txt
```

### Cloud Pub/Subにトピックを作成
```
# [PUBSUB_TOPIC_NAME] must be same as in app.yaml
$ gcloud beta pubsub topics create [PUBSUB_TOPIC_NAME]
```

### BigQueryにDatasetとTableを作成
- WebUIなどから適当にセットアップ
- 今回はデータ生成元をローカルPCのロードアベレージをロードアベレージを決め打ちとしているで以下のフォーマットに対応させているが変更可能
```bash
{"datetime":"2017-07-10 10:30:00", "load1": 1.0, "load15": 3.5}
# datetime: DATETIME
# load1: FLOAT
# load2: FLOAT
```

### GAEでpushサブスクリプション用のエンドポイントを作成
```
# Replace env_vars to your own env name in app.yaml
$ cd ()
$ source env/bin/activate
$ dev_appserver.py app.yaml
$ gcloud app deploy app.yaml
```

## セットアップの確認
- Cloud Pub/Subに対してJSONをpublishする
  - ローカルPCのロードアベレージをpublishするスクリプトとして`script/generate_json.py`を用意している
- BigQueryにクエリ発行
  - ストリーミングインサートの場合、WebUIのPreviewに反映されるには一定の時間がかかるためクエリを発行して結果を確認する
