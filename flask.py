"configurations": [
  {
    "name": "Python: Flask",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": {
      "FLASK_APP": "server/run.py",
      "FLASK_ENV": "development",
      "FLASK_DEBUG": "0"
    },
    "args": ["run", "--no-debugger", "--no-reload"],
    "jinja": true
  }
]