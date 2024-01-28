#Derivando da iamgem oficial do MySQL
FROM MySQL:5.7

#Adicionando os scripts SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/
