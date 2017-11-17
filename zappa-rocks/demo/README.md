# Demo app

## Instalation

```bash
$ python3.6 -m venv .env --without-pip
$ . .env/bin/activate
(.env) $ curl https://bootstrap.pypa.io/get-pip.py | python
(.env) $ deactivate
$ . .env/bin/activate
(.env) $ pip install -r requirements.txt
```

## Usage

```bash
(.env) $ export FLASK_APP=app.py
(.env) $ flask run
```

## Zappa initial deploy

```bash
(.env) $ pip install zappa
(.env) $ zappa init
...
(.env) $ zappa deploy dev
```
## Zappa update

```bash
(.env) $ zappa update dev
```

## Zappa Scheduling

```json
{
  ...
  "dev": {
      ...
      "events": [{
        "function": "schedule.schedule_function",
        "expression": "rate(1 minute)"
      }],
      ...
  }
  ...
}
```

```bash
(.env) $ zappa schedule dev
```

```bash
(.env) $ zappa unschedule dev
```

## Zappa invoke

```bash
(.env) $ zappa invoke dev "print(\"PyConAr {}\".format(2000 + 17))" --raw
```

## Zappa Undeploy

```bash
(.env) $ zappa undeploy dev
```
