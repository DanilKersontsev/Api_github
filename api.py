import requests
import pygal
from pygal.style import Style

python_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
js_url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
pyth_response = requests.get(python_url)
js_response = requests.get(js_url)

print("Python status code:", pyth_response.status_code)
print("JavaScript status code:", js_response.status_code)


python_response_dict = pyth_response.json()
js_response_dict = js_response.json()

py_repo_dicts = python_response_dict['items']
js_repo_dicts = js_response_dict['items']


python_stars = []
js_stars = []

i = 0
x = 0

for repo_dict in py_repo_dicts:
    python_stars.append(py_repo_dicts[x]['stargazers_count'])
    x += 1

for repo_dict in js_repo_dicts:
    js_stars.append(js_repo_dicts[i]['stargazers_count'])
    i += 1

custom_style = Style(
    colors = ('#F44708', '#5D3E33')
)

chart = pygal.Bar(style=custom_style, x_label_rotation=10, show_legend=True)
chart.title = "Most-Starred Python And JavaScript Projects on Github"
chart.add('JavaScript', js_stars)
chart.add('Python', python_stars)
chart.render_in_browser()