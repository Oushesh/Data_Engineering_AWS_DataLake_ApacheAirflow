# Data_Engineering_AWS_DataLake_ApacheAirflow
Sample workflow for Data Engineering


## Tech Stack:
    Apache Airflow
    * https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html
    
    Docker
    AWS
      AWS Glue
      AWS Athena, AWS S3


## Machine Learning Operations Framework setup and operations:
   + Install Airflow from its main website: https://airflow.apache.org/docs/apache-airflow/stable/start.html
   + once installed: airflow standalone
   + Configure airflow environment
        -- airflow db init
   + then run the code.
   + We also need to build authentication system before running the airflow db init 
        command. You do it like the following: 
        airflow users create -r Admin -u oushesh -e oushesh@gmail.com -f oushesh -l haradhun -p <password>