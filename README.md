# RF and FSO Attenuation Prediction

This repository contains the modelling work for an RF/FSO communication-link attenuation prediction project. The notebooks use weather, link-distance, frequency, visibility, humidity, particulate, rain and wind measurements to predict radio-frequency link attenuation (`RFL_Att`) and free-space optical link attenuation (`FSO_Att`).

The project explores feature selection, random-forest regression, weather-specific modelling and cascade models that use one predicted channel as supporting information for the other channel.

## Repository Contents

| File | Description |
| --- | --- |
| `code.ipynb` | Initial data exploration, preprocessing, random-forest feature selection, general model evaluation and SYNOP weather-category modelling. |
| `code2.ipynb` | Extended feature-selection experiments and random-forest model evaluation. |
| `code3.ipynb` | Final cascade modelling notebook, including RF to FSO and FSO to RF experiments, Pearson correlation, mutual information and heatmap visualisations. |
| `generic model revised edition.ipynb` | Revised generic RF model notebook with global and per-weather performance summaries. |

## Dataset

The notebooks expect a CSV file named:

```text
RFLFSODataFull.csv
```

Place the CSV file in the repository root before running the notebooks.

The dataset used for this project has:

- 91,379 rows
- 27 columns
- Two target variables: `FSO_Att` and `RFL_Att`
- Weather-category labels in `SYNOPCode`

Main columns include:

```text
FSO_Att, RFL_Att, AbsoluteHumidity, Distance, Frequency, Particulate,
RainIntensity, RelativeHumidity, SYNOPCode, Temperature, Time,
Visibility, WindDirection, WindSpeed
```

SYNOP weather classes used in the notebooks:

| SYNOPCode | Weather condition | Samples |
| --- | --- | ---: |
| 0 | Clear Weather | 56,964 |
| 3 | Duststorm | 191 |
| 4 | Fog | 466 |
| 5 | Drizzle | 6,605 |
| 6 | Rain | 25,018 |
| 7 | Snow | 419 |
| 8 | Showers | 1,716 |

## Methods

The project uses random-forest regression to model RF and FSO attenuation. The workflow includes:

- Loading and checking the RF/FSO dataset
- Removing duplicate records
- Splitting features and targets for `FSO_Att` and `RFL_Att`
- Selecting important features using random-forest feature importance
- Tuning random-forest hyperparameters with `GridSearchCV` and `RandomizedSearchCV`
- Training general models and weather-specific models grouped by `SYNOPCode`
- Evaluating models with RMSE and R-squared
- Comparing real and predicted RF/FSO relationships using Pearson correlation and mutual information
- Plotting feature-selection traces, bar charts and measured-vs-predicted heatmaps

## Key Features Used

The final cascade notebook uses these universal RF features:

```python
[
    "RainIntensity",
    "RainIntensityMax",
    "RainIntensityMin",
    "Frequency",
    "TemperatureMax",
    "Temperature",
    "Distance",
    "Visibility",
]
```

The universal FSO selected features are:

```python
[
    "Distance",
    "Temperature",
    "Visibility",
    "TemperatureMin",
    "VisibilityMin",
    "ParticulateMax",
    "TemperatureMax",
    "WindSpeedMax",
]
```

## Results Summary

In the final RF to FSO cascade experiment, the notebook reports the following weather-specific test performance:

| Weather | RF RMSE | RF R2 | FSO RMSE | FSO R2 |
| --- | ---: | ---: | ---: | ---: |
| Clear Weather | 0.693 | 0.927 | 1.240 | 0.879 |
| Duststorm | 0.483 | 0.978 | 2.265 | 0.941 |
| Fog | 0.666 | 0.844 | 0.794 | 0.959 |
| Drizzle | 0.823 | 0.921 | 1.046 | 0.914 |
| Rain | 1.024 | 0.934 | 1.222 | 0.918 |
| Snow | 0.603 | 0.804 | 1.023 | 0.961 |
| Showers | 1.054 | 0.870 | 1.423 | 0.863 |

The reverse FSO to RF cascade experiment reports RF R2 values between approximately 0.877 and 0.978 for most weather groups, with the strongest performance on Duststorm and Rain subsets.

## Requirements

The notebooks were developed with Python 3 and common data-science libraries:

```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/fashaolea/a1904280-UNIADL-PROJ-MDS.git
cd a1904280-UNIADL-PROJ-MDS
```

2. Copy `RFLFSODataFull.csv` into the repository root.

3. Install the required packages:

```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
```

4. Start Jupyter Notebook:

```bash
jupyter notebook
```

5. Open and run the notebooks. A recommended order is:

```text
generic model revised edition.ipynb
code.ipynb
code2.ipynb
code3.ipynb
```

## Project Notes

- `RFLFSODataFull.csv` is not included in this repository because it is a large dataset file.
- Several notebook outputs contain saved plots and experiment logs.
- Some comments or outputs may appear with encoding issues if the notebook is opened in a non-UTF-8 environment.
- Random-forest results may vary slightly depending on package versions and runtime environment.

## Author

This project was developed for the University of Adelaide MDS project coursework.
