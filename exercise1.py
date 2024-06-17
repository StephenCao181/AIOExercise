def evaluate_class_model(tp, fp, fn):
# check if inputs are integer:
    if not isinstance(tp, int):
        print("tp must be an integer")
        return
    if not isinstance(fp, int):
        print("fp must be an integer")
        return
    if not isinstance(fn, int):
        print("fn must be an integer")
        return

# check if tp, fp, fn are lower than 0:
    if tp <= 0:
        print("tp must be greater than or equal to 0")
        return
    if fp <= 0:
        print("fp must be greater than or equal to 0")
        return
    if fn <= 0:
        print("fn must be greater than or equal to 0")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1 # return only F1

assert round(evaluate_class_model(2,3,5),2) == 0.33
print(round(evaluate_class_model(2, 4, 5), 2))