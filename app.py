import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY], suppress_callback_exceptions=True, meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])
img = app.get_asset_url("43437160.jpeg")
linkedin = app.get_asset_url("linkedin-3000959_960_720.png")
github = app.get_asset_url("GitHub-Mark.png")
upwork = app.get_asset_url("upwork.png")
server = app.server

# layout
map_bonn = html.Iframe(srcDoc=open(r"./assets/bonn.html", 'r').read(),
                       style={"frameBorder": "0", "width": "100%", "height": "600px"})

card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("IT", className="card-title"),
            dbc.Row([dbc.Col([
                html.Br(),
                "Python:    proficient",
                html.Div(className="progress",
                         children=html.Div(className="progress-bar progress-bar-striped bg-success",
                                           role="progressbar", style={"width": "85%"})),
                html.Br(),
                "Java:  Good Command",
                html.Div(className="progress",
                         children=html.Div(className="progress-bar progress-bar-striped bg-info",
                                           role="progressbar", style={"width": "70%"})),
                html.Br(),
                "SQL:  Good Command",
                html.Div(className="progress",
                         children=html.Div(className="progress-bar progress-bar-striped bg-warning",
                                           role="progressbar", style={"width": "70%"}))
            ]),
                dbc.Col([
                    html.Br(),
                    "Deep Learning (Tensorflow, Pytorch): Good Command",
                    html.Div(className="progress",
                             children=html.Div(className="progress-bar progress-bar-striped bg-success",
                                               role="progressbar", style={"width": "80%"})),
                    html.Br(),
                    "Data Visualisation (Tableau, Dash):  proficient",
                    html.Div(className="progress",
                             children=html.Div(className="progress-bar progress-bar-striped bg-info",
                                               role="progressbar", style={"width": "70%"})),
                    html.Br(),
                    "AWS:  Basic",
                    html.Div(className="progress",
                             children=html.Div(className="progress-bar progress-bar-striped bg-warning",
                                               role="progressbar", style={"width": "30%"})),
                    html.Br(),
                    "Web Scrapping: Proficient",
                    html.Div(className="progress",
                             children=html.Div(className="progress-bar progress-bar-striped bg-danger",
                                               role="progressbar", style={"width": "90%"}))
                ])])
        ]
    ), className="h-100"

)

card_lan = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Language Skill", className="card-title"),
            "Mandarin", html.Br(),
            "Mother Language",
            html.Div(className="progress", children=html.Div(className="progress-bar progress-bar-striped bg-success",
                                                             role="progressbar", style={"width": "100%"})),
            html.Br(),
            "German", html.Br(),
            "Goethe-Zertifikat C2: Großes Deutsches Sprachdiplom",
            html.Div(className="progress", children=html.Div(className="progress-bar progress-bar-striped bg-info",
                                                             role="progressbar", style={"width": "90%"})),
            html.Br(),
            "English", html.Br(),
            "fluent",
            html.Div(className="progress", children=html.Div(className="progress-bar progress-bar-striped bg-warning",
                                                             role="progressbar", style={"width": "90%"})),

        ]
    ), className="h-100"

)

tabs = dbc.Container(fluid=True, children=
[
    dbc.Tabs(
        [
            dbc.Tab(label="Working Experience", tab_id="tab-1"),
            dbc.Tab(label="Education", tab_id="tab-2"),
            dbc.Tab(label="Extracurricular activities", tab_id="tab-3")
        ],
        id="tabs",
        active_tab="tab-1",
    ),
    html.Div(children=dbc.Container(html.Div([dcc.Slider(
    ), html.Br(),
        dbc.Card(
            children=[
                dbc.CardHeader(""),
                dbc.CardBody(
                    [
                        html.H5("", className="card-title"),
                        html.P(
                            "",
                            className="card-text",
                        ),
                    ]
                ),
            ], )])), id="content"),
]
                     )

row2 = dbc.Row([dbc.Col(card_lan, width=4),
                dbc.Col(card, width=8)],
               className="ml-2 mr-2 mt-2 mb-2 h-50")

