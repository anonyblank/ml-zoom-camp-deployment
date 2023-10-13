import pickle5 as pickle
import numpy as np

with open('./model/model1.bin', 'rb') as mf:
  model = pickle.load(mf)

with open('./model/dv.bin', 'rb') as df:
  dv = pickle.load(df)

# print(model)
# client = {
#   "job": "retired", 
#   "duration": 445, 
#   "poutcome": "success"
# }

# client_feature = dv.transform(client)
# client_pred_label = model.predict_proba(client_feature)[:, 1]

# print(np.round(client_pred_label, 3))