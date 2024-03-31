import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def _get_bins(n_elements, n_bins):
    bin_edges = np.linspace(0, n_elements, n_bins + 1).astype(int)
    return [slice(bin_edges[i], bin_edges[i + 1]) for i in range(n_bins)]

def get_binscatter_objects(y, x, controls, n_bins, recenter_x, recenter_y, bins, fixed_effects):
    if fixed_effects is not None:
        fe_dummies = pd.get_dummies(fixed_effects, drop_first=True)
        controls = np.hstack([controls, fe_dummies]) if controls is not None else fe_dummies

    if controls is None:
        argsort = np.argsort(x)
        x_data, y_data = x[argsort], y[argsort]
    else:
        if controls.ndim == 1:
            controls = np.asarray(controls)[:, None]

        reg_y = LinearRegression().fit(controls, y)
        reg_x = LinearRegression().fit(controls, x)
        y_data, x_data = y - reg_y.predict(controls), x - reg_x.predict(controls)
        argsort = np.argsort(x_data)
        x_data, y_data = x_data[argsort], y_data[argsort]

        if recenter_y:
            y_data += np.mean(y)
        if recenter_x:
            x_data += np.mean(x)

    reg = LinearRegression().fit(x_data[:, None], y_data)
    if bins is None:
        bins = _get_bins(len(y_data), n_bins)

    x_means = [np.mean(x_data[bin_]) for bin_ in bins]
    y_means = [np.mean(y_data[bin_]) for bin_ in bins]

    return x_means, y_means, reg.intercept_, reg.coef_[0]

def create_binscatter(x, y, controls=None, n_bins=20, line_kwargs=None, scatter_kwargs=None,
               recenter_x=False, recenter_y=True, bins=None, fit_reg=True, fixed_effects=None, ax=None):
    """
    Binned scatter plot with optional control variables and fixed effects.

    Parameters:
    - x: Independent variable.
    - y: Dependent variable.
    - controls: Additional control variables to partial out from x and y.
    - n_bins: Number of bins for the scatter plot.
    - line_kwargs: Keyword arguments for the regression line plot.
    - scatter_kwargs: Keyword arguments for the scatter plot.
    - recenter_x: Recenter the residualized x data to its original mean.
    - recenter_y: Recenter the residualized y data to its original mean.
    - bins: Custom bins for the scatter plot.
    - fit_reg: Plot a regression line if True.
    - fixed_effects: Categorical variable for fixed effects.
    """
    if line_kwargs is None:
        line_kwargs = {}
    if scatter_kwargs is None:
        scatter_kwargs = {}

    # Create a new figure and axes if not provided
    if ax is None:
        fig, ax = plt.subplots()

    x_means, y_means, intercept, coef = get_binscatter_objects(
        np.asarray(y), np.asarray(x), controls, n_bins, recenter_x, recenter_y, bins, fixed_effects
    )

    ax.scatter(x_means, y_means, **scatter_kwargs)
    if fit_reg:
        x_range = np.array(ax.get_xlim())
        ax.plot(x_range, intercept + x_range * coef, **line_kwargs)
        # Add beta coefficient to the plot
        ax.text(0.05, 0.95, f'Beta: {coef:.3f}', transform=ax.transAxes, ha='left', va='top', fontsize=12,
                bbox=dict(boxstyle="round", alpha=0.5, color='lightgray'))

    if hasattr(x, 'name'):
        ax.set_xlabel(x.name)
    if hasattr(y, 'name'):
        ax.set_ylabel(y.name)

    # Show the plot if it was created within this function
    if ax is None:
        plt.show()

    return x_means, y_means, intercept, coef
