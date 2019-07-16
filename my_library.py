print("welcome to library")
fiction={"A":"Comedy","B":"Graphics/novel","C":"Science fiction","D":"fantasy","E":"history fiction"}
non_fiction={"F":"History and geography","G":"Arts","H":"science and Technology","I":"othes"}
library=int(input("Enter 1 for fiction or 2 for Non-fiction"))
if library==1:
    print("fiction")
    print("A:for Comedy")
    print("B:for Graphics/Novel")
    print("C: for Science fiction")
    print("D: for Fantasy")
    print("E: for History Fiction")
    genre=input("Enter your choice ")
    genre=genre.upper()
    for i,j in fiction.items():
        if genre==i:
            print("you have choosen ", j, "book", "locationis in", i, "shelf")

if library==2:
    print("Non-fiction section")
    print("F:for History and Geography")
    print("G: for Arts")
    print("H: for Science And Technology")
    print("I:for other")
    genre = input("Enter your choice ")
    genre = genre.upper()
    for i, j in non_fiction.items():
        if genre == i:
            print("you have choosen ",j,"book", "locationis in",i, "shelf")

