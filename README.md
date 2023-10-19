# python-microservices-devops

[![Python application test with Github Actions](https://github.com/locemarn/python-microservices/actions/workflows/devops.yml/badge.svg)](https://github.com/locemarn/python-microservices/actions/workflows/devops.yml)

## Steps
1. Create a Python Virtual Environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
2. Create an empty files:
- touch requirements.txt
- touch Dockerfile
- touch Makefile
- mkdir mylib
- touch mylib/__init__.py
- touch mylib/logic.py
- touch main.py
3. Populate Makefile
4. Setup Cotinuous Integration, i.e check code for issues like lint errors
  <img width="1344" alt="Captura de Tela 2023-10-19 às 18 34 31" src="https://github.com/locemarn/python-microservices/assets/31143542/ff10c64d-e056-40f2-9ad5-1d6588bd5a84">
5. Build CLI using Python Fire lib ` ./cli-fire.py --help` to test logic
