from autogluon.tabular import TabularDataset, TabularPredictor
import csv
import random
import autogluon.eda.analysis as eda
import autogluon.eda.visualization as viz
import autogluon.eda.auto as auto
import pandas as pd

#Generates a new randomized training and test dataset
#data (n=518)
#training roughly 80% (n=414)
#testing roughly 20% (n=104)


def split():
    data = []

    #opens data into a list of lists
    with open("data_pre.csv", "r", encoding='utf-8-sig') as f:
        data_reader = csv.reader(f)
        header = next(data_reader)
        for row in data_reader:
            data.append(row)

    random.shuffle(data)

    #splits data into aforementioned ratio
    train_data = data[:414]
    test_data = data[414:]

    #creates csv file with training data
    with open('train_data.csv', 'w', newline='') as g:
        writer = csv.writer(g)
        writer.writerow(header)
        for row in train_data:
            writer.writerows([row])

    #creates csv file with testing data
    with open('test_data.csv', 'w', newline='') as h:
        writer = csv.writer(h)
        writer.writerow(header)
        for row in test_data:
            writer.writerows([row])

#MACE definined as : CV Death, Non-fatal MI, Ischemic/Hemorrhagic Stroke, Unstable Angina, HF

#Uses data to train and test multi-layer model
def tabular():
    train_data = TabularDataset('data_raw.csv')
    #test_data = TabularDataset('data_final.csv')
    ignore = ["MACE"]

    #the value we want to predict
    label = "MACE"

    #trains model with hyperparameter optimization of individual models and model ensembling based on bootstrap aggregation (bagging and multi-layer stacking)
    predictor = TabularPredictor(label=label, eval_metric='roc_auc', learner_kwargs={"ignored_columns":ignore}).fit(train_data, auto_stack=True, presets='best_quality', hyperparameters = "extreme")
    predictor.fit_summary()

    '''
    #creates csv file with ranked feature importance
    importance_data = predictor.feature_importance(test_data)
    importance_data.to_csv('importance_'+label+'.csv', encoding='UTF-8')

    #creates csv file with model leaderboard
    leaderboard_data = predictor.leaderboard(test_data, extra_metrics=['accuracy', 'roc_auc'], silent=True)
    leaderboard_data.to_csv('leaderboard_'+label+'.csv', encoding='UTF-8')
    '''

#split()
tabular()
