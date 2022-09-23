"""
Calculates P, R, and F1 across all combinations of dataset

Run Instructions:

Before running, populate gold folder with all folders (format gold/consult, gold/discharge_summary, etc)
Output folder should be populated with output from running medacy script (train_medacy.py and test_medacy.py)

then simply run

python brateval.py

output will be to results.csv in same directory










"""

# calculate P, R, F across all combinations of categories


from medacy.tools.calculators.inter_dataset_agreement import measure_dataset
from medacy.data import Dataset

# gold = Dataset("gold")
# out = Dataset("output")
# average_recall = 0
# average_precision  = 0
# average_f1 = 0
# measures= measure_dataset(gold, out)
# for measure in measures:
# 	print(measure)
# 	print("Recall: "+ str(measures[measure].recall()))
# 	print("Precision: "+ str(measures[measure].precision()))
# 	print("f1: "+ str(measures[measure].f_score()))
# 	average_recall += measures[measure].recall()
# 	average_precision += measures[measure].precision()
# 	average_f1+= measures[measure].f_score()
#
# print("Average Recall: "+str(average_recall/len(measures)))
# print("Average Precision: "+str(average_precision/len(measures)))
# print("Average f1: "+str(average_f1/len(measures)))

categories = ["consult", "discharge_summary", "general", "nursing", "pharmacy", "physician"]
out_file = open("results.csv", "w")
for m in categories:

	for t in categories:

		if m!=t:
			out_file.write("Trained on " + m + " Tested on " + t+"\n\n")
			out_file.write("entity,recall,precision,f1\n")
			gold = Dataset("gold/"+t)
			out = Dataset("output/"+m+t)
			average_recall = 0
			average_precision  = 0
			average_f1 = 0
			measures= measure_dataset(gold, out)
			for measure in measures:
				out_file.write(measure+","+str(measures[measure].recall())+","+str(measures[measure].precision())+","+str(measures[measure].f_score())+"\n")
				average_recall += measures[measure].recall()
				average_precision += measures[measure].precision()
				average_f1+= measures[measure].f_score()
			out_file.write("\n")
			out_file.write("Average,"+str(average_recall/len(measures))+","+str(average_precision/len(measures))+","+str(average_f1/len(measures))+"\n\n\n")

out_file.close()