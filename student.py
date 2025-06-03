def drop_columns(df, columns_to_drop):
    """
    Drops specified columns from a DataFrame.

    Parameters:
    - df (pd.DataFrame): The original DataFrame.
    - columns_to_drop (list): List of column names to drop.

    Returns:
    - pd.DataFrame: New DataFrame with columns removed.
    """
    return df.drop(columns=columns_to_drop, axis=1)
