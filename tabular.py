from autogluon.tabular import TabularDataset, TabularPredictor
import csv
import random
import autogluon.eda.analysis as eda
import autogluon.eda.visualization as viz
import autogluon.eda.auto as auto

#Generates a new randomized training and test dataset
#data (n=303)
#training roughly 70%
#testing roughly 30%

#Cleveland Heart Data
#    -- Only 14 used
#      -- 1. #3  (age)       
#      -- 2. #4  (sex)       
#      -- 3. #9  (cp)        
#      -- 4. #10 (trestbps)  
#      -- 5. #12 (chol)      
#      -- 6. #16 (fbs)       
#      -- 7. #19 (restecg)   
#      -- 8. #32 (thalach)   
#      -- 9. #38 (exang)     
#      -- 10. #40 (oldpeak)   
#      -- 11. #41 (slope)     
#      -- 12. #44 (ca)        
#      -- 13. #51 (thal)      
#      -- 14. #58 (num)       (the predicted attribute)

def split():
    data = []

    #opens data into a list of lists
    with open("processed.cleveland.csv", "r", encoding='utf-8-sig') as f:
        data_reader = csv.reader(f)
        header = next(data_reader)
        for row in data_reader:
            data.append(row)

    random.shuffle(data)

    #splits data into aforementioned ratio
    train_data = data[:212]
    test_data = data[212:]

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


#Uses data to train and test multi-layer model
def tabular():
    train_data = TabularDataset('train_data.csv')
    test_data = TabularDataset('test_data.csv')

    #the value we want to predict
    label = 'num'

    #trains model
    metric = 'roc_auc'
    predictor = TabularPredictor(label=label, eval_metric=metric).fit(train_data, auto_stack=True, presets='best_quality')

    #creates csv file with ranked feature importance
    importance_data = predictor.feature_importance(test_data)
    importance_data.to_csv('importance_data.csv', encoding='UTF-8')

    #creates csv file with model leaderboard
    leaderboard_data = predictor.leaderboard(test_data, extra_metrics=['accuracy'], silent=True)
    leaderboard_data.to_csv('leaderboard_data.csv', encoding='UTF-8')

"""
    auto.analyze(model=predictor, label=label, train_data=train_data, val_data=test_data, anlz_facets=[
    eda.model.AutoGluonModelEvaluator(),
], viz_facets=[
    viz.model.ConfusionMatrix(fig_args=dict(figsize=(5,5)), headers=True, annot_kws={"size": 12}),
])
"""    

#split()
tabular()