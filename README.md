# RF and FSO Attenuation Prediction

This project is about predicting RF and FSO link attenuation using weather and link-related data. I used the `RFLFSODataFull.csv` dataset and tried different random forest models to see how well `RFL_Att` and `FSO_Att` can be predicted under different weather conditions.

The work started from basic data exploration, then moved into feature selection, general models, weather-specific models, and finally cascade models where I tested whether RF and FSO predictions could help each other.

## Files

| File | What it is for |
| --- | --- |
| `code.ipynb` | My first main notebook. It includes data checking, preprocessing, feature selection, random forest modelling, and early weather-based experiments. |
| `code2.ipynb` | A follow-up notebook where I continued testing the feature-selection process and model performance. |
| `generic model revised edition.ipynb` | A cleaner version of the general modelling workflow. I organised the code into reusable functions and added per-weather evaluation. |
| `code3.ipynb` | The final modelling notebook. It includes the RF to FSO and FSO to RF cascade experiments, plus correlation, mutual information, and heatmap analysis. |

## Dataset

The dataset file should be placed in the root folder of the project with this name:

```text
RFLFSODataFull.csv
```

I did not include the CSV file in the repository because it is a large dataset file.

The dataset I used has:

- 91,379 rows
- 27 columns
- two target columns: `FSO_Att` and `RFL_Att`
- weather labels stored in `SYNOPCode`

Some of the main columns are:

```text
FSO_Att, RFL_Att, AbsoluteHumidity, Distance, Frequency, Particulate,
RainIntensity, RelativeHumidity, SYNOPCode, Temperature, Time,
Visibility, WindDirection, WindSpeed
```

The `SYNOPCode` values are used to separate the data into weather conditions:

| SYNOPCode | Weather condition | Samples |
| --- | --- | ---: |
| 0 | Clear Weather | 56,964 |
| 3 | Duststorm | 191 |
| 4 | Fog | 466 |
| 5 | Drizzle | 6,605 |
| 6 | Rain | 25,018 |
| 7 | Snow | 419 |
| 8 | Showers | 1,716 |

This imbalance was one of the reasons I checked model performance separately for each weather type.

## What I Tried

The main model I used was `RandomForestRegressor`. I chose it because it works well with tabular data and can also give feature importance, which was useful for deciding which variables to keep.

The general workflow was:

- load the RF/FSO dataset
- check data shape, data types, duplicates, and missing values
- separate the targets `FSO_Att` and `RFL_Att`
- use random forest feature importance to remove less useful features
- tune model parameters with `GridSearchCV` or `RandomizedSearchCV`
- compare results using RMSE and R2
- evaluate models under different `SYNOPCode` weather groups
- test cascade models to see whether RF and FSO predictions are related

## Feature Selection

A big part of the project was deciding which features were actually useful. At first I used many columns, but that made the model harder to explain. Later I used a step-by-step feature removal process and watched whether RMSE or R2 became worse.

For FSO attenuation, the final useful features in the revised general model were:

```text
Distance, Temperature, Visibility
```

For RF attenuation, the revised general model kept:

```text
AbsoluteHumidity, RainIntensity
```

In the final cascade notebook, I used a slightly larger selected feature set because the goal was to compare RF/FSO relationships under each weather condition.

## Final Cascade Experiments

In `code3.ipynb`, I tested two directions:

- RF to FSO: predict RF attenuation first, then model FSO attenuation
- FSO to RF: predict FSO attenuation first, then model RF attenuation

I added this part because RF and FSO links are both affected by weather, but not always in the same way. I wanted to check whether one channel could provide useful information for the other.

I also used Pearson correlation, mutual information, and heatmaps because RMSE and R2 only show prediction error. The extra analysis helped me compare whether the predicted RF/FSO relationship looked similar to the measured relationship.

## Results

In the final RF to FSO cascade experiment, the results were:

| Weather | RF RMSE | RF R2 | FSO RMSE | FSO R2 |
| --- | ---: | ---: | ---: | ---: |
| Clear Weather | 0.693 | 0.927 | 1.240 | 0.879 |
| Duststorm | 0.483 | 0.978 | 2.265 | 0.941 |
| Fog | 0.666 | 0.844 | 0.794 | 0.959 |
| Drizzle | 0.823 | 0.921 | 1.046 | 0.914 |
| Rain | 1.024 | 0.934 | 1.222 | 0.918 |
| Snow | 0.603 | 0.804 | 1.023 | 0.961 |
| Showers | 1.054 | 0.870 | 1.423 | 0.863 |

Overall, the models performed reasonably well, but the results were not equally strong for every weather condition. Smaller weather groups such as Duststorm, Fog, and Snow were harder to rely on because they had much fewer samples.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/fashaolea/a1904280-UNIADL-PROJ-MDS.git
cd a1904280-UNIADL-PROJ-MDS
```

2. Put `RFLFSODataFull.csv` into the project folder.

3. Install the main packages:

```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
```

4. Start Jupyter Notebook:

```bash
jupyter notebook
```

5. Open the notebooks. The rough order of the project is:

```text
code.ipynb
code2.ipynb
generic model revised edition.ipynb
code3.ipynb
```

## Notes

- The notebooks show the project process from early experiments to the final version.
- Some notebook outputs may look messy if the encoding is different, especially for older comments or printed text.
- Results may change slightly depending on package versions and random forest settings.
- This was developed as part of my University of Adelaide MDS project coursework.
