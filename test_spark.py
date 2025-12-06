from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("WSL-Test") \
    .master("local[4]") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

spark.range(10).show()
