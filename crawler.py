from inscrawler import InsCrawler
from flask import request
import json
from io import open
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fetch_hash_tag():
    hash_tag = request.args.get('hash_tag')
    print(hash_tag)
    if hash_tag is None:
        return 'Error! The "hash_tag" parameter is required.'
    photos = json.dumps(get_posts_by_hashtag(hash_tag, 15))
    return photos


def get_posts_by_hashtag(tag, number):
    ins_crawler = InsCrawler()
    return ins_crawler.get_latest_posts_by_tag(tag, number)


def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)
    if filepath:
        with open(filepath, 'w') as f:
            f.write(out)
    else:
        print(out)
    return out


if __name__ == '__main__':
    app.run(debug=True)
