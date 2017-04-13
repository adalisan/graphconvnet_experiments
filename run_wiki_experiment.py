import networkx
import numpy as np
def main:
  en_wch_file = DATA_DIR+"/en.wch"
  fr_wch_file = DATA_DIR+"/fr.wch"
  EN_WCH_Mat = None
  FR_WCH_Mat = None
  open (en_wch_file,'r') as en_f:
    en_lines = en_f.readlines()
    row_count = len(en_lines)
    EN_WCH_Mat = np.zeros([row_count,])
    FR_WCH_Mat = np.zeros([row_count,])
    for i,line in enumerate(en_lines):
      en_line.split()
    
      
