export DB_PATH := $(PWD)/db/db.sqlite
export RESOURCE_PATH := $(PWD)/resource
export STATIC_PATH := $(PWD)/static
export PORT=80


DEST := ~/Library/LaunchAgents
PLIST := info.hotoku.streaming.plist


.PHONY: load
load: $(PLIST) unload clear-log build
	cp $< $(DEST)
	launchctl load $(DEST)/$<


.PHONY: buld
build:
	cd ../client && npm run build


.PHONY: clean
clean: unload clear-log
	rm -f $(PLIST)


.PHONY: unload
unload:
	launchctl unload $(DEST)/$(PLIST)
	rm -f $(DEST)/$(PLIST)


.PHONY: clear-log
clear-log:
	rm -f server.err server.out


%: %.jinja
	jinja2 -D pwd=$(PWD) \
		-D label=$(subst .plist,,$(PLIST)) \
		-D DB_PATH=$(DB_PATH) \
		-D RESOURCE_PATH=$(RESOURCE_PATH) \
		-D STATIC_PATH=$(STATIC_PATH) \
		-D PORT=$(PORT) \
		$< > $@


.PHONY: start
start:
	./run
