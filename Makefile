VENV_NAME = venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(PYTHON) -m pip
JUPYTER = $(PYTHON) -m jupyter

.PHONY: setup
setup: $(VENV_NAME)/bin/activate
	. $(VENV_NAME)/bin/activate && $(PIP) install -r requirements.txt
	$(PYTHON) -m ipykernel install --user --name=$(VENV_NAME)

$(VENV_NAME)/bin/activate:
	python3 -m venv $(VENV_NAME)

.PHONY: run
run: $(VENV_NAME)/bin/activate
	. $(VENV_NAME)/bin/activate && $(JUPYTER) notebook

.PHONY: clean
clean:
	rm -rf $(VENV_NAME)