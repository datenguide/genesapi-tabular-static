import os
import requests
import uuid
from flask import Flask, request, redirect, render_template
from markdown import markdown


app = Flask(__name__)


GENESAPI_TABULAR_URL = os.getenv('GENESAPI_TABULAR_URL', 'https://tabular.genesapi.org')
GENESAPI_STATIC_DIR = os.getenv('GENESAPI_STATIC_DIR', 'tables')
GENESAPI_STATIC_URL = os.getenv('GENESAPI_STATIC_URL', '/tables')


@app.route('/')
def api():
    if not request.args:
        with open('./README.md') as f:
            content = markdown(f.read())
        return render_template('docs.html', content=content)

    url = GENESAPI_TABULAR_URL + '/?' + request.query_string.decode()
    res = requests.get(url)
    file_ext = 'json' if 'json' in res.headers['Content-Type'] else 'csv'
    table_name = '%s.%s' % (str(uuid.uuid4()).replace('-', ''), file_ext)
    with open(os.path.join(GENESAPI_STATIC_DIR, table_name), 'w') as f:
        f.write(res.text)
    return redirect('%s/%s' % (GENESAPI_STATIC_URL, table_name))
