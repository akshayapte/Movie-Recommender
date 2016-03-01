from recommendations import *
from recommendations import critics

print "User Based recommendations for Toby: (using Pearson coefficient)\n"
ranks = getRecommendations(critics,'Toby')
i=1
for rank in ranks:
	print "%d)" % i,rank 
	i=i+1

print "-----------------------------------------------------------------------------------------------"
itemsim=calculateSimilarItems(critics)
print "\nItem Based recommendations for Toby:\n"
ranks = getRecommendedItems(critics,itemsim,'Toby')
i=1
for rank in ranks:
	print "%d)" % i,rank 
	i=i+1
print "==============================================================================================="

#Recommendation for movielens dataset
print "\nUsing MovieLens Dataset:\n"
prefs=loadMovieLens( )


prefs.setdefault(0,{})
prefs['0'] = {'Birdcage, The (1996)': 2.49776569, 'Enchanted April (1991)': 2.0, 'Diabolique (1996)': 1.1}
#print prefs.items()[0]


print "\nUser Based recommendations for User0: (using Pearson coefficient)\n"
ranks = getRecommendations(prefs,'0')[0:30]

i=1
for rank in ranks:
	print "%d)" % i,rank 
	i=i+1
print "-----------------------------------------------------------------------------------------------"

itemsim=calculateSimilarItems(prefs,n=50)
print "\nItem Based recommendations for User0:\n"
ranks = getRecommendedItems(prefs,itemsim,'0')[0:30]
i=1
for rank in ranks:
	print "%d)" % i,rank 
	i=i+1
print "==============================================================================================="
