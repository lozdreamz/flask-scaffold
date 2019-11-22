export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
export FLASK_APP=autoapp.py
export APP_SECRET=somesecretbytes
export FLASK_DEBUG=1
# export PYTHONWARNINGS=ignore::DeprecationWarning
flask run
