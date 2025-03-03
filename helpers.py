import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

def info_with_nones(df):
    """Displays info only for columns with missing values."""
    null_counts = df.isnull().sum()
    cols_with_nones = null_counts[null_counts > 0].index
    couter = 0
    if not cols_with_nones.empty:
        for col in cols_with_nones:
            couter = couter+1
            print(f"Column: {col}")
            print(f"Non-Null Count: {df[col].count()}")
            print(f"Null Count: {df[col].isnull().sum()}")
            print(f"Dtype: {df[col].dtype}")
            print("-" * 20)
    else:
        print("No columns with missing values found.")
    print(f'Number of columns with Nones={couter}')
    
    
    
# def impute_column_mean(df, column_name):
#     """Imputes a column using the mean."""
#     mean_value = df[column_name].mean()
#     df[column_name] = df[column_name].fillna(mean_value)
#     return df

# def impute_column_knn_sklearn(df, column_name, k=5):
#     """Imputes a column using sklearn's KNNImputer."""
#     df_numeric = df.select_dtypes(include=np.number)
#     imputer = KNNImputer(n_neighbors=k)
#     df_imputed = imputer.fit_transform(df_numeric)
#     df_imputed = pd.DataFrame(df_imputed, columns=df_numeric.columns, index=df.index)
#     df[column_name] = df_imputed[column_name]
#     return df
