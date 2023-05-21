import numpy as np
# Define the structure of the Alarm Bayesian network
# Variable names
variables = ['Burglary', 'Earthquake', 'Alarm', 'JohnCalls', 'MaryCalls']
# Parent-child relationships
edges = [('Burglary', 'Alarm'),
('Earthquake', 'Alarm'),
('Alarm', 'JohnCalls'),
('Alarm', 'MaryCalls')]
# Initialize the parameters of the Bayesian network
# CPTs for each variable
# CPT for Burglary
cpt_Burglary = np.array([0.001, 0.999])# CPT for Earthquake
cpt_Earthquake = np.array([0.002, 0.998])
# CPT for Alarm given Burglary and Earthquake
cpt_Alarm_given_BE = np.array([[[0.999, 0.001], [0.71, 0.29]],
[[0.06, 0.94], [0.05, 0.95]]])
# CPT for JohnCalls given Alarm
cpt_JohnCalls_given_A = np.array([[0.95, 0.05],
[0.10, 0.90]])
# CPT for MaryCalls given Alarm
cpt_MaryCalls_given_A = np.array([[0.99, 0.01],
[0.30, 0.70]])
# Store the CPTs in a dictionary for easy access
cpts = {'Burglary': cpt_Burglary,
'Earthquake': cpt_Earthquake,
'Alarm|Burglary,Earthquake': cpt_Alarm_given_BE,
'JohnCalls|Alarm': cpt_JohnCalls_given_A,
'MaryCalls|Alarm': cpt_MaryCalls_given_A}
# Generate a sample dataset
# Set random seed for reproducibility
np.random.seed(123)
# Generate 1000 samples
num_samples = 1000
# Initialize an empty dataset
data = np.zeros((num_samples, len(variables)), dtype=int)
# Sample from the network
for i in range(num_samples):
# Sample from Burglary
data[i, variables.index('Burglary')] = np.random.choice([0, 1], p=cpt_Burglary)
# Sample from Earthquake
data[i, variables.index('Earthquake')] = np.random.choice([0, 1], p=cpt_Earthquake)
# Sample from Alarm given Burglary and Earthquake
p_alarm = cpt_Alarm_given_BE[data[i, variables.index('Burglary')], data[i,
variables.index('Earthquake')]]
data[i, variables.index('Alarm')] = np.random.choice([0, 1], p=p_alarm)
# Sample from JohnCalls given Alarm
p_john_calls = cpt_JohnCalls_given_A[data[i, variables.index('Alarm')]]
data[i, variables.index('JohnCalls')] = np.random.choice([0, 1], p=p_john_calls)# Sample from MaryCalls given Alarm
p_mary_calls = cpt_MaryCalls_given_A[data[i, variables.index('Alarm')]]
data[i, variables.index('MaryCalls')] = np.random.choice([0, 1], p=p_mary_calls)
# EM algorithm for learning the parameters
# Initialize the parameters randomly
# CPTs for each variable
# EM algorithm for learning the parameters
# Initialize the parameters randomly
# CPTs for each variable
cpt_Burglary = np.random.random(size=2)
cpt_Earthquake = np.random.random(size=2)
cpt_Alarm_given_BE = np.random.random(size=(2, 2, 2))
cpt_JohnCalls_given_A = np.random.random(size=(2, 2))
cpt_MaryCalls_given_A = np.random.random(size=(2, 2))
# Iterate EM steps
num_iterations = 10
for iteration in range(num_iterations):
print(f"Iteration {iteration+1}...")
# E-step: Compute expected sufficient statistics
# Initialize expected counts
counts_Burglary = np.zeros(2)
counts_Earthquake = np.zeros(2)
counts_Alarm_given_BE = np.zeros((2, 2, 2))
counts_JohnCalls_given_A = np.zeros((2, 2))
counts_MaryCalls_given_A = np.zeros((2, 2))
for sample in data:
# Compute the posterior probability of the hidden variables using the current parameters
# Compute P(Burglary = 0) and P(Burglary = 1)
p_Burglary = cpt_Burglary
# Compute P(Earthquake = 0) and P(Earthquake = 1)
p_Earthquake = cpt_Earthquake
# Compute P(Alarm | Burglary, Earthquake)
p_Alarm_given_BE = cpt_Alarm_given_BE[:, sample[variables.index('Burglary')],
sample[variables.index('Earthquake')]]
# Compute P(JohnCalls | Alarm)
p_JohnCalls_given_A = cpt_JohnCalls_given_A[:, sample[variables.index('Alarm')]]# Compute P(MaryCalls | Alarm)
p_MaryCalls_given_A = cpt_MaryCalls_given_A[:, sample[variables.index('Alarm')]]
# Compute the joint probability of the hidden variables
joint_prob = p_Burglary * p_Earthquake * p_Alarm_given_BE * p_JohnCalls_given_A *
p_MaryCalls_given_A
# Compute the posterior probability of the hidden variables using Bayes' rule
posterior_prob = joint_prob / np.sum(joint_prob)
# Update the expected counts
counts_Burglary += posterior_prob[0] # 0 corresponds to Burglary = 0
counts_Earthquake += posterior_prob[1] # 1 corresponds to Burglary = 1
counts_Alarm_given_BE[:, sample[variables.index('Burglary')],
sample[variables.index('Earthquake')]] += posterior_prob
counts_JohnCalls_given_A[:, sample[variables.index('Alarm')]] += posterior_prob
counts_MaryCalls_given_A[:, sample[variables.index('Alarm')]] += posterior_prob
# M-step: Update the parameters using the expected sufficient statistics
# Update CPT for Burglary
cpt_Burglary = counts_Burglary / np.sum(counts_Burglary)
# Update CPT for Earthquake
cpt_Earthquake = counts_Earthquake / np.sum(counts_Earthquake)
# Update CPT for Alarm given Burglary and Earthquake
# Update CPT for Alarm given Burglary and Earthquake
# Update CPT for Alarm given Burglary and Earthquake
for i in range(2):
for j in range(2):
for k in range(2):
denominator = np.sum(counts_Alarm_given_BE[i, j, :])
if denominator != 0:
cpt_Alarm_given_BE[i, j, k] = counts_Alarm_given_BE[i, j, k] / denominator
# Update CPT for JohnCalls given Alarm
for i in range(2):
for j in range(2):
cpt_JohnCalls_given_A[i, j] = counts_JohnCalls_given_A[i, j] /
np.sum(counts_JohnCalls_given_A[i, :])
# Update CPT for MaryCalls given Alarm
for i in range(2):
for j in range(2):
cpt_MaryCalls_given_A[i, j] = counts_MaryCalls_given_A[i, j] /
np.sum(counts_MaryCalls_given_A[i, :])
# Print the learned parametersprint("Learned Parameters:")
print("CPT for Burglary:")
print(cpt_Burglary)
print()
print("CPT for Earthquake:")
print(cpt_Earthquake)
print()
print("CPT for Alarm given Burglary and Earthquake:")
print(cpt_Alarm_given_BE)
print()
print("CPT for JohnCalls given Alarm:")
print(cpt_JohnCalls_given_A)
print()
print("CPT for MaryCalls given Alarm:")
print(cpt_MaryCalls_given_A)
