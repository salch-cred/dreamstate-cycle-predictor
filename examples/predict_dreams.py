from src.dream_predictor import predict_rem_probability

movements = [0.01, 0.02, 0.01, 0.03, 0.02]
prob = predict_rem_probability(movements)
print("Calculated Dreaming Phase Probability:", round(prob, 4))
