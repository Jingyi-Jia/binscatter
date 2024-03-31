If you're looking to make a nice binned scatter plot with a regression line and you
don't need to account for any control variables use
[seaborn.regplot](https://seaborn.pydata.org/generated/seaborn.regplot.html)! If you're
looking for a Python analog to Stata's![Screenshot 2024-03-31 074532](https://github.com/Jingyi-Jia/binscatter/assets/57499338/ec038a01-5762-41a9-b1c8-995753501996)

[binscatter](https://michaelstepner.com/binscatter/), read on.

Stata's `binscatter` is described fully by Michael Stepner
[here](https://michaelstepner.com/binscatter/). You can use this Python version in
essentially the same way you use Matplotlib functions like `plot` and `scatter`.
A more extensive description is [here](http://esantorella.com/2017/11/03/binscatter/).

## Getting started
1. Download the code through git clone or downloading the zip file. For example:
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
Example output:
![Screenshot 2024-03-31 074532](https://github.com/Jingyi-Jia/binscatter/assets/57499338/64897f49-7baa-4016-8930-71433b242d8c)
