import pandas as pd

def read_keywords(file_path):
    df = pd.read_csv(file_path)


    required_columns = ["Keyword", "Intent", "Volume", "Keyword Difficulty"]
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Input file must contain Keyword, Intent, Volume, and Keyword Difficulty columns.")


    keywords_data = df[["Keyword", "Volume", "Keyword Difficulty"]]

    return keywords_data


def sort_keywords(df):

    sorted_df = df.sort_values(by=["Volume", "Keyword Difficulty"], ascending=[False, True])
    return sorted_df


def write_keywords(df, output_file):

    df["Volume"] = pd.to_numeric(df["Volume"], errors='coerce').fillna(0).astype(int)  
    df["Keyword Difficulty"] = pd.to_numeric(df["Keyword Difficulty"], errors='coerce').fillna(0).astype(int) 


    df.columns = ["Keyword", "Search Volume", "Keyword Difficulty"]


    df.to_csv(output_file, index=False, sep=',')
    print(f"Sorted keywords saved to {output_file}")


def process_keywords(input_file, output_file):
    keywords_df = read_keywords(input_file)
    sorted_keywords_df = sort_keywords(keywords_df)
    write_keywords(sorted_keywords_df, output_file)


input_file = 'input.csv' 
output_file = 'output.csv'  

process_keywords(input_file, output_file)  
