# Tornado API RESTfull- Python

##English

This is a simple example, to implements a http web server (API RESTfull) with python (tornado framework).


###Dependencies

| Dependency        | For what?           | Link  |
| ------------- |:-------------:| -----:|
| tornado | web framework server    |    https://www.tornadoweb.org/ |
| pymongo      | mongo database driver | https://api.mongodb.com/python/current/ |
| marshmallow      | fileds schema validator     |   https://marshmallow.readthedocs.io |
| logzero | create application logs   |    https://logzero.readthedocs.io/en/latest/ |

###Architecture
**Handlers** - It is the layer responsible for handling requests

**Persistence** - Responsible layer for centralizing information and database connection.

**Schemas** - Responsible for manipulating fields and data.

**Util** - Gather higher-use codes in the project

**Settings** - Project Settings

###Run
After preparing your environment and your virtualenv, follow the steps:

* `cd project-folder`
* `pip install -r requeriments.txt`
* `python main.py`

##


##Português - Brasil

Este é um exemplo simples, para implementar um servidor web http (API RESTfull) com python (framework tornado).


###Dependências

| Dependência | Para quê? | Link |
| ------------- |: -------------: | -----: |
| tornado | servidor de estrutura web | https://www.tornadoweb.org/ |
| pymongo | driver de conexão com o banco de dados mongo | https://api.mongodb.com/python/current/ |
| marshmallow | validador de campos e dados | https://marshmallow.readthedocs.io |
| logzero | criar logs da aplicação | https://logzero.readthedocs.io/en/latest/ |

###Arquitetura
**Handlers** - É a camada responsável por manipular as requisições

**Persistence** - Camada responsável por centralizar informações e conexão de banco de dados.

**Schemas** - Responsável pela manipulação de campos e dados.

**Util** - Reúne códigos de uso mais alto (repetitivos) no projeto

**Settings** - Configurações do projeto

###Executar a aplicação
Depois de preparar seu ambiente e seu virtualenv, siga os passos:

* `cd project-folder`
* `pip install -r requeriments.txt`
* `python main.py`