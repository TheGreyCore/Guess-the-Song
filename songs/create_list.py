from pandas import DataFrame, concat, Series

print("""=====================================================================
Type the name(answer), then type the file name. For exit/break type exit.
PS: "-" replacing with new line!
PS: Max 30 symbols!
=====================================================================""")

playlist = DataFrame(columns=["Names", "Paths"])

while True:
    name = input("Name: ").title()

    if name == "exit":
        break
    elif len(name) > 30:
        print("Max 30 symbols!")
        name = input("Name: ").title()

    filename = input("File name: ")

    user_input = [name, filename]
    playlist.loc[len(playlist)] = user_input

playlist.to_csv("list.csv")

print(f"""Playlist: 
{playlist}""")

