print("hello")
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
a1=SparkSession.builder.appName('practice1').getOrCreate()
#print(a1)
df_pyspark=a1.read.csv("test1_cvs")
