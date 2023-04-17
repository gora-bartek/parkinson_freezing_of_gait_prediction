from re import compile, match
from os import listdir
import pandas as pd
from random import sample


def split_data_paths(path: str, split_ratio: float) -> (list, list):
    """
    Get paths to csv and split them into train and test set
    
    params:
        paths (str): paths to csv
        split_ration (float): ratio of train-test split
    
    returns:
        train_set_paths (list): paths to training set
        test_set_paths (list): paths to test set
    """
    
    csv_regex = compile("\w+\.csv")
    csv_paths = listdir(path)
    csv_paths = [tmp_path for tmp_path in csv_paths if csv_regex.match(tmp_path)]
    paths_len = len(csv_paths)
    
    train_set_paths = sample(csv_paths, round(split_ratio * paths_len))
    test_set_paths = list(set(csv_paths) - set(train_set_paths))

    return train_set_paths, test_set_paths


def read_data(csv_names: list, path: str) -> pd.DataFrame:
    """
    For each patient read csv and combine it into one data frame
    
    params:
        paths (list): list of csv files
    
    return:
        results (pd.DataFrame): combined data frame of all patients in set
    """
    
    results = pd.DataFrame()
    
    for csv_name in csv_names:
        tmp_df = pd.read_csv(path + csv_name)
        tmp_df['patient_id'] = csv_name.replace(".csv", "")
        results = pd.concat([results, tmp_df])
    
    return results