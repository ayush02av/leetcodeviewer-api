import pandas as pd
import numpy as np
import pickle as pkl

def get_problem_set(data):
    '''
    Function to generate problem_set dictionary of type and number of questions solved
    '''
    try:
        problem_set = dict()

        for label in ['advanced', 'intermediate', 'fundamental']:
            if label in data['skillStats'].keys():
                for problem in data['skillStats'][label]:
                    problem_set[problem['tagSlug']] = problem['problemsSolved']

        return problem_set if len(problem_set.keys()) > 0 else np.NaN
    except:
        return np.NaN
    
def get_problem_status(row, problem_set):
    '''
    Function to get count of each problem
    '''
    values = list()
    for problem in problem_set:
        if problem in row[2].keys():
            values.append(row[2][problem])
        else:
            values.append(0)
    return values

def generate_df(details):
    df = pd.DataFrame.from_dict({
        'data': [details],
        'rating': [details['rating']]
    })

    df['problems'] = df.data.apply(get_problem_set)
    problem_set = pkl.load(open('./states/problem_set.pkl', 'rb'))
    df[list(problem_set)] = df.apply(lambda row: get_problem_status(row, problem_set), axis = 1, result_type = 'expand')

    return df