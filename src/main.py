from train import *

f = open('trueG', 'w')
matG = np.matrix(nx.to_numpy_array(ground_truth_G))
for line in matG:
    np.savetxt(f, line, fmt='%.5f')
f.closed

f1 = open('predG', 'w')
matG1 = np.matrix(origin_A.data.clone().numpy())
for line in matG1:
    np.savetxt(f1, line, fmt='%.5f')
f1.closed


if log is not None:
    print(save_folder)
    log.close()
