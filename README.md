# Weather-Aware RF/FSO Link Attenuation Prediction

## Project Overview

This project predicts signal attenuation in hybrid Free-Space Optical (FSO) and Radio Frequency (RF) communication links using weather and channel measurements. It was developed as a University of Adelaide Master of Data Science portfolio project and focuses on applying supervised machine learning to a real-world telecommunications reliability problem.

The analysis compares Random Forest regression models across generic, weather-specific, feature-selected, and cascade modelling workflows. The main prediction targets are:

- `FSO_Att`: Free-Space Optical link attenuation
- `RFL_Att`: Radio Frequency link attenuation

The project investigates how environmental variables such as humidity, rain intensity, visibility, temperature, wind, and weather condition labels affect attenuation prediction performance.

## Folder Structure

```text
.
|-- README.md
|-- requirements.txt
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
|-- archive/
|   |-- experimental_joint_model_text5_3.ipynb
|   |-- scratch_import_pandas.py
```

The notebooks contain the main experimental workflow. The `src/` directory contains reusable helper modules for loading data, cleaning data, splitting features and targets, selecting features, training Random Forest models, tuning hyperparameters, and evaluating predictions. The `archive/` directory contains exploratory or superseded work kept for reference.

## Requirements

The project uses Python and common data science libraries:

- pandas
- numpy
- scikit-learn
- scipy
- matplotlib
- seaborn
- jupyter

Install them with:

```bash
pip install -r requirements.txt
```

For cleaner environment management, create and activate a virtual environment before installing dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Dataset

The raw dataset is not committed to the repository. The notebooks expect a CSV file named:

```text
RFLFSODataFull.csv
```

Place this file in the repository root before running the notebooks.

The modelling workflow expects columns such as:

```text
FSO_Att, RFL_Att, AbsoluteHumidity, Distance, Frequency, Particulate,
RainIntensity, RelativeHumidity, SYNOPCode, Temperature, Time,
Visibility, WindDirection, WindSpeed
```

`SYNOPCode` is used for weather-specific modelling, including clear weather, dust storm, fog, drizzle, rain, snow, and showers.

## How to Run

1. Clone or download the repository.
2. Place `RFLFSODataFull.csv` in the project root.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Start Jupyter from the repository root:

```bash
jupyter notebook
```

5. Run the notebooks in order:

```text
notebooks/01_data_exploration_and_generic_model.ipynb
notebooks/02_feature_selection_and_weather_models.ipynb
notebooks/03_revised_generic_rf_model.ipynb
notebooks/04_cascade_rf_fso_model.ipynb
```

The repository does not currently provide a single command-line training pipeline. The Python files in `src/` are reusable modules that support the notebook-based workflow.

## Modelling Workflow

The project follows this workflow:

1. Load and clean the RF/FSO weather-channel dataset.
2. Explore attenuation patterns and weather-condition groupings.
3. Train baseline Random Forest regression models for RF and FSO attenuation.
4. Rank predictors using Random Forest feature importance.
5. Compare generic models with weather-specific models grouped by `SYNOPCode`.
6. Tune Random Forest hyperparameters using grid search and randomized search.
7. Evaluate cascade experiments where one link prediction is used as an input feature for the other link.
8. Report model quality using RMSE, R-squared, Pearson correlation, and mutual information where applicable.

## Results

The committed results file, `results/model_performance_report.csv`, reports weather-specific Random Forest performance for selected weather groups:

| Condition | Training RMSE | Training R2 | Test RMSE | Test R2 | Best Parameters |
| --- | ---: | ---: | ---: | ---: | --- |
| Code 0 - Clear | 0.3317 | 0.9928 | 0.8714 | 0.9366 | 200 trees, max depth None, min samples split 2 |
| Code 3 - Dust Storm | 1.3694 | 0.9758 | 0.8446 | 0.9527 | 200 trees, max depth None, min samples split 2 |
| Code 4 - Fog | 0.8103 | 0.9496 | 0.8809 | 0.9576 | 200 trees, max depth None, min samples split 2 |
| Code 5 - Drizzle | 1.4367 | 0.9385 | 0.8066 | 0.9556 | 200 trees, max depth None, min samples split 2 |

These results show strong predictive performance for the evaluated weather categories, with test R2 values above 0.93 in the saved report. The notebooks contain additional experiments for generic, weather-specific, feature-selection, and RF/FSO cascade modelling.

## Limitations

- The raw dataset is not included, so results cannot be reproduced without access to `RFLFSODataFull.csv`.
- The project currently uses notebook-driven execution rather than a fully automated experiment pipeline.
- The dependency file does not pin package versions, so results may vary slightly across Python environments.
- Some weather categories may have relatively small sample sizes, which can make performance estimates less stable.
- Random train/test splitting may overstate performance for time-dependent data. A chronological split or time-series validation strategy would provide a stricter assessment.
- Cascade modelling can produce optimistic results if second-stage models are trained on predictions generated from models that have already seen the same rows. Out-of-fold stacking would be a stronger validation design.

## Reproducibility

To improve reproducibility:

- Run notebooks from the repository root so relative paths resolve consistently.
- Use the same dataset file name: `RFLFSODataFull.csv`.
- Keep notebook execution order consistent, starting with exploration and ending with cascade modelling.
- Preserve fixed `random_state` values used in the helper modules and notebooks.
- Record Python and package versions when rerunning experiments.
- Save updated evaluation outputs under `results/` rather than overwriting notebook-only outputs.

## Portfolio Summary

This project demonstrates an end-to-end applied data science workflow: domain framing, exploratory data analysis, supervised regression, feature selection, hyperparameter tuning, weather-specific model comparison, cascade modelling, and quantitative evaluation. It is suitable as a portfolio example for machine learning applied to telecommunications, environmental sensing, and reliability prediction.
