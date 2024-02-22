# set environment variables for `flask run` and `rq worker` for development
# in production, the variables should be set in systemd or docker files
export FLASK_APP=isimip_files_api.app
export FLASK_ENV=development
export RQ_WORKER_CLASS=isimip_files_api.worker.Worker

server:
	flask run

worker:
	rq worker

.PHONY: server worker