from jinja2 import Template, FileSystemLoader, Environment
import boto3
import os

# S3呼び出し
s3 = boto3.client('s3')


def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader('.'))
    
    # テンプレートに含む情報を初期化
    tasks = []
    
    # S3からテンプレート読み込み
    template_str = s3.get_object(Bucket='ac-book-ma-footprints', Key='list.html')['Body'].read().decode('utf-8')

    # jinja2で扱えるテンプレートに変換する
    template = Template(template_str)
    
    # 環境変数から必要な情報を取得
    # db_host =
    # db_port = 
    # db_username =
    # db_password =
    # db_database = 

    # 動作確認用
    tasks = [
        {
            "id": 10,
            "title": "tamago",
            "memo": "50個(5パック)",
            "deadline": "2024/06/30"
        },
        {
            "id": 11,
            "title": "tomato",
            "memo": "20個",
            "deadline": "2024/07/30"
        },
        {
            "id": 21,
            "title": "tamaigou",
            "memo": "50個(5パック)",
            "deadline": "2024/04/30"
        }
    ]

    # レンダリング内容
    data = {
        "tasks": tasks
    }

    # templateにdataを埋め込む
    rendered = template.render(data)

    return {
      'statusCode': 200,
      'headers': {
        'Content-Type': 'text/html'
      },
      'body': rendered
    }


