VIDEO_DIR := resource/videos
THUMBNAIL_DIR := resource/thumbnails
INFO_JSON := ".info.json"


.PHONY: db
db: thumbnails
	make -C db INFO_JSON=$(PWD)/$(INFO_JSON)


.PHONY: thumbnails
thumbnails:
	python -m thumbnail $(VIDEO_DIR) $(THUMBNAIL_DIR) --json-path=$(INFO_JSON)


.PHONY: clean
clean:
	rm -rf $(INFO_JSON) $(THUMBNAIL_DIR)/*.jpg
	make -C db clean
