# para gerar imagem
docker build -f spark.df -t spark --force-rm .

# para ativar o cluster
docker-compose -f cluster.yml up -d

# rodar a aplicação 
docker-compose -f app.yml -p app up -d

# para desativar:
docker-compose -f app.yml -p app down
docker-compose -f cluster.yml down
