import pandas as pd
import numpy as np
import pickle
import json
import config

class Sales_price_prediction:

    def __init__(self):
        print("INIT FUNCTION")

    def load_saved_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.sales_data = json.load(f)

    def price_pred(self,TV_sales,Radio_sales,News_paper_sales):
        
        self.load_saved_data()

        test_array = np.zeros(self.model.n_features_in_, int)
        test_array[0] = TV_sales
        test_array[1] = Radio_sales
        test_array[2] = News_paper_sales
        
        test_array

        sales = np.around(self.model.predict([test_array])[0] , 2)
        print(f"Predicted sales  is : {sales} $")    
        return sales
    
if __name__ == "__main__":
    sales_pp =Sales_price_prediction() 
    
#<form action="predict_sales_price", method="POST">
