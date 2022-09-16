VIDEO_DIR := resource/videos
THUMBNAIL_DIR := resource/thumbnails
INFO_JSON := ".info.json"


.PHONY: start
start:
	python -m server -d


.PHONY: db
db: thumbnails
	make -C db INFO_JSON=$(PWD)/$(INFO_JSON)


.PHONY: thumbnails
thumbnails:
	python -m thumbnail $(VIDEO_DIR) $(THUMBNAIL_DIR) $(INFO_JSON)


.PHONY: test
test:
	DB_PATH=$(PWD)/db/db.sqlite PYTHONPATH=$(PWD) pytest


.PHONY: clean
clean:
	rm -rf $(INFO_JSON) $(THUMBNAIL_DIR)/*.jpg
	make -C db clean
