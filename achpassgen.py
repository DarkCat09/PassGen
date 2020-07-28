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

print("")
print("****** PASSWORD DICTIONARY GENERATOR *******")
print("*** by AndreyCh (DarkCat09/CodePicker13) ***")
print("")

target_personal_data = [
    {
        "name": input("Target's name: "),
        "lastname": input("Target's last name: "),
        "nickname": input("Target's nickname: "),
        "birth": input("Target's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Spouse's name: "),
        "lastname": input("Spouse's last name: "),
        "nickname": input("Spouse's nickname: "),
        "birth": input("Spouse's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Child's name: "),
        "lastname": input("Child's last name: "),
        "nickname": input("Child's nickname: "),
        "birth": input("Child's birthday, DDMMYYYY: ")
    },
    {
        "name": input("Pet's name: "),
        "lastname": input("Pet's last name: "),
        "birth": input("Pet's birthday, DDMMYYYY: ")
    },
    input("First target's phone number, +X 9YYYYYYYYY: "),
    input("Second target's phone number, +X 9YYYYYYYYY: "),
    input("Date of password setting, MMYYYY: ")
]
print("")

join_signs = ["", "_", "-"]
dicdata = [
    "",
    target_personal_data[0]["name"], target_personal_data[0]["lastname"], target_personal_data[0]["nickname"],
    target_personal_data[0]["birth"][0:2], target_personal_data[0]["birth"][2:4], target_personal_data[0]["birth"][4:8],
    target_personal_data[1]["name"], target_personal_data[1]["lastname"], target_personal_data[1]["nickname"],
    target_personal_data[1]["birth"][0:2], target_personal_data[1]["birth"][2:4], target_personal_data[1]["birth"][4:8],
    target_personal_data[2]["name"], target_personal_data[2]["lastname"], target_personal_data[2]["nickname"],
    target_personal_data[2]["birth"][0:2], target_personal_data[2]["birth"][2:4], target_personal_data[2]["birth"][4:8],
    target_personal_data[3]["name"], target_personal_data[3]["lastname"],
    target_personal_data[3]["birth"][0:2], target_personal_data[3]["birth"][2:4], target_personal_data[3]["birth"][4:8],
    target_personal_data[4][3:], target_personal_data[4][1:2] + target_personal_data[4][3:],
    target_personal_data[5][3:], target_personal_data[5][1:2] + target_personal_data[5][3:]
]
dicfile = open("dictionary.txt", "wt", encoding="utf-8")

for i in range(19):
    for j in range(19):
        if not ((dicdata[i] + dicdata[j]) == ""):
            for jsign in join_signs:
                dicfile.write(dicdata[i].capitalize() + jsign + dicdata[j].capitalize() + "\n")
                dicfile.write(dicdata[i].capitalize() + jsign + dicdata[j].lower() + "\n")
                dicfile.write(dicdata[i].capitalize() + jsign + dicdata[j].upper() + "\n")
                dicfile.write(dicdata[i].lower() + jsign + dicdata[j].capitalize() + "\n")
                dicfile.write(dicdata[i].upper() + jsign + dicdata[j].capitalize() + "\n")
                dicfile.write(dicdata[i].lower() + jsign + dicdata[j].lower() + "\n")
                dicfile.write(dicdata[i].upper() + jsign + dicdata[j].lower() + "\n")
                dicfile.write(dicdata[i].lower() + jsign + dicdata[j].upper() + "\n")
                dicfile.write(dicdata[i].upper() + jsign + dicdata[j].upper() + "\n")

#writing password: MonthYear (Russia += МесяцГод += (VtczwUjl=МесяцГод_Латиницей))

dicfile.close()
print("")
input("Press ENTER to exit")
