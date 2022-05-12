import json

# notebook = open("../Python Basics/Python Review.ipynb", "r")
notebook = open("Pandas_Fundamentals.ipynb", "r")

nb_json = json.loads(notebook.read())
cells = nb_json['cells']

id = ""
list_n = 1
sub_list_id = 1

for cell in cells:
    if cell['cell_type'] == 'markdown':
        for line in cell['source']:
            if "# " in line:
                line2 = line.replace("\n","").replace("\r","")#.replace("#","").lstrip()
                line3 = line2.split(" ")
                level = len(line3[0])
                text = " ".join(line3[1:])

                # print(str(level), text)

                if level == 1:
                    print(f'**{text}**')
                    n = 0
                elif level == 2:
                    print(f'{n}. <a href="#{text}">{text}</a>')
                    n += 1
                else:
                    tabs = "\t" * (level - 2)
                    print(f'{tabs}* <a href="#{text}">{text}</a>')

            #     line = line.replace("\n","").replace("\r","").replace("#","").lstrip()
            #     line = f"[{line}](#{id})"

            #     if level == 1:
            #         line = f"{list_n}. " + line
            #         list_n += 1
            #     elif level == 2:
            #         line = "    * " + line

            #     print(line)
            # elif "<a id=" in line:
            #     id = line.split('<a id="')[1].split('"></a>')[0]