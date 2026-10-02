print("==== PLACEMENT PREPERATION DASHBOARD ====")
name = input("Enter your name: ")
aptitude_score = int(input("Enter aptitude score: "))
coding_score = int(input("Enter coding score: "))
communication_score = int(input("Enter communication score: "))
average = (aptitude_score + coding_score + communication_score)/3
print("\n---- REPORT ----")
print("Name:",name)
print("Average score:", round(average, 2))
if average >= 80:
    print("Placement status: Excellent")
elif average >= 60:
    print("Placement status: Good")
else:
    print("Placement ststus: Needs Improvement")