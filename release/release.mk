export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
export UPLOADED_PATH := $(PWD)/resource/uploaded


export STATIC_PATH := $(PWD)/static
export PORT=80


.PHONY: buld
build:
	cd ../client && npm run build


.PHONY: start
start: build
	./run