badges = html.Span(
    [
        dbc.CardImg(src=github, style={"max-width": "2rem"}),
        dbc.Badge("GitHub", pill=True, color="secondary", className="mr-1", href="https://github.com/sitongye"),
        dbc.CardImg(src=linkedin, style={"max-width": "2rem"}),
        dbc.Badge("Linkedin", pill=True, color="info", className="mr-1", href="https://www.linkedin.com/in/sitong-ye/"),
        dbc.CardImg(src=upwork, style={"max-width": "1.5rem"}),
        dbc.Badge("Upwork", pill=True, color="success", className="mr-1",
                  href="https://www.upwork.com/o/profiles/users/~0107c536920b1fb3f1/")

    ], style={"Align": "right"}
)

jumbotron = dbc.Row(
    dbc.Col(
        dbc.Jumbotron(
            [
                dbc.Row(
                    [dbc.Col([
                        html.H3("Hello World!"),
                        html.H1("This is Sitong Ye", className="display-3"),
                        badges,
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                html.P(""),
                                html.P("53227, Bonn"),
                                html.P("+4915174211571"),
                                html.P("sitongye94@outlook.com")], width=3),
                            dbc.Col(html.Div(), width=4),
                            dbc.Col(className="text-muted", children=[
                                html.Br(),
                                html.P("const me=new DataScientist();"),
                                html.P("let RealWorldDataIsComplex=true;"),
                                html.P("let MachineLearningIsHard=true;"),
                                html.P("while (MachineLearningIsHard) {"),
                                html.P(style={"margin-left": "15px"}, children="me.upgrade();"),
                                html.P("}"),
                            ], width=3)
                        ]),
                    ], width=9),
                        dbc.Col(dbc.CardImg(src=img, style={"max-width": "20rem"}), width=3)])])
    ))

app.layout = dbc.Container([jumbotron,
                            dbc.Row([dbc.Col(dbc.Container(fluid=True,id="map_container",
                                                           children=html.Iframe(),
                                                           className="h-100"), width=4),
                                     dbc.Col(tabs, width=8)],
                                    className="ml-2 mr-2 mt-2 mb-2 h-50"), row2], fluid=True)

# card with header
card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

# card without header
card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Go somewhere", color="primary"),
        ]
    ), className="h-100"

)
df_work = pd.read_csv(r"./assets/work_experience_dt.csv")
df_education = pd.read_csv(r"./assets/education.csv")
df_extracurricular = pd.read_csv(r"./assets/extracurricular.csv")


