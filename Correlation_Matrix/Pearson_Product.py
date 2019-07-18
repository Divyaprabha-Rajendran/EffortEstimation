from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr

def Pearson_product(data1,data2,logger):
    try:
        return (pearsonr(data1,data2))
    except exception as e:
        logger.error(e)

def Spearman(data1,data2,logger):
    try:
        return (spearmanr(data1,data2))
    except exception as e:
        logger.error(e)