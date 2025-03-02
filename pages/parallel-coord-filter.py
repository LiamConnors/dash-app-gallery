import dash

from lib.code_and_show import example_app


dash.register_page(
    __name__,
    description="This app uses a parallel coordinates graph and the selected coordinates to filter a DataTable. It has a top-bottom layout and a regular-callback.",
)

filename = __name__.split("pages.")[1]

notes = """

#### Dash Components in App:
- [DataTable](https://dash.plotly.com/datatable)
- [Store](https://dash.plotly.com/dash-core-components/store)

#### Plotly Documentation:  
- [parallel coordinates](https://plotly.com/python/parallel-coordinates-plot/) 

#### Community Components:

Dash Bootstrap Components
- [Themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
- [Container](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)

#### Contributed by:
This example app was contributed by [Bryan](https://community.plotly.com/u/jinnyzor/summary)

"""

layout = example_app(filename, notes=notes)
