import pandas as pd 

def fun(key):
    df = pd.read_csv("benefits.csv")
    df = df.set_index("exercise")
    
    df = df.dot(key)
    df = df.reset_index(level=0)
    df.columns = ["exercise", "scores"]
    df = df.sort_values(["scores"], ascending=0)
    print(df)
    return df

def get_aasan_baby():
    scores = fun([1, 1, 0, 0])
    d = {
        "plank": {"high": "2m", "medium": "1m", "low": "30s"},
        "downdog": {"high": "2m", "medium": "1m", "low": "30s"},
        "tree": {"high": "2m", "medium": "1m", "low": "30s"},
        "warrior2": {"high": "2m", "medium": "1m", "low": "30s"},
        "goddess": {"high": "2m", "medium": "1m", "low": "30s"}
    }

    scoring = {"high": [scores.exercise[0], scores.exercise[1]], "medium": [scores.exercise[2]], "low": [scores.exercise[3], scores.exercise[4]]}

    ret = {}

    for k, v in scoring.items():
        for v_ in v:
            ret[v_] = d[v_][k] + "-" +  d[v_][k] + "-" + d[v_][k]
    
    ret_final = {"exercise": [], "reps": []}
    for k, v in ret.items():
        ret_final["exercise"].append(k)
        ret_final["reps"].append(v)
    
    ret_final = pd.DataFrame(ret_final)
    
    return ret_final



