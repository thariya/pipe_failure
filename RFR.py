import pandas as pd
import numpy as np
from RFR_models import pipeline_regression as regr
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor

model_pipelines = {}
model2save='training_file_rf'
model_name='RandomForest'
def train(df_training_entity, model2save,model_name):
    y = df_training_entity['Failed']

    X = df_training_entity[['#_failures','length','size', 'meanGL',  "age"]]

    ### setup the model to be used

    md_regr = regr(model_pipelines[model_name])

    ### training the  model
    print('Start training ...')
    # print('Start training by', model_name, '...')
    md_regr.train(X, y)
    print('Training for ', model_name, 'is completed.')

    ### saving the  model
    md_regr.save_model(model2save)
    print('Trained model is saved.')


def predict(df_testing_entity, model2read, model_name):

    X = df_testing_entity[['#_failures','length','size', 'meanGL',  "age"]]

    md_regr = regr(model_pipelines[model_name])
    md_regr.load_model(model2read)

    y_pred = md_regr.predict(X)

    df_testing_entity['y_pred'] = y_pred
    return df_testing_entity

df1=pd.read_csv('training_file' + '.csv')

df_training_entity = df1[df1['observation_year'] <2012]
df_testing_entity = df1[df1['observation_year'] == 2015]
df_testing_pipes=df_testing_entity['pipes']
df_testing_failures=df_testing_entity['Failed']

dic={}

model_pipelines['RandomForest'] = RandomForestRegressor(n_estimators=100, min_samples_leaf=5,
                                                            random_state=None, max_features=5, n_jobs=-1)
train( df_training_entity, model2save,model_name)
pred=df_predicting_entity = predict(df_testing_entity, model2save, model_name)

pred.to_csv('rf_sw.csv',index=False)