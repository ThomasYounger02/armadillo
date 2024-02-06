def data_overview(data):
    '''呈现一个DF的主要信息
    '''
    print ("Rows             :" ,data.shape[0])
    print ("Columns          :" ,data.shape[1])
    print ("\nFeatures       :\n" ,data.columns.tolist())
    print ("\nMissing values :", data.isnull().sum().values.sum())
    print ("\nUnique values  :\n",data.nunique())