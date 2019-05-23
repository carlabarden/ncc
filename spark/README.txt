# para gerar imagem
docker build -f spark.df -t spark --force-rm .

# para ativar o cluster
docker-compose -f cluster.yml up -d


# rodar a aplicação, iterativo
## criar o container (considerando estar dentro do diretório spark --- pwd)

docker run -it -p 4040:4040 -p 8088:8088 -p 8042:8042 -e SPARK_MASTER=spark://spark-master:7077 -e SPARK_PUBLIC_DNS=127.0.0.1 --network spark_default --link spark-master:spark-master -v $(pwd)/data:/data -v $(pwd)/src:/src  spark:latest


## dentro do container, iniciar a aplicação
### a saída estará em data/out
### para a aplicação funcionar, o diretorio out/ não deve existir

/spark/bin/spark-submit --class my.main.Application --master spark://spark-master:7077 /src/main.py


# rodar a aplicação, automático -- **** ERRO DNS na hora de rodar - ver nos logs do spark quando testar ****
docker-compose -f app.yml -p app up -d

# para desativar:
## se usado o app.yml
docker-compose -f app.yml -p app down

## desativando cluster
docker-compose -f cluster.yml down
