from airflow import DAG
from datetime import datetime
import airflow_dbt
import dagfactory
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtSnapshotOperator,
    DbtRunOperator,
    DbtTestOperator,
)

DbtRunOperator.ui_color = '#f5f5dc'

# from pathlib import Path
# import sys
# path_root = Path(__file__).parents[2]
# sys.path.append(str(path_root))
# print(sys.path)

from dbt_viewflow.operators.rmd_operator import RmdOperator
RmdOperator.ui_color = '#5F9EA0'

dag_factory = dagfactory.DagFactory("/workspace/test-dbt-airflow/airflow/dags/analytics/core/core.yml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())