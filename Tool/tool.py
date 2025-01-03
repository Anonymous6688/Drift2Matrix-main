from SRModel.Block_SSC import Block_SSC
import numpy as np
from SRModel.SSC_model import ssc_model
from SRModel.LRR_model import demo




def find_Block(data, K,win_size,lam,gam):
    [B, Z] = Block_SSC(np.array(data.values.tolist()), data.shape[1],
                       win_size, lam[5],
                       gam[0]).BDR_solver(K)
    '''sns.heatmap(B, annot=False, xticklabels=False, yticklabels=False, square=True, cmap="YlGnBu_r", cbar=True)
    plt.title('Block')
    plt.show()
'''
    return [B]


def find_ssc(data):
    B = ssc_model(data).computeCmat()
    B = np.maximum(0, (B + B.T) / 2)
    return [B]




def find_lrr(data):
    [B, E] = demo(np.array(data.values.tolist()))
    return [B, E]



def zij(Y, i, j, lam, N):
    if i == j:
        return 0.0
    else:
        numerator = np.exp(-(np.square(np.linalg.norm(Y[:, i] - Y[:, j], 2))) / lam)
        # print(numerator)
        # sum_i=0
        # sum_j=0
        # for h in range(N):
        #     if h!=i:
        #         sum_i += np.exp(-(np.square(np.linalg.norm(Y[:,i]-Y[:,h],2)))/lam)
        # for h in range(N):
        #     if h!=j:
        #         sum_j += np.exp(-(np.square(np.linalg.norm(Y[:,j]-Y[:,h],2)))/lam)
        return numerator


