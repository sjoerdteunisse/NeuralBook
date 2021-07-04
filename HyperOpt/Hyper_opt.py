import optuna

def objective_f(trial):
    print('strating trial', trial)
    #define the parameter m and call fit

#TPE and ASHA, Bayes
study = optuna.create_study()
study.optimize(objective, n_trials=100)
