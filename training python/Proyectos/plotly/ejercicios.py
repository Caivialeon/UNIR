from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
from plotly.offline import iplot
import plotly.graph_objects as go
import numpy as np

valores = np.array([1,5,7,2,8])

data = [go.Scatter(y=valores)]


iplot(data)


