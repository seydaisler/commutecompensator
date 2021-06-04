print('***Commuting Compensation Calculator Application***\n')

means_of_transport=(input('How do you go to work?\nPlease write one of the options: "on foot", "by bike", "by train" , "by car"\n'))

distance_in_km=int(input('How many kms do you travel?\n'))
compensation=0
if means_of_transport=='by bike':
  compensation= distance_in_km * 0.5

elif means_of_transport =='by train': 
  compensation= distance_in_km=distance_in_km * 0.25

elif means_of_transport== 'by car':
  compensation= distance_in_km * 0.10

elif means_of_transport== 'on foot':
  compensation= distance_in_km * 0.80


print('Your commute compensation is' , compensation, '€ per month.')