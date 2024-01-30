# Derivando da imagem oficial do PostgreSQL
FROM postgres:latest

# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/

