# yglu-server
Yglu ᕄ as a service for demo purposes.

## Requirements

``` 
pip3 install yglu flask flask-cors
```

## Run

```
FLASK_APP=server.py [CORS=<allowed-origins>] flask run
```

## API

**`POST`** `/yglu/process`

Request:

```json
{
    "doc": "a: !? 1 + 1",
    "filename": "input.yml"
}
```

- `doc`: The YAML input. **Required**.
- `filename`: A filename to use in the error report.

Response:

```json
{
    "doc": "a: 2"
}
```

- `doc`: The YAML output.

```json
{
    "errors": [
        {
            "message": "unexpected end of input...",
            "start": {
                "line": 2,
                "column": 3
            },
            "end": {
                "line": 2,
                "column": 4
            }
        }             
    ]
}
```

- `errors`: List of processing errors