from flask import Flask, request, jsonify
from flask_cors import cross_origin
from yglu.main import process
from io import StringIO
from os import environ
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16384

origins = environ['CORS'] if 'CORS' in environ else ""


@app.route('/api/process', methods=['POST'])
@cross_origin(origins=origins)
def process_doc():
    input = request.json
    errors = []
    output = StringIO()
    filename = input['filename'] if 'filename' in input else None
    process(input['doc'], output, filename, errors)
    if len(errors) == 0:
        return jsonify({'doc': output.getvalue()})
    else:
        return jsonify({'errors': list(build_errors(errors))})


def build_errors(errors):
    for error in errors:
        result = dict()
        result['message'] = str(error)
        yield result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
