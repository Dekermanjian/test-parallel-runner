"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import sum_data
from test_parallel_runner import settings

def create_pipeline(**kwargs) -> Pipeline:
    dp_pipeline =  pipeline([
        node(
            func=sum_data,
            inputs=['simple_data', 'params:group'],
            outputs='summed_data',
            name='sum_data'
        )
    ])

    pipes = []
    for group in settings.DYNAMIC_PIPELINES_MAPPING:
        pipes.append(
            pipeline(
                dp_pipeline,
                inputs={
                    "simple_data": "simple_data",
                },
                outputs={
                    "summed_data": f"RPM_patient_model_dataset_{group}",
                },
                parameters={
                    "params:group": group,
                },
                namespace=f"{group}",
            )
        )
    return sum(pipes)
