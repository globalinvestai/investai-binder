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