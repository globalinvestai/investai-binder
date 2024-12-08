# investai-binder


###Miniconda
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
###

conda create -y -n pyspark_conda_env -c conda-forge pyarrow pandas conda-pack
conda activate pyspark_conda_env
conda pack -f -o pyspark_conda_env.tar.gz


python3 -m pip install pyspark.pandas

# To activate this environment, use                                                                                                                        
#                                                                                                                                                          
#     $ conda activate pyspark_conda_env                                                                                                                   
#                                                                                                                                                          
# To deactivate an active environment, use                                                                                                                 
#                                                                                                                                                          
#     $ conda deactivate       

https://github.com/globalinvestai/investai-binder


https://mybinder.org/v2/gh/globalinvestai/investai-binder/HEAD


https://mybinder.org/v2/gh/apache/spark/32232e9ed33?filepath=python%2Fdocs%2Fsource%2Fgetting_started%2Fquickstart_df.ipynb

$ docker build - < Dockerfile


brew install apache-spark




use a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install pyspark numpy pandas