#Practice 2
name = "Chatwimon Wangsabay"
age = 20
gender = False
sale = 25000.00
commission = sale * 0.07
interest = ['Java', 'Web Development', 'IOT', 'FinTech','Healthy', 'Sport car', 'Dog' ]
education = {'vocational':'Commercial','deploma':'Business Computer','bachelor': 'Information System','master': 'Information Technology','doctoral': 'Information Studies' }

print("************ My Variable Data *************")
print("Hello: " + name)
print("Your are: ", age, " years old")
print("Your gender are: ", gender)
print("Your sale for this month: ", sale , ", and getcommission: ", commission)
print("Your interest: ", len(interest) , " are: ",interest)
interest.append("Fashion")
print("Your interest after update: ", interest)
print("New your interest are: ", interest[7])
print("Your education are: ", education)
education['vocational'] = "Marketing"
education.update({'deploma': 'Finance'})
education['postdoctor'] = 'Digital Tranformation'
print("New your education are: ", education)
print("Your bachelor degree is: " ,education.get('bachelor'))
print("Good Bye.")
print("*********************")