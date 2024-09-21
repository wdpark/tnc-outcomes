from autogluon.tabular import TabularDataset, TabularPredictor
import csv
import random
import autogluon.eda.analysis as eda
import autogluon.eda.visualization as viz
import autogluon.eda.auto as auto

#Generates a new randomized training and test dataset
#data (n=682)
#training (n=478) roughly 70%
#testing (n=204) roughly 30%

def split():
    data = []

    #opens data into a list of lists
    with open("data.csv", "r", encoding='utf-8-sig') as f:
        data_reader = csv.reader(f)
        header = next(data_reader)
        for row in data_reader:
            data.append(row)

    random.shuffle(data)

    #splits data into aforementioned ratio
    train_data = data[:478]
    test_data = data[478:]

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

#split()

#Uses data to train and test multi-layer model
def tabular():
    train_data = TabularDataset('train_data.csv')
    test_data = TabularDataset('test_data.csv')

    #the value we want to predict
    label = 'Potassium'

    #trains model
    time_limit = 700
    metric = 'roc_auc'
    predictor = TabularPredictor(label=label, eval_metric=metric).fit(train_data, presets='best_quality')

    #creates csv file with ranked feature importance
    importance_data = predictor.feature_importance(test_data)
    importance_data.to_csv('importance_data.csv', encoding='UTF-8')

    #creates csv file with model leaderboard
    leaderboard_data = predictor.leaderboard(test_data, silent=True)
    leaderboard_data.to_csv('leaderboard_data.csv', encoding='UTF-8')


    auto.analyze(model=predictor, label=label, train_data=train_data, val_data=test_data, anlz_facets=[
    eda.model.AutoGluonModelEvaluator(),
], viz_facets=[
    viz.model.ConfusionMatrix(fig_args=dict(figsize=(5,5)), headers=True, annot_kws={"size": 12}),
])
    

tabular()