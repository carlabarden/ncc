from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("wordcount").setMaster("spark://spark-master:7077")
sc = SparkContext(conf = conf)

text_file = sc.textFile("/data/in/arq.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("/data/out")
