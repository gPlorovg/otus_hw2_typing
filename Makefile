.PHONY: build typing

build:
	@echo "Building docker container..."
	docker build -t python-typing .

typing:
	@echo "Running mypy for type checking..."
	docker run --rm -v $(CURDIR)/tasks:/app/tasks:ro python-typing
