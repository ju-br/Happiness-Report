# Cleaning columns names
def stand_colum_name(df):
    ````
    `standardize column names
    ````
    dict_rename = {column : column.lower().strip() for column in df.columns}
    df = df.rename(dict_rename, axis = 1, inplace = True)

# Changing the type to float
def historic_to_float(df):
   ````
    `change numeric columns with comma to float``
    ````

    for i in df.columns:
        try:
            df[i] = df[i].apply(lambda x: float(x.replace(",", ".")))
        except:
            pass

def temperature(df):
       ````
    `clean temperature column
    ````
    df['average yearly temperature (1961–1990 celsius)'] = df['average yearly temperature (1961–1990 celsius)'].apply(lambda x: x.replace('−','-'))

# Changing the type
def percent_to_float(df):
       ````
    `transform percentage to float
    ````
    for i in df.columns:
        if i != 'average yearly temperature (1961–1990 celsius)':
            try:
                df[i] = df[i].apply(lambda x: float(x.replace("%", "")))
            except:
                pass

def to_numeric(df):
       ````
    `transform temperature to float
    ````
    try:
        df = df.apply(pd.to_numeric)
    except:
        pass
    df['average yearly temperature (1961–1990 celsius)'] = df['average yearly temperature (1961–1990 celsius)'].apply(lambda x: float(x))
    
