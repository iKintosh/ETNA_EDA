from etna.datasets import TSDataset
import pandas as pd


def compare_commulative_metric(real, predicted, metric):
    """Calculates matrics on summarization of all segments."""
    min_date_time = str(predicted.index.min().date())
    real_df = TSDataset.to_flatten(real[min_date_time:, ...])
    real_df = real_df.groupby("timestamp").sum()
    real_df["segment"] = "SUMMARIZATION_OF_ALL_SEGMENTS_METRIC_" + metric.name
    real_df = real_df.reset_index()

    idx = pd.IndexSlice

    predicted_df = predicted.loc[idx[:], idx[:, "target"]]
    predicted_df = TSDataset.to_flatten(predicted_df)
    predicted_df = predicted_df.groupby("timestamp").sum()
    predicted_df["segment"] = "SUMMARIZATION_OF_ALL_SEGMENTS_METRIC_" + metric.name
    predicted_df = predicted_df.reset_index()

    return metric(
        TSDataset(TSDataset.to_dataset(real_df), freq="30T"),
        TSDataset(TSDataset.to_dataset(predicted_df), freq="30T"),
    )
