// spark-shell --packages com.hortonworks:shc-core:1.1.1-2.1-s_2.11 --repositories https://repo.hortonworks.com/content/groups/public/
import org.apache.spark.sql.functions.{concat, lit}
import org.apache.spark.sql.types._
import org.apache.spark.sql.{SQLContext, _}
import org.apache.spark.sql.execution.datasources.hbase._
import org.apache.spark.{SparkConf, SparkContext}
import spark.sqlContext.implicits._


object SparkETL{

    def main(args: Array[String]): Unit = {
        catalog
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

        val df = spark.read.format("csv").option("header","true").option("mode","FAILFAST").schema(schema).load("hdfs:///user/root/flight_data/297004386_T_ONTIME_1.csv")
    }

case class DelaysRecord(rowkey: String,dep: Double, arr: Double)

val schema = StructType(
  List(
    StructField("YEAR", IntegerType, true),
    StructField("MONTH", IntegerType, true),
    StructField("DAY_OF_MONTH", IntegerType, true),
    StructField("fl_date", DateType, true),
    StructField("UNIQUE_CARRIER", StringType, true),
    StructField("AIRLINE_ID", IntegerType, true),
    StructField("CARRIER", StringType, true),
    StructField("TAIL_NUM", StringType, true),
    StructField("FL_NUM", IntegerType, true),
    StructField("ORIGIN_AIRPORT_ID", IntegerType, true),
    StructField("ORIGIN_AIRPORT_SEQ_ID", IntegerType, true),
    StructField("ORIGIN", StringType, true),
    StructField("DEST_AIRPORT_ID", IntegerType, true),
    StructField("DEST_AIRPORT_SEQ_ID", IntegerType, true),
    StructField("DEST", StringType, true),
    StructField("DEP_DELAY", DoubleType, true),
    StructField("ARR_DELAY", DoubleType, true),
    StructField("CANCELLED", DoubleType, true),
    StructField("DIVERTED", DoubleType, true),
    StructField("DISTANCE", DoubleType, true),
    StructField("_c20", StringType, true)
    )
)


val df = spark.read.format("csv").option("header","true").option("mode","FAILFAST").schema(schema).load("hdfs:///user/root/flight_data/297004386_T_ONTIME_1.csv")

val hbasedf = df.select(concat($"dest", lit("_"), $"origin").alias("rowkey"), concat($"fl_date", lit("_"), $"tail_num").alias("dep_name") , $"dep_delay".alias("dep_value"), concat($"fl_date", lit("_"), $"tail_num").alias("arr_name") , $"arr_delay".alias("arr_value"))


def createRow (row: Row): DelaysRecord = {
    val date = row(3)
    val tail_num = row(7)
    val rowkey = date + "_" + tail_num
    val dep = row(16)
    val arr = row(17)
    return new DelaysRecord(rowkey, dep, arr)
}



def catalog = s"""{
        |"table":{"namespace":"flights_spark", "name":"delays_spark"},
        |"rowkey":"key",
        |"columns":{
          |"col0":{"cf":"rowkey", "col":"key", "type":"string"},
          |"dep":{"cf":"dep", "col":"[flight_date]_[tail_num]", "type":"double"},
          |"arr":{"cf":"arr", "col":"[flight_date]_[tail_num]", "type":"double"},
        |}
      |}""".stripMargin
}





