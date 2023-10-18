import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_plots(folder_path):
    files = os.listdir(folder_path)
    csv_files = [f for f in files if f.endswith('.csv')]

    sample_file_path = os.path.join(folder_path, csv_files[0])
    data_sample = pd.read_csv(sample_file_path)

    for col_name in data_sample.columns[1:]:
        plt.figure(figsize=(10, 6))

        for file in csv_files:
            file_path = os.path.join(folder_path, file)
            data = pd.read_csv(file_path)

            # Group by 'data_variable_size' and calculate mean
            data_avg = data.groupby('data_variable_size').mean().reset_index()

            x_data = data_avg.iloc[:, 0]
            plt.plot(x_data, data_avg[col_name], marker='o', linestyle='-', label=file.strip('.csv'))

        plt.title(col_name)
        plt.xlabel('Number of nodes')
        plt.ylabel(col_name)
        plt.legend(loc='upper right')
        plt.savefig(os.path.join(folder_path, f"{col_name}.png"))
        plt.close()


generate_plots('out')
