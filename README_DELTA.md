Step 1: Create a Dockerfile

Create a Dockerfile with the following content to set up a Spark environment with Scala, Java, and Python:

FROM spark:3.5.1-scala2.12-java17-ubuntu
USER root
RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip; \
    rm -rf /var/lib/apt/lists/*
# Install PySpark
RUN pip3 install pyspark
USER spark
# Add PySpark to PATH for the spark user
ENV PATH=$PATH:/home/spark/.local/bin
Step 2: Build the Docker Image

Build the Docker image using the Dockerfile:

docker buildx build -t my-spark:3.5.1 .
Step 3: Start the Docker Container

Run the Docker container:

docker run -it --name spark-test --user root -p 4040:4040 -p 7077:7077 -p 8080:8080 my-spark:3.5.1 /bin/bash

# Inside the container 
# Start Spark master
$SPARK_HOME/sbin/start-master.sh
# Find the container IP address
container_ip=$(hostname -I | awk '{print $1}')
# Start Spark worker
$SPARK_HOME/sbin/start-worker.sh spark://$container_ip:7077
Now, you should be able to access the Spark web UI by navigating to http://localhost:8080 in your browser.


Step 4: Set Environment Variables

Inside the Docker container, set the necessary environment variables:

export JAVA_HOME=/opt/java/openjdk
export PYSPARK_PYTHON=$(which python3)
export SPARK_VERSION=3.5
Step 5: Run PySpark with Hudi Configuration

Install the Delta Lake Python package (delta-spark):

pip3 install delta-spark==3.2.0


Step 2: Start PySpark Shell with Delta Lake Configuration
Start the PySpark shell with the necessary Delta Lake configurations:
pyspark --packages io.delta:delta-spark_2.12:3.2.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

Step 3: Test Delta Lake in PySpark Shell
Once the PySpark shell starts, run the following commands to test Delta Lake:
from delta import *

builder = spark.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Create a Delta table
data = spark.range(0, 5)
data.write.format("delta").save("/tmp/delta-table")

# Read data from the Delta table
df = spark.read.format("delta").load("/tmp/delta-table")
df.show()
output:


Conclusion
By following the steps outlined in this guide, you have successfully set up and tested Delta Lake in an existing Apache Spark Docker container. This setup allows you to leverage the powerful features of Delta Lake, such as ACID transactions and scalable metadata handling, within your Spark environment. With Delta Lake integrated, you can now perform more reliable and efficient data processing and analytics. Whether you are working on data engineering, data science, or big data analytics, this setup provides a robust foundation for your projects. Happy coding!         
