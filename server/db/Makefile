DB_FILE := db.sqlite
LOADED := load.done


$(LOADED): $(DB_FILE)
	python load.py $(DB_FILE) $(INFO_JSON)
	touch $@


$(DB_FILE):
	@cat create.sql | sqlite3 $@


clean:
	rm -rf $(DB_FILE) $(LOADED)
