from elfarclass import ElFarolBar

''' Default parameters
bar = ElFarolBar(num_agents=100, num_contagious_agents=50, capacity=80, threshold=0.6, contagious_threshold=0.2 , contagious_duration=6,  people_memory_weight=0.1, contagious_thresholdNotPresent=0.8, debugCSV=True)
weeks_until_full = bar.simulate(num_weeks=150, respect_the_max=False)
'''

bar = ElFarolBar(num_agents=100, num_contagious_agents=5, capacity=80, threshold=0.6, contagious_threshold=0.2 , contagious_duration=6,  people_memory_weight=0.1, contagious_thresholdNotPresent=0.8, Use_SIR=True, SIR_AgentsRecoveryTime=4, debugCSV=True)
weeks_until_full = bar.simulate(num_weeks=150, respect_the_max=True)
print(f"The bar reached capacity in week {weeks_until_full[0] + 1}.")

bar.chartSave()



