from pycaret.classification import *

# data and metric imports
import sklearn.model_selection
import sklearn.datasets
from sklearn.metrics import *

df_digits = sklearn.datasets.load_digits(as_frame=True)["frame"]

df_train, df_test = sklearn.model_selection.train_test_split(df_digits, random_state=0)

print("data_train", df_train)
print("data_test", df_test)

# setup PyCaret
setup(
    df_train,
    target="target",
)

# train model
best_model = compare_models()
print("best_model", best_model)

# tune model
tuned_model = tune_model(best_model)
print("tuned_model", tuned_model)

# finalize model
final_model = finalize_model(tuned_model)
print("final_model", final_model)

# predict
df_pred = predict_model(final_model, data=df_test)
print("df_pred", df_pred)

score = accuracy_score(df_pred["target"], df_pred["Label"])
print("Accuracy score", score)
