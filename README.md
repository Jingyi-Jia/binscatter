Based on Elizabeth Santorella's project: https://github.com/esantorella/binscatter?tab=readme-ov-file

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

Compare to STATA output:
![Graph](https://github.com/Jingyi-Jia/binscatter/assets/57499338/435ebc0a-ee24-4817-89e0-5c69a4f002a5)
![Screenshot 2024-03-31 072903](https://github.com/Jingyi-Jia/binscatter/assets/57499338/86cdd45a-9040-456e-89d1-6fe6870a7936)

