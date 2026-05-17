# Weather-Aware RF/FSO Link Attenuation Prediction

This project models signal attenuation in hybrid Free-Space Optical (FSO) and Radio Frequency (RF) communication links under different weather conditions. It uses measured weather and channel data to predict `FSO_Att` and `RFL_Att`, then compares generic, weather-specific, and cascade modelling strategies.

The work was developed as part of a University of Adelaide Master of Data Science project.

## Project Highlights

- Built Random Forest regression models for RF and FSO attenuation prediction.
- Compared generic models with weather-specific models grouped by `SYNOPCode`.
- Developed RF-to-FSO and FSO-to-RF cascade experiments, where one channel prediction is used as an additional feature for the other channel.
- Evaluated model performance with RMSE, R-squared, Pearson correlation, and mutual information.
- Visualised prediction behaviour with feature-importance plots and measured-vs-predicted 2D density heatmaps.
- Analysed model behaviour across 7 weather categories, including low-sample extreme-weather conditions such as duststorm, fog, and snow.

## Repository Structure

```text
.
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- notebooks/
|   |-- 01_data_exploration_and_generic_model.ipynb
|   |-- 02_feature_selection_and_weather_models.ipynb
|   |-- 03_revised_generic_rf_model.ipynb
|   |-- 04_cascade_rf_fso_model.ipynb
|-- src/
|   |-- data_preprocessing.py
|   |-- feature_selection.py
|   |-- train_model.py
|   |-- evaluate.py
|-- results/
|   |-- model_performance_report.csv
|   |-- figures/
|-- archive/
|   |-- experimental_joint_model_text5_3.ipynb
|   |-- scratch_import_pandas.py
```

## Dataset

The notebooks and scripts expect a CSV file named:

```text
RFLFSODataFull.csv
```

Place it in the project root before running the notebooks or scripts.

The local dataset used during development contains:

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

Weather groups used in the experiments:

| SYNOPCode | Weather condition | Samples |
| --- | --- | ---: |
| 0 | Clear Weather | 56,964 |
| 3 | Duststorm | 191 |
| 4 | Fog | 466 |
| 5 | Drizzle | 6,605 |
| 6 | Rain | 25,018 |
| 7 | Snow | 419 |
| 8 | Showers | 1,716 |

Because several extreme-weather groups have limited samples, their results should be interpreted as scenario-specific experimental evidence rather than broad production-grade robustness claims.

## Methods

The modelling workflow includes:

1. Data loading, duplicate checks, and feature preparation.
2. Generic Random Forest regression for `RFL_Att` and `FSO_Att`.
3. Feature selection based on Random Forest feature importance.
4. Hyperparameter tuning with `GridSearchCV` and `RandomizedSearchCV`.
5. Weather-specific training and evaluation by `SYNOPCode`.
6. Cascade modelling:
   - RF -> FSO: predicted RF attenuation is used as an additional FSO feature.
   - FSO -> RF: predicted FSO attenuation is used as an additional RF feature.
7. Evaluation using RMSE, R-squared, Pearson correlation, mutual information, and 2D heatmap visualisation.

## Results Summary

The final cascade notebook reports the following weather-specific test performance for the RF -> FSO experiment:

| Weather | RF RMSE | RF R2 | FSO RMSE | FSO R2 |
| --- | ---: | ---: | ---: | ---: |
| Clear Weather | 0.693 | 0.927 | 1.240 | 0.879 |
| Duststorm | 0.483 | 0.978 | 2.265 | 0.941 |
| Fog | 0.666 | 0.844 | 0.794 | 0.959 |
| Drizzle | 0.823 | 0.921 | 1.046 | 0.914 |
| Rain | 1.024 | 0.934 | 1.222 | 0.918 |
| Snow | 0.603 | 0.804 | 1.023 | 0.961 |
| Showers | 1.054 | 0.870 | 1.423 | 0.863 |

The reverse FSO -> RF cascade experiment reports RF R2 values between approximately 0.877 and 0.978 for most weather groups, with stronger performance on Duststorm and Rain subsets in the recorded experiments.

## Technical Notes

- Most notebooks currently use random train/test splitting with a fixed `random_state`.
- For a stricter time-dependent evaluation, a future improvement would be to split the 18-month dataset chronologically or use a time-series validation strategy.
- For cascade/stacking-style experiments, an out-of-fold prediction setup would reduce the risk of overly optimistic second-stage model evaluation.
- The raw dataset is excluded from version control because of file size and data-sharing constraints.

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

1. Place `RFLFSODataFull.csv` in the repository root.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Start Jupyter from the project root so the notebooks can find `RFLFSODataFull.csv`:

```bash
jupyter notebook
```

4. Run the notebooks in this order:

```text
notebooks/01_data_exploration_and_generic_model.ipynb
notebooks/02_feature_selection_and_weather_models.ipynb
notebooks/03_revised_generic_rf_model.ipynb
notebooks/04_cascade_rf_fso_model.ipynb
```

The `src/` directory contains reusable helper modules for preprocessing, feature selection, training, and evaluation. These modules can be used to turn the notebook workflow into a script-based experiment pipeline.

## Resume-Friendly Summary

Built a weather-aware RF/FSO link attenuation prediction system using measured weather-channel data. Implemented Random Forest regression, feature selection, weather-specific modelling, hyperparameter tuning, cascade RF/FSO prediction, and evaluation with RMSE, R-squared, Pearson correlation, mutual information, and 2D density heatmaps.
