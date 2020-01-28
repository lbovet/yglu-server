from flask import Flask, request, jsonify
from flask_cors import cross_origin
from yglu.main import process
from yglu.tree import NodeException
from io import StringIO
from os import environ
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16384

origins = environ['CORS'] if 'CORS' in environ else [
    "http://localhost:8888", "http://yglu.io"]


@app.route('/yglu/process', methods=['POST'])
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
        result['message'] = str(error).splitlines()[0]
        if isinstance(error, NodeException):
            result['start'] = {
                'line': error.start_mark().line,
                'column': error.start_mark().column
            }
            result['end'] = {
                'line': error.end_mark().line,
                'column': error.end_mark().column
            }
        elif hasattr(error, 'problem_mark'):
            result['message'] = error.problem
            mark = {
                'line': error.problem_mark.line,
                'column': error.problem_mark.column
            }
            result['start'] = mark
            result['end'] = mark
        else:
            result['start'] = {0, 0}
            result['end'] = {0, 0}
        yield result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
