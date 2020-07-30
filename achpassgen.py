# encoding: utf-8

## Copyright © 2020 Чечкенёв Андрей
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

def lowstr(string):
    return string.lower()
def uppstr(string):
    return string.upper()
def capstr(string):
    return string.capitalize()

print("")
print("************ PASSWORD DICTIONARY GENERATOR *************")
print("********* by AndreyCh (DarkCat09/CodePicker13) *********")
print("*** Licensed by GNU General Public License version 2 ***")
print("")

target_personal_data = [
    {
        "name": input("Target's name: "),
        "secondname": input("Target's second name: "),
        "lastname": input("Target's last name: "),
        "nickname": input("Target's nickname: "),
        "birth": input("Target's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Spouse's name: "),
        "secondname": input("Spouse's second name: "),
        "lastname": input("Spouse's last name: "),
        "nickname": input("Spouse's nickname: "),
        "birth": input("Spouse's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Child's name: "),
        "secondname": input("Child's second name: "),
        "lastname": input("Child's last name: "),
        "nickname": input("Child's nickname: "),
        "birth": input("Child's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Pet's name: "),
        "secondname": input("Pet's second name: "),
        "lastname": input("Pet's last name: "),
        "birth": input("Pet's birthday, DDMMYYYY: ")
    },
    input("First target's phone number, +X 9YYYYYYYYY: "),
    input("Second target's phone number, +X 9YYYYYYYYY: "),
    input("Date of password setting, MMYYYY: ")
]
try:
    rus_locale = bool(int(input("Is target using russian locale? (1,y=yes;0,n=no) ").replace("y", "1").replace("n", "0")))
except ValueError:
    print("Incorrect value. Setting to \"No\".")
    rus_locale = bool(0)
print("")

old_strs = []
join_signs = ["", "_", "-", "&", "%", "+", "*", "#", "@", "$"]
dicdata = [
    "",
    target_personal_data[0]["name"], target_personal_data[0]["secondname"], target_personal_data[0]["lastname"], target_personal_data[0]["nickname"],
    target_personal_data[0]["birth"][0:2], target_personal_data[0]["birth"][2:4], target_personal_data[0]["birth"][4:8],
    target_personal_data[1]["name"], target_personal_data[1]["secondname"], target_personal_data[1]["lastname"], target_personal_data[1]["nickname"],
    target_personal_data[1]["birth"][0:2], target_personal_data[1]["birth"][2:4], target_personal_data[1]["birth"][4:8],
    target_personal_data[2]["name"], target_personal_data[2]["secondname"], target_personal_data[2]["lastname"], target_personal_data[2]["nickname"],
    target_personal_data[2]["birth"][0:2], target_personal_data[2]["birth"][2:4], target_personal_data[2]["birth"][4:8],
    target_personal_data[3]["name"], target_personal_data[3]["secondname"], target_personal_data[3]["lastname"],
    target_personal_data[3]["birth"][0:2], target_personal_data[3]["birth"][2:4], target_personal_data[3]["birth"][4:8],
    target_personal_data[4][3:], target_personal_data[4][1:2] + target_personal_data[4][3:],
    target_personal_data[5][3:], target_personal_data[5][1:2] + target_personal_data[5][3:]
]
data_functions = [lowstr, uppstr, capstr]
dicfile = open("dictionary.txt", "wt", encoding="utf-8")

try:
    for i in range(len(dicdata)-1):
        for j in range(len(dicdata)-1):
            for k in range(len(dicdata)-1):
                for l in range(len(dicdata)-1):
                    if not ((dicdata[i] + dicdata[j] + dicdata[k] + dicdata[l]) == ""):
                        for dfunc1 in data_functions:
                            for dfunc2 in data_functions:
                                for dfunc3 in data_functions:
                                    for dfunc4 in data_functions:
                                        for jsign1 in join_signs:
                                            for jsign2 in join_signs:
                                                for jsign3 in join_signs:
                                                        
                                                    result_string = \
                                                                  dfunc1(dicdata[i]) + jsign1 + \
                                                                  dfunc2(dicdata[j]) + jsign2 + \
                                                                  dfunc3(dicdata[k]) + jsign3 + \
                                                                  dfunc4(dicdata[l])
                                                                
                                                    for oldstr in old_strs:
                                                        if oldstr == result_string:
                                                            break
                                                    else:
                                                        print(result_string)
                                                        dicfile.write(result_string + "\n")
                                                        if len(old_strs) > 27:
                                                            old_strs.clear()
                                                        old_strs.append(result_string)

##                            for dfindex in range(81):
##                                
##                                result_string = \
##                                data_functions[(dfindex+0)%len(data_functions)](dicdata[i]) + jsign + \
##                                data_functions[(dfindex+1)%len(data_functions)](dicdata[j]) + jsign + \
##                                data_functions[(dfindex+2)%len(data_functions)](dicdata[k]) + jsign + \
##                                data_functions[(dfindex+3)%len(data_functions)](dicdata[l])
##                                
##                                if not (result_string == old_string):
##                                    dicfile.write(result_string + "\n")
##                                    old_string = result_string

except KeyboardInterrupt:
    print("Stopped by keyboard.")

#writing password: MonthYear (Russia += МесяцГод += (VtczwUjl=МесяцГод_Латинской_Раскладкой))

print("OK")
dicfile.close()
input("Press ENTER to exit")
