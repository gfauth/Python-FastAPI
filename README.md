# Comandos do terminal

```shell
poetry shell ---- # Inicializer o serviço (primeiro comando a ser rodado para inicializar)
task --list ----- # Lista os comandos do taskipy
task lint ------- # Para chegar erros de boas praticas
task format ----- # Para formatar o código de acordo com as boas praticas
task run -------- # Para rodar a aplicação (executa 'fastapi dev fast_api/app.py')
task pre_test --- # Para rodar os testes (executa 'pytest --dov-fast_api -vv')
task test ------- # Para rodar e detalhar os testes (executa 'pytest -s -x --cov=fast_api -vv')
task post_test -- # Para verificar a cobertura dos testes em html (executa 'coverage html')
```
