import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def read_keywords(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    keywords_data = []
    

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) >= 7:   
            keyword = parts[0]
            intent = parts[1]
            volume = int(parts[2]) if parts[2].isdigit() else 0
            difficulty = int(parts[3]) if parts[3].isdigit() else 0
            

            keywords_data.append([keyword, volume, difficulty])
    

    df = pd.DataFrame(keywords_data, columns=["Keyword", "Volume", "Difficulty"])
    return df


def sort_keywords(df):

    sorted_df = df.sort_values(by=["Volume", "Difficulty"], ascending=[False, True])
    return sorted_df


def write_keywords(df, output_file):
    df.to_csv(output_file, sep='\t', index=False)
    print(f"Sorted keywords saved to {output_file}")


def process_keywords(input_file, output_file):
    keywords_df = read_keywords(input_file)
    sorted_keywords_df = sort_keywords(keywords_df)
    write_keywords(sorted_keywords_df, output_file)


input_file = 'input.txt' 
output_file = 'output.txt' 

process_keywords(input_file, output_file)  
