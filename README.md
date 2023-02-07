# Ride Sharing App EDA
This project focuses on analyzing ride sharing app data to predict locations of high value.

## Results
Findings of this EDA could be found in [eda_notebook](https://github.com/iKintosh/ETNA_EDA/blob/master/notebook/eda_notebook.ipynb). And as nbviewer notebook.
  
<a href="https://nbviewer.org/github/iKintosh/ETNA_EDA/blob/master/notebook/eda_notebook.ipynb" 
   target="_parent">
   <img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png" 
      width="109" height="20">
</a>

## How to install

If you want to play with the data or the report you may install and set up the environment.

1. Clone the repository.
2. In the terminal run:
    ```bash
    poetry install
    ```
3. Done

I recommend using [pyenv](https://github.com/pyenv/pyenv) to set up correct Python version.

### Requirements
- Python >=3.8.1,<3.10.0
- Poetry
- Other requirements listed in pyproject.toml file

## Data Description
The data used in this project is in the form of a .csv file and contains the following columns:
- start_time: the time when the order was made
- start_lat: latitude of the location where the order was made
- start_lng: longitude of the location where the order was made
- end_lat: latitude of the destination point
- end_lng: longitude of the destination point
- ride_value: how much monetary value is in this particular ride

## EDA Purpose
The availability of supply for ride sharing services depends on the duration of time it takes for the drivers to reach the customers. We want to attract drivers towards areas of the highest ride value. The purpose of this EDA is to determine if it is possible to predict areas of high ride value using only the data available.

## Methodology
The data is aggregated into clusters to allow prediction of demand based on location. [ETNA library](https://github.com/tinkoff-ai/etna) is used to conduct the forecasting tasks in this work.

Two different approaches for clustering and forecasting is used. The most promissing one is using:
- uber h3 for clusterization.
- catboost model for forecasting.

## Further Work
- Rearrange the regions manually
- Collect more data on small regions
- Try an ensemble of models
- Use `end_lat`, `end_lng` columns