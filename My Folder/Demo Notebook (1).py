# Databricks notebook source
print("Hello Jobax")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL"

# COMMAND ----------

# MAGIC %run ./Includes/SetUp

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls "/databricks-datasets"

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

display(files)

# COMMAND ----------


