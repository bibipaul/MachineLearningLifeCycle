import numpy as np
from LoadDataSet import LoadHosingData
import hashlib
from sklearn.model_selection import train_test_split

#class train_test_set:
def __init__(self):
    return self

def create_test_train_random(housing, test_ratio):
    np.random.seed(42)
    random_indices = np.random.permutation(len(housing))
    test_size = int(len(housing)* test_ratio)
    
    test_indices = random_indices[:test_size]
    train_indices = random_indices[test_size:]
    
    print (len(random_indices))
    print (len(test_indices), len(train_indices))
    print (len(train_indices)+len(test_indices))
            
    print (test_indices)
    return housing.iloc[train_indices], housing.iloc[test_indices]
    
housing = LoadHosingData.load_housing_data()

#    train_data, test_data= create_test_train_random(housing,0.2)
#    print(train_data)

def test_set_check(identifier,test_ratio,hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
#    test_class =train_test_set()
    in_test_set = ids.apply(lambda id_: 
        test_set_check(id_, test_ratio,hash))
    return data.loc[~in_test_set], data.loc[in_test_set]
    
housing_with_id = housing.reset_index()
train_data, test_data= split_train_test_by_id(housing_with_id, 0.2, "index")        

print(len(train_data), len(test_data), len(housing))

def sklearn_data_split(housing):
    train_set, test_set = train_test_split(housing, 
                                           test_size=0.2, random_state=42 )
    
#train_set,test_set = sklearn_data_split(housing)

    
    