# Tornado API RESTfull- Python

## English

This is a simple example, to implements a http web server (API RESTfull) with python (tornado framework).


### Dependencies

| Dependency        | For what?           | Link  |
| ------------- |:-------------:| -----:|
| tornado | web framework server    |    https://www.tornadoweb.org/ |
| pymongo      | mongo database driver | https://api.mongodb.com/python/current/ |
| marshmallow      | fileds schema validator     |   https://marshmallow.readthedocs.io |
| logzero | create application logs   |    https://logzero.readthedocs.io/en/latest/ |

### Architecture
**Handlers** - It is the layer responsible for handling requests

**Persistence** - Responsible layer for centralizing information and database connection.

**Schemas** - Responsible for manipulating fields and data.

**Util** - Gather higher-use codes in the project

**Settings** - Project Settings

### Run
After preparing your environment and your virtualenv, follow the steps:

* `cd project-folder`
* `pip install -r requeriments.txt`
* `python main.py`

Run application with docker:
* `cd project-folder`
* `docker build -t api-tornado .`
* `docker run -d -p 8081:8081 --name api-tornado api-tornado:latest`

##


## Português - Brasil

Este é um exemplo simples, para implementar um servidor web http (API RESTfull) com python (framework tornado).


### Dependências

| Dependência        | Qual o uso?           | Link  |
| ------------- |:-------------:| -----:|
| tornado | servidor web    |    https://www.tornadoweb.org/ |
| pymongo      | conexão com o banco de dado NoSQL mongo | https://api.mongodb.com/python/current/ |
| marshmallow      | validação de capos e dados     |   https://marshmallow.readthedocs.io |
| logzero | criação de logs da applicação   |    https://logzero.readthedocs.io/en/latest/ |

### Arquitetura
**Handlers** - É a camada responsável por manipular as requisições

**Persistence** - Camada responsável por centralizar informações e conexão de banco de dados.

**Schemas** - Responsável pela manipulação de campos e dados.

**Util** - Reúne códigos de uso mais alto (repetitivos) no projeto

**Settings** - Configurações do projeto

### Executar a aplicação
Depois de preparar seu ambiente e seu virtualenv, siga os passos:

* `cd project-folder`
* `pip install -r requeriments.txt`
* `python main.py`

Executar a aplicação com docker:
* `cd project-folder`
* `docker build -t api-tornado .`
* `docker run -d -p 8081:8081 --name api-tornado api-tornado:latest`