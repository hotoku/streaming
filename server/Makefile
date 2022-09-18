export INFO_JSON := $(PWD)/.info.json
export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
VIDEO_DIR = $(RESOURCE_PATH)/videos
THUMBNAIL_DIR = $(RESOURCE_PATH)/thumbnails


define indent
@echo "   "$1
endef


.PHONY: usage
usage:
	@echo available commands are following:
	$(call indent,"make start")
	$(call indent,"make db")
	$(call indent,"make clean")


.PHONY: start
start:
	python -m server -d


.PHONY: db
db: thumbnails
	make -C db


.PHONY: thumbnails
thumbnails:
	python -m thumbnail prefix.json $(VIDEO_DIR) $(THUMBNAIL_DIR) $(INFO_JSON) --use-pathlib


.PHONY: test
test:
	DB_PATH=$(PWD)/db/db.sqlite pytest


.PHONY: clean
clean:
	rm -rf $(INFO_JSON) $(THUMBNAIL_DIR)/*.jpg
	make -C db clean
