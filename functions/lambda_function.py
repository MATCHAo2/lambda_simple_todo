from jinja2 import FileSystemLoader, Environment
import boto3

# S3呼び出し
s3 = boto3.client('s3')


def lambda_handler(event, context):
    env = Environment(loader=FileSystemLoader('.'))
    # S3からテンプレート読み込み
    template_str = s3.get_object(Bucket='ac-book-ma-footprints', Key='index.html')['Body'].read().decode('utf-8')

    # jinja2で扱えるテンプレートに変換する
    template = Template(template_str)

    # レンダリング内容
    data = {
        "name": "MATCHA",
        "is_login": True
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
