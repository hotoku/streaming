LOADED := load.done


$(LOADED): $(DB_PATH)
	./load.py $(DB_PATH) $(INFO_JSON)
	touch $@


$(DB_PATH):
	@cat create.sql | sqlite3 $@


clean:
	rm -rf $(DB_PATH) $(LOADED)
