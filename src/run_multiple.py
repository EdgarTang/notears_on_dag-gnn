import csv
import os

def create_csv_files(min_val, max_val, step):
    output_dir = 'out'
    os.makedirs(output_dir, exist_ok=True)

    filenames = ['notears.csv', 'DAG-GNN_best_ELBO_graph.csv', 'DAG-GNN_best_NLL_graph.csv',
                 'DAG-GNN_best_MSE_graph.csv', 'DAG-GNN_threshold01.csv',
                 'DAG-GNN_threshold02.csv', 'DAG-GNN_threshold03.csv']

    headers = ['data_variable_size', 'fdr', 'tpr', 'fpr', 'shd', 'nnz']

    for filename in filenames:
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            for data_size in range(min_val, max_val + step, step):
                writer.writerow([data_size] + [0] * (len(headers) - 1))
# Usage
start = 10
end = 100
step = 10
create_csv_files(start, end, step)


# for i in range(start, (end + 1), step):
#     command = ["python", "notears_on_dag-gnn/src/main.py", "--data_variable_size=" + str(i)]
#     subprocess.run(command)
