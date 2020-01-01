help:
	@echo "Makefile Help:"
	@echo ""
	@echo "install			install my_cookies in current python env"
	@echo "run			run my_cookies installed in current python env"

install:
	pip install -e .

run:
	~/.virtualenvs/dev_env/bin/my_cookies
