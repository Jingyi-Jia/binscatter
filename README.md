If you're looking to make a nice binned scatter plot with a regression line and you
don't need to account for any control variables use
[seaborn.regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html)! If you're
looking for a Python analog to Stata's
[binscatter](https://michaelstepner.com/binscatter/), read on.

Stata's `binscatter` is described fully by Michael Stepner
[here](https://michaelstepner.com/binscatter/). You can use this Python version in
essentially the same way you use Matplotlib functions like `plot` and `scatter`.
A more extensive description is [here](http://esantorella.com/2017/11/03/binscatter/).

## Getting started
1. Download the code through git clone or downloading the zip file. Example:
```
git clone git@github.com:Jingyi-Jia/binscatter.git
```
2. Set up the module
```
cd binscatter
pip install -r requirements.txt
pip install .
```
## Usage

```
import pandas as pd
import numpy as np
df = pd.read_csv('extensive_fake_data.csv')

from binscatter.binscatter import create_binscatter
# Binscatter plot
create_binscatter(df['x'], df['y']);

# Binscatter plot with fixed effects
create_binscatter(df['x'], df['y'], fixed_effects=df['ind']);
```
