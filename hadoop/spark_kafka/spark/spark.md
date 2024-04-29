## SPARK

### 환경변수 설저
```
getdit ~/.bashrc
```
```
export JAVA_HOME=/root/jdk1.8.0
export HADOOP_HOME=/root/hadoop

export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

export HIVE_HOME=/root/apache-hive-3.1.3
export PATH=$PATH:$HIVE_HOME/bin

export SQOOP_HOME=/root/sqoop
export SQOOP_CONF_DIR=/root/sqoop/conf
export PATH=$PATH:$SQOOP_HOME/bin:$PATH


export SPARK_HOME=/root/spark
export PATH=$PATH:$SPARK_HOME/bin:$PATH

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'
```
---
### spark 실행
var myRange = spark.range(1000).toDF("number")

var divisBy2 = myRange.where("number % 2 = 0")

divisBy2.show()

var flightData = spark.read.option("inferSchema","true").option("header","true").csv("2015-summary.csv")
# 2015-summary.csv 파일을 spark 폴더로 옮겨야 함.

flightData.show()

flightData.createOrReplaceTempView("flightData")

var flightData_sql=spark.sql("""
select DEST_COUNTRY_NAME, count(*)
from fightData
group by DEST_COUNTRY_NAME
""")

var flightData_gb = flightData.groupBy("DEST_COUNTRY_NAME").count()

import org.apache.spark.sql.functions.max

var result = flightData.select(max("count")).take(1)

var max_sql = spark.sql("""
select DEST_COUNTRY_NAME, sum(count) as des_total
from flightData
group by DEST_COUNTRY_NAME
order by sum(count) desc
limit 5
""")



var flight2015 = spark.read.option("inferSchema","true").option("header","true").csv("2015-summary.csv")

flight2015.show()

flight2015.createOrReplaceTempView("flight2015") # view 생성

var sql_flight2015 = spark.sql("""
select * from flight2015""")

sql_flight2015.show()

var sql_flight2015 = spark.sql("""
select ORIGIN_COUNTRY_NAME, sum(count) from flight2015 group by ORIGIN_COUNTRY_NAME
order by sum(count) desc""")

sql_flight2015.show()

flight2015.groupBy("ORIGIN_COUNTRY_NAME").sum("count").withColumnRenamed("sum(count)","origin_total").sort(desc("origin_total")).show()

import spark.implicits._

case class Flight(DEST_COUNTRY_NAME: String, ORIGIN_COUNTRY_NAME: String, count: BigInt)

# linux
mkdir -p flight_data/parquet
mv part-r-00000-1a9822ba-b8fb-4d8e-844a-ea30d0801b9e.gz.parquet flight_data/parquet/

# spark
var flightDF = spark.read.parquet("./flight_data/parquet")
var flights = flightDF.as[FLIGHT]
flights.show()


# linux에서 pyspark 실행
range_ = spark.range(1000).toDF("number")

range_.show()
print(range_)

df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("bydata/by-day/*.csv")

df.show()

df.createOrReplaceTempView("retail_data")

from pyspark.sql.functions import window,column,desc,col

df.schema
staticSchema = df.schema

df.selectExpr("CustomerId","(UnitPrice*Quantity) as total_count","InvoiceDate").groupBy( col("CustomerID"), window(col("InvoiceDate"), "1 day")).sum("total_count").show(5)

streamingDF = spark.readStream.schema(staticSchema).option("maxFilesPerTrigger",1).format("csv").option("header","true").load("./bydata/by-day/*.csv")



### 실시간 처리
purchaseByCustomerPerHour = streamingDF.selectExpr("CustomerID","(Quantity*UnitPrice) as total_cost","InvoiceDate").groupBy(col("CustomerID"),window(col("InvoiceDate"), "1 day")).sum("total_cost")


purchaseByCustomerPerHour.writeStream.format("memory").queryName("customer_purchases").outputMode("complete").start()

purchaseByCustomerPerHour.writerStream.format("memory").queryName("customer_purchase").outputMode("complete").start().awaitTermination()


spark.sql("""select * from customer_purchases order by 'sum(total_cost)' desc""").show(5)


from pyspark.sql.functions import date_format, col


preparedDF = df.na.fill(0).withColumn('day_of_week', date_format(col('InvoiceDate'), "EEEE")).coalesce(5)

train_df = preparedDF.where("Invoicedate < '2011-07-01'")

trainDataFrame = preparedDF.where("InvoiceDate >= '2011-07-01'")


### jupyter lab install

gedit ~/.bashrc

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'

source ~/.bashrc

pip install jupyterlab
# pip install -y python3-pip

pyspark
=> jupyter lab 열림

# jupyter lab 실행

rom pyspark.ml.feature import StringIndexer
indexer = StringIndexer().setInputCol("day_odf_week").setOutPutCol("day_of_week_index")


MLOPS => 파이프라인
