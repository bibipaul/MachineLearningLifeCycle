import pandas as pd
import os

class LoadHosingData:

    HOUSING_PATH ="C:/Users/Paul/Desktop/AI/Python/Learning/MachineLearningLifeCycle/DataSet/"    
    def load_housing_data(housing_path=HOUSING_PATH):
        csv_path = os.path.join(housing_path, "housing.csv")
        return pd.read_csv(csv_path)
    
    housing = load_housing_data()
    print (housing)