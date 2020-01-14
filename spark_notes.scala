val files = Array(/user/root/flight_data/297004386_T_ONTIME_1.csv,
 /user/root/flight_data/297004386_T_ONTIME_2.csv,
/user/root/flight_data297004386_T_ONTIME_3.csv,
 /user/root/flight_data/297004386_T_ONTIME_4.csv,
 /user/root/flight_data/297004386_T_ONTIME_5.csv,
 /user/root/flight_data/297004386_T_ONTIME_6.csv,
 /user/root/flight_data/297043733_T_ONTIME_10.csv,
 /user/root/flight_data/297043733_T_ONTIME_11.csv,
 /user/root/flight_data/297043733_T_ONTIME_12.csv,
 /user/root/flight_data/297043733_T_ONTIME_7.csv,
 /user/root/flight_data/297043733_T_ONTIME_8.csv,
 /user/root/flight_data/297043733_T_ONTIME_9.csv)



val df = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_1.csv")

val df2 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_2.csv")

val df3 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_3.csv")

val df4 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_4.csv")

val df5 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_5.csv")

val df6 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297004386_T_ONTIME_6.csv")

val df7 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_7.csv")

val df8 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_8.csv")

val df9 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_9.csv")

val df10 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_10.csv")

val df11 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_11.csv")

val df12 = spark.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","true").load("hdfs:///user/root/flight_data/297043733_T_ONTIME_12.csv")

import org.apache.spark.sql.functions.{concat, lit}
import org.apache.spark.sql.types._
import org.apache.spark.sql.{SQLContext, _}
import org.apache.spark.sql.execution.datasources.hbase._
import org.apache.spark.{SparkConf, SparkContext}
import spark.sqlContext.implicits._

case class DelaysRecord(
    rowkey: String,
    dep: Double,
    arr: Double,
    )
val dest = df.select($"dest")
val rowkey = df.select(concat($"dest", lit("_"), $"origin").alias("rowkey")) //gets rowkey
val col_name = df.select(concat($"fl_date".cast(DateType), lit("_"), $"tail_num")) //dep and arr column name
val df.select($"arr_delay").where($"tail_num" === ("N3CTAA") and $"fl_date".cast(DateType) === "2016-01-01" and $"dest" === "DFW" and $"origin" === "MSP")
df.select($"dep_delay").where($"tail_num" === ("N3CTAA") and $"fl_date".cast(DateType) === "2016-01-01" and $"dest" === "DFW" and $"origin" === "MSP")

def createRow (Row row): DelaysRecord { val date = row(3).cast(DateType) val tail_num = row(7) val rowkey = concat(date, lit("_"),tail_num) val dep = row(16) val arr = row(17) return new DelaysRecord(rowkey, dep, arr)
}

val df = spark.read.format("csv").option("header","true").option("mode","FAILFAST").schema(schema).load("hdfs:///user/root/flight_data/297004386_T_ONTIME_1.csv")

val hbasedf = df.select(concat($"dest", lit("_"), $"origin").alias("rowkey"), concat($"fl_date", lit("_"), $"tail_num").alias("dep_name") , $"dep_delay".alias("dep_value"), concat($"fl_date", lit("_"), $"tail_num").alias("arr_name") , $"arr_delay".alias("arr_value"))

def catalog = s"""{
        |"table":{"namespace":"flights_spark", "name":"delays_spark"},
        |"rowkey":"key",
        |"columns":{
          |"col0":{"cf":"rowkey", "col":"key", "type":"string"},
          |"dep":{"cf":"dep", "col":"[flight_date]_[tail_num]", "type":"double"},
          |"arr":{"cf":"arr", "col":"[flight_date]_[tail_num]", "type":"double"},
        |}
      |}""".stripMargin




