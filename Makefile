help:
	@echo "Makefile Help:"
	@echo ""
	@echo "install			install my_cookies in current python env"
	@echo "run			run my_cookies installed in current python env"
	@echo "package			build package"
	@echo "upload			upload package"
	@echo "clean			clean builds"

install:
	pip install -e .

run:
	@~/.virtualenvs/dev_env/bin/my_cookies

package:
	@python setup.py sdist bdist_wheel

upload:
	@twine upload --verbose dist/*

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *egg-info/
