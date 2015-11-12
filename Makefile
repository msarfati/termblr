SHELL=/bin/bash
PROJECT_NAME=Termblr
MOD_NAME=Termblr
TEST_CMD=SETTINGS=$$PWD/etc/testing.conf nosetests -w $(MOD_NAME)
TEST_DUMP="./maketests.log"

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`
	find . -name "__pycache__" -delete

server:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py runserver

shell:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	rm -f $(TEST_DUMP)
	$(TEST_CMD) -c etc/nose/test.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg

db:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py populate_db

dbshell:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py dbshell

upgradedb:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py db upgrade

migratedb:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py db migrate


.PHONY: clean install test server watch db single docs shell upgradedb migratedb dbshell test-server deps-linux upgrade