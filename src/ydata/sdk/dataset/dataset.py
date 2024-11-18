import numpy as np
from numpy import int64
from pandas import DataFrame as pdDataFrame
from pandas import read_csv, to_datetime

from ydata.sdk.utils.cache import cache_file


def get_timeseries() -> pdDataFrame:
    def generate_multivariate_multientity_timeseries(num_rows=1000, num_entities=5, num_timesteps=10):
        """Generates a multivariate, multi-entity time series dataset.

        Args:
            num_rows: The number of rows in the dataset. Defaults to 1000.
            num_entities: The number of entities in the dataset. Defaults to 5.
            num_timesteps: The number of time steps for each entity. Defaults to 10.

        Returns:
            A pandas DataFrame representing the time-series dataset.
        """

        data = []
        for entity in range(num_entities):
            for t in range(num_timesteps):
                row = {
                    'entity_id': entity,
                    'time': t
                }
                for feature in range(3):
                    # Simulate some random data
                    row[f'feature_{feature}'] = np.random.rand()
                data.append(row)

        # Adding more rows to meet the desired number of rows
        additional_rows = max(0, num_rows - len(data))
        for _ in range(additional_rows):
            entity = np.random.randint(0, num_entities)
            t = np.random.randint(0, num_timesteps)
            row = {
                'entity_id': entity,
                'time': t
            }
            for feature in range(3):
                row[f'feature_{feature}'] = np.random.rand()
            data.append(row)
        df = pdDataFrame(data)

        return df

    return generate_multivariate_multientity_timeseries()


def get_census() -> pdDataFrame:
    file_name = cache_file(
        "census_train.csv",
        "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
    )

    df = read_csv(
        file_name,
        header=None,
        index_col=False,
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
        ],
        skipinitialspace=True
    )

    # Prepare missing values
    df = df.replace("\\?", None, regex=True)

    return df


def get_titanic() -> pdDataFrame:
    file_name = cache_file(
        "titanic.csv",
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    )

    return read_csv(file_name)


def get_airquality() -> pdDataFrame:
    file_name = cache_file(
        "pollution_us_2000_2016.csv",
        "https://query.data.world/s/mz5ot3l4zrgvldncfgxu34nda45kvb",
    )

    return read_csv(file_name, index_col=[0])


def get_occupancy() -> pdDataFrame:
    file_name = cache_file(
        "occupancy.csv",
        "https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master/Occupancy%20Detection/datatraining.csv",
    )

    df = read_csv(file_name)
    df["date"] = to_datetime(
        df["date"], format="%m/%d/%Y %H:%M").values.astype(int64) // 10 ** 9
    return df


def get_dataset(name: str):
    DATASETS = {
        'census': get_census,
        'titanic': get_titanic,
        'airquality': get_airquality,
        'timeseries': get_timeseries
    }

    if name not in DATASETS:
        raise FileNotFoundError(
            f"Dataset {name} does not exist. Valid datasets are: {', '.join(DATASETS.keys())}.")

    return DATASETS[name]()
