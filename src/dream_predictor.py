import numpy as np

def predict_rem_probability(micro_movements: list) -> float:
    # Variance of micro-movements indicates dreaming phase
    var = np.var(micro_movements)
    return min(1.0, float(var * 50))
