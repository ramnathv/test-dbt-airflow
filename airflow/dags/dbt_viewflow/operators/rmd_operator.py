from airflow.models.baseoperator import BaseOperator
import os

class RmdOperator(BaseOperator):
    def __init__(self, input: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.input = input

    def execute(self, context):
        cmd_rmd_render = f"rmarkdown::render('{self.input}', output_dir='/tmp', clean=TRUE, run_pandoc=FALSE)"
        cmd_rscript = f"Rscript -e '{cmd_rmd_render}'"
        print(cmd_rscript)
        os.system(cmd_rscript)