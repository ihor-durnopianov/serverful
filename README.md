# Serverful

The way I see it, we express custom entities as classes.  Web server is a custom entity.  Why do we express it as a global variable?

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

One may use [application factory](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) so that `app` is at least not global, but half of the problem (well, not really problem) still remains.

Serverful proposes this instead

```python
from serverful import Server

class App(Server):

    @expose(rule='/')
    def hello_world(self):
        return 'Hello, World!'
```

That's it.
