DIR="ADAM_VENV"

if ! [ -d "$DIR" ] ; then
    echo "Creating VENV"
	python3 -m venv ADAM_VENV
	echo "Activating Source"
	source ADAM_VENV/bin/activate
	echo "Upgrading PIP"
	pip install --upgrade pip
	echo "Installing Requirements"
	pip install -r requirements.txt
	echo "Initializing Databases"
	export FLASK_APP=adam_v2
	flask db init --multidb
	flask db migrate -m "Initial Migration"
	flask db upgrade
	echo "Adding intial user"
	python create_initial_user.py
    chmod +x run.sh
	echo "ADAM Server has been installed!"
	echo "Starting ADAM Server for 10 minutes, afterwards execute it with command: ./run.sh"
	timeout 600s gunicorn -k gevent -w 1 -b :5000 adam_v2:app --certfile=testing.crt --keyfile=testing.key	
fi
