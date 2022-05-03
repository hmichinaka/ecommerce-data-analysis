import os
import pandas as pd

class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "data", "csv")
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]
        key_names = []
        for key in file_names:
            key_name = key.replace("olist_", "").replace("_dataset.csv", "").replace(".csv", "")
            key_names.append(key_name)
        data = {}
        for (x, y) in zip(key_names, file_names):
            data[x] = pd.read_csv(os.path.join(csv_path, y))
        return data
