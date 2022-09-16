DB_FILE := db.sqlite
LOADED := load.done


$(LOADED): $(DB_FILE)
	@echo INFO_JSON $(INFO_JSON)
	python load.py --json-path=$(INFO_JSON)
	touch $@


$(DB_FILE):
	@cat create.sql | sqlite3 $@


clean:
	rm -rf $(DB_FILE) $(LOADED)
