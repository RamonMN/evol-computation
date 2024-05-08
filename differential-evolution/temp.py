import pandas as pd
configs = {"config1": [None, 0.25, 0.5, 50],
           "config2": [None, 0.25, 0.5, 100],
           "config3": [None, 0.25, 0.5, 200],
           "config4": [None, 0.25, 1.5, 50],
           "config5": [None, 0.25, 1.5, 100],
           "config6": [None, 0.25, 1.5, 200],
           "config7": [None, 0.75, 0.5, 50],
           "config8": [None, 0.75, 0.5, 100],
           "config9": [None, 0.75, 0.5, 200],
           "config10": [None, 0.75, 1.5, 50],
           "config11": [None, 0.75, 1.5, 100],
           "config12": [None, 0.75, 1.5, 200],
           "config13": [0.75, 0.25, 0.5, 50],
           "config14": [0.75, 0.25, 0.5, 100],
           "config15": [0.75, 0.25, 0.5, 200],
           "config16": [0.75, 0.25, 1.5, 50],
           "config17": [0.75, 0.25, 1.5, 100],
           "config18": [0.75, 0.25, 1.5, 200],
           "config19": [0.75, 0.75, 0.5, 50],
           "config20": [0.75, 0.75, 0.5, 100],
           "config21": [0.75, 0.75, 0.5, 200],
           "config22": [0.75, 0.75, 1.5, 50],
           "config23": [0.75, 0.75, 1.5, 100],
           "config24": [0.75, 0.75, 1.5, 200]    
}

df = pd.DataFrame()


df["test"] = [1, 2, 3, 4, 5]
print(df.head())