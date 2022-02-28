echo "Running the command script"
mkdir -p /workspace/.dbt
ln -snf /workspace/.dbt ~/.dbt

export PGPASSWORD=gitpod PGDATABASE=dbt
export AIRFLOW__CORE__DAGS_FOLDER=/workspace/test-dbt-airflow/airflow/dags
export AIRFLOW__CORE__LOAD_EXAMPLES=False
# airflow standalone

