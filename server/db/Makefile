DB_FILE := db.sqlite
RESOURCE_DIR := $(realpath $(PWD)/../resource)


.PHONY: load
load: $(DB_FILE)
	python load.py $(DB_FILE) $(RESOURCE_DIR)


$(DB_FILE):
	cat create.sql | sqlite3 $@


clean:
	rm $(DB_FILE)
