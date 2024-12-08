$ export DLDG_DATA_DIR=~/path/to/delta-lake-definitive-guide/datasets/
$ export DLDG_CHAPTER_DIR=~/path/to/delta-lake-definitive-guide/ch05
$ docker run --rm -it \
 --name delta_quickstart \
 -v $DLDG_DATA_DIR/:/opt/spark/data/datasets \
 -v $DLDG_CHAPTER_DIR/:/opt/spark/work-dir/ch05 \
 -p 8888-8889:8888-8889 \
 delta_quickstart