@app.callback([Output("content", "children"), Output("map_container", "children")], [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return dbc.Container([html.Br(),
                              dbc.Row([
                                  dbc.Col(dbc.Badge("select on the timeline here", color="dark",
                                                    className="mr-1"), width=3),
                                  dbc.Col(
                                      dcc.Slider(id="work_slider",
                                                 min=1,
                                                 max=5,
                                                 marks={
                                                     1: "2021",
                                                     2: "2020",
                                                     3: "2019",
                                                     4: "2018",
                                                     5: "2017"
                                                 },
                                                 value=1,
                                                 step=None
                                                 ), width=9)]),
                              dbc.Card(id="work_card",
                                       children=[
                                           dbc.CardHeader(df_work.iloc[0, :]["time"]),
                                           dbc.CardBody(
                                               [
                                                   html.H4(df_work.iloc[0, :]["company"],
                                                           className="card-title"),
                                                   html.H5(df_work.iloc[0, :]["Role"], className="card-title"),
                                                   html.P(
                                                       df_work.iloc[0, :]["location"],
                                                       className="card-text",
                                                   ),
                                               ]
                                           ),
                                       ], color="info", outline=True), html.Br(),
                              dbc.Alert(id="alert",
                                        children=[html.Br()] * 2 + [html.Li([string], className="ul") for
                                                                    string in
                                                                    df_work.iloc[0, :]["Experience"].split(
                                                                        r"\n")], color="info",
                                        style={"height": "250px",
                                               "textIndent": "20px"}),
                              ]), html.Iframe(className="embed-responsive-item",id="work_map", srcDoc=open('./assets/bonn.html', 'r').read(),
                                              style={"frameBorder": "0", "width": "100%",
                                                     "height": "100%"
                                                    }),
    elif at == "tab-2":
        return dbc.Container(fluid=True, children=dbc.Container(fluid=True, children=[html.Br(),
                                                                                      dbc.Row([
                                                                                          dbc.Col(dbc.Badge(
                                                                                              "select on the timeline here",
                                                                                              color="dark",
                                                                                              className="mr-1"),
                                                                                              width=3),
                                                                                          dbc.Col(
                                                                                              dcc.Slider(
                                                                                                  id="edu_slider",
                                                                                                  min=1,
                                                                                                  max=4,
                                                                                                  marks={
                                                                                                      1: "09/2018-06/2020",
                                                                                                      2: "9/2013-07/2018",
                                                                                                      3: "09/2016-2/2017",
                                                                                                      4: "09/2010-07/2013",
                                                                                                  },
                                                                                                  value=1,
                                                                                                  step=None
                                                                                              ), width=9)]),
                                                                                      dbc.Card(id="edu_card",
                                                                                               children=[
                                                                                                   dbc.CardHeader(
                                                                                                       df_education.iloc[
                                                                                                       0, :]["time"]),
                                                                                                   dbc.CardBody(
                                                                                                       [
                                                                                                           html.H4(
                                                                                                               df_education.iloc[
                                                                                                               0, :][
                                                                                                                   "school"],
                                                                                                               className="card-title"),
                                                                                                           html.H5(
                                                                                                               df_education.iloc[
                                                                                                               0, :][
                                                                                                                   "Role"],
                                                                                                               className="card-title"),
                                                                                                           html.P(
                                                                                                               df_education.iloc[
                                                                                                               0, :][
                                                                                                                   "location"],
                                                                                                               className="card-text",
                                                                                                           ),
                                                                                                       ]
                                                                                                   ),
                                                                                               ], color="info",
                                                                                               outline=True), html.Br(),
                                                                                      dbc.Alert(id="alert_edu",
                                                                                                children=[
                                                                                                    html.Li([string],
                                                                                                            className="ul")
                                                                                                    for
                                                                                                    string in
                                                                                                    df_education.iloc[0,
                                                                                                    :][
                                                                                                        "Experience"].split(
                                                                                                        r"\n")],
                                                                                                color="info",
                                                                                                style={
                                                                                                    "height": "250px",
                                                                                                    "textIndent": "20px"}),
                                                                                      ])), html.Iframe(id="edu_map",
                                                                                                       srcDoc=open(
                                                                                                           './assets/frankfurt_school.html',
                                                                                                           'r').read(),
                                                                                                       style={
                                                                                                           "frameBorder": "0",
                                                                                                           "width": "100%",
                                                                                                           "height": "600px"}),
    elif at == "tab-3":
        return dbc.Container(fluid=True, children=dbc.Container(fluid=True, children=[html.Br(),
                                                                                      dbc.Row([
                                                                                          dbc.Col(dbc.Badge(
                                                                                              "select on the timeline here",
                                                                                              color="dark",
                                                                                              className="mr-1"),
                                                                                              width=3),
                                                                                          dbc.Col(
                                                                                              dcc.Slider(
                                                                                                  id="extra_slider",
                                                                                                  min=1,
                                                                                                  max=4,
                                                                                                  marks={
                                                                                                      1: "09/2019",
                                                                                                      2: "04/2019",
                                                                                                      3: "10/2018",
                                                                                                      4: "2015-2016",
                                                                                                  },
                                                                                                  value=1,
                                                                                                  step=None
                                                                                              ), width=9)]),
                                                                                      dbc.Card(id="extra_card",
                                                                                               children=[
                                                                                                   dbc.CardHeader(
                                                                                                       df_extracurricular.iloc[
                                                                                                       0, :]["time"]),
                                                                                                   dbc.CardBody(
                                                                                                       [
                                                                                                           html.H4(
                                                                                                               df_extracurricular.iloc[
                                                                                                               0, :][
                                                                                                                   "Insitut"],
                                                                                                               className="card-title"),
                                                                                                           html.H5(
                                                                                                               df_extracurricular.iloc[
                                                                                                               0, :][
                                                                                                                   "Role"],
                                                                                                               className="card-title"),
                                                                                                           html.P(
                                                                                                               df_extracurricular.iloc[
                                                                                                               0, :][
                                                                                                                   "location"],
                                                                                                               className="card-text",
                                                                                                           ),
                                                                                                       ]
                                                                                                   ),
                                                                                               ], color="info",
                                                                                               outline=True), html.Br(),
                                                                                      dbc.Alert(id="alert_extra",
                                                                                                children=[
                                                                                                    html.Li([string],
                                                                                                            className="ul")
                                                                                                    for
                                                                                                    string in
                                                                                                    df_extracurricular.iloc[
                                                                                                    0,
                                                                                                    :][
                                                                                                        "Experience"].split(
                                                                                                        r"\n")],
                                                                                                color="info",
                                                                                                style={
                                                                                                    "height": "250px",
                                                                                                    "textIndent": "20px"}),
                                                                                      ])), html.Iframe(id="extra_map",
                                                                                                       srcDoc=open(
                                                                                                           './assets/frankfurt_school.html',
                                                                                                           'r').read(),
                                                                                                       style={
                                                                                                           "frameBorder": "0",
                                                                                                           "width": "100%",
                                                                                                           "height": "100%"}),
    return html.P("This shouldn't ever be displayed...")


@app.callback([Output("work_card", "children"), Output("alert", "children"), Output("work_map", "srcDoc")],
              [Input("work_slider", "value")])
def change_card_content(value):
    html_key = df_work.iloc[value - 1, :]["location_key"]
    src = open('./assets/{}.html'.format(html_key), 'r').read()
    return [
               dbc.CardHeader(df_work.iloc[value - 1, :]["time"]),
               dbc.CardBody(
                   [
                       html.H4(df_work.iloc[value - 1, :]["company"], className="card-title"),
                       html.H5(df_work.iloc[value - 1, :]["Role"], className="card-title"),
                       html.P(
                           df_work.iloc[value - 1, :]["location"],
                           className="card-text",
                       ),
                   ]
               ),
           ], [html.Br()] * 2 + [html.Li([string], className="ul") for string in
                                 df_work.iloc[value - 1, :]["Experience"].split("\n")], src


@app.callback([Output("edu_card", "children"), Output("alert_edu", "children"), Output("edu_map", "srcDoc")],
              [Input("edu_slider", "value")])
def change_card_content(value):
    html_key = df_education.iloc[value - 1, :]["location_key"]
    src = open('./assets/{}.html'.format(html_key), 'r').read()
    return [
               dbc.CardHeader(df_education.iloc[value - 1, :]["time"]),
               dbc.CardBody(
                   [
                       html.H4(df_education.iloc[value - 1, :]["school"], className="card-title"),
                       html.H5(df_education.iloc[value - 1, :]["Role"], className="card-title"),
                       html.P(
                           df_education.iloc[value - 1, :]["location"],
                           className="card-text",
                       ),
                   ]
               ),
           ], [html.Li([string], className="ul") for string in
               df_education.iloc[value - 1, :]["Experience"].split(r"\n")], src


@app.callback([Output("extra_card", "children"), Output("alert_extra", "children"), Output("extra_map", "srcDoc")],
              [Input("extra_slider", "value")])
def change_card_content(value):
    html_key = df_extracurricular.iloc[value - 1, :]["location_key"]
    src = open('./assets/{}.html'.format(html_key), 'r').read()
    return [
               dbc.CardHeader(df_extracurricular.iloc[value - 1, :]["time"]),
               dbc.CardBody(
                   [
                       html.H4(df_extracurricular.iloc[value - 1, :]["Insitut"], className="card-title"),
                       html.H5(df_extracurricular.iloc[value - 1, :]["Role"], className="card-title"),
                       html.P(
                           df_extracurricular.iloc[value - 1, :]["location"],
                           className="card-text",
                       ),
                   ]
               ),
           ], [html.Br()] * 2 + [html.Li([string], className="ul") for string in
                                 df_extracurricular.iloc[value - 1, :]["Experience"].split(r"\n")], src


if __name__ == '__main__':
    app.run_server(debug=True)
