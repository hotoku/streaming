ifeq ($(TEST),true)
export DB_PATH := $(PWD)/../server/db/db.sqlite
export RESOURCE_PATH := $(PWD)/../server/resource
else
export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
endif


export STATIC_PATH := $(PWD)/static
export PORT=80


.PHONY: buld
build:
	cd ../client && npm run build


.PHONY: start
start: build
	./run
