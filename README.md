# yglu-server
Yglu ᕄ as a service for demo purposes.

## Requirements

``` 
pip3 install yglu flask
```

## Run

```
FLASK_APP=yglu-server.py flask run
```

## API

**`POST`** `/api/process`

Request:

```json
{
    "doc": "a: 1",                                   // (required) YAML input
    "filename": "input.yml"                          // Filename for error reports
}
```

Response:

```json
{
    "doc": "a: !? ",                                 // YAML output
    "errors": [                                      // Processing errors
        {
            "message": "unexpected end of input..."
        }             
    ]
}
```