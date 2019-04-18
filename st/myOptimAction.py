def myOptimAction(priceVec, transFeeRate):
    import numpy as np
    dataLen = len(priceVec)
    actionVec = np.zeros(dataLen)
    
    ic=dataLen-1
    actionVec[ic] = -1
    for ie in range(dataLen-1,-1,-1):
        if actionVec[ic]==1:
            if priceVec[ie]<priceVec[ic]:
                actionVec[ie]=1
                
                ic=ie

            elif priceVec[ie]*(1-transFeeRate)**2>priceVec[ic]:
                actionVec[ie]=-1
                
                ic=ie

        elif actionVec[ic]==-1:
            if priceVec[ie]/(1-transFeeRate)**2<priceVec[ic]:
                actionVec[ie]=1
                
                ic=ie
  
            elif priceVec[ie]>priceVec[ic]:
                actionVec[ie]=-1
        
                ic=ie

    actionVec[ic] = 0
     
    return actionVec
