import ipywidgets as iwidgets
from IPython.display import display

w_activation = iwidgets.Dropdown(
    options=['softmax', 'tanh', 'relu'],
    value='tanh',
    description='Activation:',
    disabled=False
)

w_n_layers = iwidgets.IntSlider(
    value=2,
    min=0,
    max=50,
    step=1,
    description='N Layers:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

w_n_nodes = iwidgets.IntSlider(
    value=4,
    min=0,
    max=200,
    step=1,
    description='N Nodes:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

w_n_epochs = iwidgets.IntSlider(
    value=100,
    min=0,
    max=1000,
    step=1,
    description='N Epochs:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

w_cutoff = iwidgets.FloatSlider(
    value=0.2,
    min=0,
    max=1.0,
    step=0.05,
    description='Dropout:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.2f',
)

items = [w_activation, w_n_layers, w_n_nodes, w_cutoff, w_n_epochs]
vbox = iwidgets.VBox(items)
button_circ = iwidgets.Button(description="Classify Circles")
button_fashion = iwidgets.Button(description="Classify Fashion")
