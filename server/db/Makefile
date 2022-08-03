DB_FILE := db.sqlite


.PHONY: load
load: $(DB_FILE)
	python load.py $(DB_FILE)


$(DB_FILE):
	cat create.sql | sqlite3 $@


clean:
	rm $(DB_FILE)
