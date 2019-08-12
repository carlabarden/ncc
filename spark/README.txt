# Para gerar imagem
docker build -f spark.df -t spark --force-rm .


# Agora, o driver de rede é criado como overlay, portanto, para o correto funcionamento,
# deve-se iniciar o swarm mode.
# Não tem problema, para o teste, ter apenas um nó. Ele apenas escalonará
# todos os conteineres localmente.
docker swarm init


# Para ativar o cluster
docker stack deploy --compose-file cluster.yml spark


# Como está no swarm mode, os contêineres demoram um pouco para serem lançados.
# Para verificar o status:
docker stack ps spark


# Rodar a aplicação, iterativo
## Criar o container (considerando estar no diretório spark --- pwd)

docker run -it -p 4040:4040 -p 8088:8088 -p 8042:8042 -e SPARK_MASTER=spark://spark-master:7077 -e SPARK_PUBLIC_DNS=127.0.0.1 --network spark_nw --link spark-master:spark-master -v $(pwd)/data:/data -v $(pwd)/src:/src  spark:latest


## Dentro do container, iniciar a aplicação
### A saída estará em data/out
### Para a aplicação funcionar, o diretorio out/ não deve existir

/spark/bin/spark-submit --class my.main.Application --master spark://spark-master:7077 /src/main.py


## Desativando cluster
docker stack rm spark 


# Desativando o swarm mode
docker swarm leave --force
