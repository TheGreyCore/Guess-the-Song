from pandas import DataFrame

print("""=====================================================================
Type name(answer), then type filename. For exit/break type exit.
=====================================================================""")

dict_playlist = {}

while True:
    name = input("Name: ").lower()

    if name == "exit":
        break

    path = input("Filepath: ")

    dict_playlist[name] = f"songs/{path}"

playlist = DataFrame(dict_playlist, index=[0])
playlist.to_csv("list.csv")

print(f"""Playlist: 
{playlist}""")
