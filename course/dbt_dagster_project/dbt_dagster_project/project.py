from pathlib import Path

from dagster_dbt import DbtProject

dbt_course_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_course").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
dbt_course_project.prepare_if_dev()