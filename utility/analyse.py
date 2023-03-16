import pandas as pd
import pickle as pkl

def analyse(df):
    # generating
    x = pd.concat([
        df.iloc[:, 1],
        df.iloc[:, 3:49]
    ], axis = 1)

    # scaling
    scaler = pkl.load(open('./states/scaler.pkl', 'rb'))
    x = pd.DataFrame(scaler.transform(x), columns = x.columns)

    # predicting
    model = pkl.load(open('./states/model.pkl', 'rb'))
    x['label'] = model.predict(x)

    # comparing
    features = pkl.load(open('./states/features.pkl', 'rb'))
    return {
        'label': int(x['label'][0]),
        'features': features
    }