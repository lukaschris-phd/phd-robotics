prior = 10.0
P_prior = 4.0

measurement = 12.0
R = 16

K = P_prior / (P_prior + R)

innovation = measurement - prior

posterior = prior + K * innovation

P_posterior = (1 - K) * P_prior

print(f"Kalman Gain : {K:.3f}")
print(f"Innovation  : {innovation:.3f} m")
print(f"Posterior   : {posterior:.3f} m")
print(f"Variance    : {P_posterior:.3f} m²")

# Summary:
# The Kalman Gain (K) sis calculated based on the prior variance (P_prior) 
# and the measurement noise (R).
# When R is large, the Kalman Gain is small, 
# meaning the measurement has less influence on the posterior estimate.