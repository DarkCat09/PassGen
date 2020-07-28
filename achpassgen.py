# encoding: utf-8

print("")
print("****** PASSWORD DICTIONARY GENERATOR *******")
print("*** by AndreyCh (DarkCat09/CodePicker13) ***")
print("")

targets_personal_data = [
    "",
    input("Target's name: "), input("Target's last name: "), input("Target's nickname: "), input("Target's birthday, DDMMYYYY: "),
    input("Spouse's name: "), input("Spouse's last name: "), input("Spouse's nickname: "), input("Spouse's birthday, DDMMYYYY: "),
    input("Child's name: "), input("Child's last name: "), input("Child's nickname: "), input("Child's birthday, DDMMYYYY: "),
    input("Pet's name: "), input("Pet's last name: "), "", input("Pet's birthday, DDMMYYYY: "),
    input("First target's phone number, +X 9YYYYYYYYY: "), input("Second target's phone number, +X 9YYYYYYYYY: "), input("Date of password setting, MMYYYY: ")
]
print("")

dicfile = open("dictionary.txt", "wt", encoding="utf-8")

for i in range(19):
    for j in range(19):
        if not ((targets_personal_data[i] + targets_personal_data[j]) == ""):
            dicfile.write(targets_personal_data[i] + targets_personal_data[j] + "\n")
            dicfile.write(targets_personal_data[i].upper() + targets_personal_data[j] + "\n")
            dicfile.write(targets_personal_data[i] + targets_personal_data[j].upper() + "\n")
            dicfile.write(targets_personal_data[i].upper() + targets_personal_data[j].upper() + "\n")

#code

dicfile.close()

print("")
input("Press ENTER to exit")
