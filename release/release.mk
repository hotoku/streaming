export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
export UPLOADED_PATH := $(PWD)/resource/uploaded
export ROOT_PATH := $(PWD)/../client/build


export PORT=80


.PHONY: buld
build:
	cd ../client && npm run build


.PHONY: start
start: build
	./run


.PHONY: debug
debug: build
	cd ../server && PORT=8081 poetry run python -m server -d
