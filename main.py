import TOSICA
import scanpy as sc


mcdaa = sc.read_h5ad('data/wang/MCDAA.h5ad')
TOSICA.train(mcdaa, 'mouse_gobp', project='test', label_name='cell_type')
