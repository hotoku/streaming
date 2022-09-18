export INFO_JSON := $(PWD)/.info.json
export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
export STATIC_PATH := $(PWD)/static


VIDEO_DIR = $(RESOURCE_PATH)/videos
THUMBNAIL_DIR = $(RESOURCE_PATH)/thumbnails


define indent
@echo "   "$1
endef


.PHONY: usage
usage:
	@echo available commands are following:
	$(call indent,"make db")
	$(call indent,"make clean")
	$(call indent,"make run")


.PHONY: db
db: thumbnails
	make -C db


.PHONY: thumbnails
thumbnails:
	cd ../server && python -m thumbnail \
		$(PWD)/prefix.json $(VIDEO_DIR) $(THUMBNAIL_DIR) $(INFO_JSON) \
		--pos "00:00:20.000"


.PHONY: clean
clean:
	rm -rf $(INFO_JSON) $(THUMBNAIL_DIR)/*.jpg
	make -C db clean


.PHONY: run
run:
#	ok
#	PORT=3000 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/../server/db/db.sqlite RESOURCE_PATH=$(PWD)/../server/resource exec python -m server -d
# ng: permission
#	PORT=80 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/../server/db/db.sqlite RESOURCE_PATH=$(PWD)/../server/resource exec python -m server -d
# ok
#	PORT=80 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/../server/db/db.sqlite RESOURCE_PATH=$(PWD)/../server/resource exec python -m server
# ng: server runs but JS does not work in browser
#	PORT=80 DB_PATH=$(PWD)/db/db.sqlite RESOURCE_PATH=$(PWD)/resource exec python -m server
# ng: same as above. accessing curl works
#	PORT=80 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/db/db.sqlite RESOURCE_PATH=$(PWD)/resource exec python -m server
# ok: JS work in browser
#	PORT=80 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/../server/db/db.sqlite RESOURCE_PATH=$(PWD)/resource exec python -m server
# ng: server runs but JS does not work in browser. accessing curl works
#	PORT=80 STATIC_PATH=$(PWD)/static DB_PATH=$(PWD)/db/db.sqlite RESOURCE_PATH=$(PWD)/../server/resource exec python -m server
# ng: server runs but JS does not work in browser. accessing curl works
	PORT=80 exec python -m server


#	gunicorn --bind :80 --workers 1 --threads 8 --timeout 0 server.server:app
