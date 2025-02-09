import pymupdf
from cv import CV
import re
from fake_names import name_list_cv_4

def find_first_number(s):
  match = re.search(r'[1-9]', s)
  if match:
    return match.group()
  return 0

doc = pymupdf.open("CV_LucaTreweller.pdf")
text = ""
for page in doc:
  text = text + page.get_text()
with open("Luca_mapping/fake_experiance_1.txt", "r") as f:
    fake_experiance1 = f.read()
with open("Luca_mapping/fake_experiance_2.txt", "r") as f:
    fake_experiance2 = f.read()
Luca_T = CV(text, ["Luca", "Treweller"], 
            experiance_adaptation=0, experiance=[[(1, 41)], [(1, 41), (32, 33)]], 
            fake_experiance=[[fake_experiance1], [fake_experiance2, "Programmiersprachen: Python, Java, Javascript, C++, C#, R"]])
Luca_T.body = Luca_T.body.replace("19.07.2000 | ", "")

doc2 = pymupdf.open("lebenslauf-englisch-vorlage.pdf")
text2 = ""
for page in doc2:
  text2 = text2 + page.get_text()
Maja_M = CV(text2, ["Maja", "Muster"],
            experiance_adaptation=0, 
            experiance=[[(6, 7), (39, 40), (45, 46), (59, 60), (64, 66), (78, 79), (93, 94), (96, 114), (116, 117), (118, 120), (128, 143)],
                        [(6, 7), (39, 40), (59, 60), (79, 80), (94, 95)]], 
            
            fake_experiance=[
                ["A professional and reliable graphic designer with two years experience in",
                "06/2024 - present",
                "Improving brand reputation and increasing outreach by 17 % in 2024",
                "03/2023 - 04/2024",
                "",
                "02/2022 - 01/2023",
                "10/2019 - 09/2022",
                "",
                "06/2024 - present\n",
                "",
                ""],
                ["A professional and reliable graphic designer with thirty years experience in",
                 "06/1998 - present",
                 "03/1994 - 02/1998",
                 "02/1993 - 01/1994",
                 "10/1990 - 09/1993",
                 ]
               ])

doc3 = pymupdf.open("CV_3.pdf")
text3 = ""
for page in doc3:
  text3 = text3 + page.get_text()
CV_3 = CV(text3, ["Max", "Mustermann"], 
          experiance_adaptation=0, 
          experiance=[[(8, 9), (17, 18), (19, 20), (21, 22), (26, 27), (30, 50), (32, 33), (36, 44)],
                      [(8, 9), (17, 18), (19, 20), (21, 22), (26, 27), (30, 31), (34, 35), (38, 39), (42, 43), (46, 47), (51, 52), (55, 56), (59, 60), (63, 64), (66, 66)]],
          fake_experiance=[
                ["05.02.2008",
                "von 2014-2018",
                "von 2018-2022",
                "von 2022-2023",
                "05/2023",
                "",
                "08/2023 - 03/2025",
                "",
                ],
                ["05.02.1979",
                "von 1985 - 1989",
                "von 1989 - 1994",
                "vor 1994 - 1995",
                "05/1994",
                "03/1997 - 07/1997",
                "11/1998 - 07/1999",
                "02/1999 - 07/1999",
                "08/2000 - 07/2001",
                "08/2003 - 06/2005",
                "08/1995 - 03/1997",
                "09/1997 - 06/2000",
                "08/2001 - 07/2003",
                "BERUFSERFAHRUNG\n07/2005 - 04/2013\nLehrer in Sozialkunde\n\nin der Ostseeschule Flensburg\n04/2013 - 05/2021\nErzieher\n\nan der Städtischen Kindertagesstätte in Flensburg\n05/2021 - Dato\nLeiter\n\nder Städtischen Kindertagesstätte in Flensburg\nKenntnisse"
                ],
               ])

with open("CV_4/CV_4.txt", "r") as f:
  text4 = f.read()
with open("CV_4/fake_experiance1.txt", "r") as f:
   fake_experiance1 = f.read()
with open("CV_4/fake_experiance2.txt", "r") as f:
   fake_experiance2 = f.read()
CV_4 = CV(text4, ["Max", "Mustermann", "Male", "New York"], 
          fake_names=name_list_cv_4,
          experiance_adaptation=0,
          experiance=[[(17, 27),], [(17, 27),]],
          fake_experiance=[[fake_experiance1,], [fake_experiance2]])

