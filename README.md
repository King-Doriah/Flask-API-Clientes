# Exemplo de uma API para pegar dados de Clientes armazenados em um Banco de Dados

Passos para usar:

1. Instalar o Python.

2. Instalar as seguintes dependências:

```
pip3 install flask
pip3 install pymysql
```

3. Criar o Banco de Dados (api) e a tabela (clientes):

```
CREATE DATABASE `api`;
```

```
CREATE TABLE `clientes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sobrenome` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `endereco` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefone` int(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```

5. Executa o código e inicia o servidor:
```
python api.py
```

6. Acessa a URL abaixo pelo navegador:
```
http://localhost:5000/
```
