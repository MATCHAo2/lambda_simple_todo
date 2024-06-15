from jinja2 import Template, FileSystemLoader, Environment
import boto3
import os

# S3呼び出し
s3 = boto3.client('s3')


def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader('.'))
    
    # レスポンスに含む情報を初期化
    name = 'Guest'
    is_login = False
    
    # S3からテンプレート読み込み
    template_str = s3.get_object(Bucket='ac-book-ma-footprints', Key='index.html')['Body'].read().decode('utf-8')

    # jinja2で扱えるテンプレートに変換する
    template = Template(template_str)
    
    # 環境変数から必要な情報を取得
    # db_host =
    # db_port = 
    # db_username =
    # db_password =
    # db_database = 
    if os.environ['DEV_NAME'] != False:
      name = os.environ['DEV_NAME']
    is_login = os.environ['DEV_IS_LOGIN']

    # レンダリング内容
    data = {
        "name": name,
        "is_login": is_login
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

