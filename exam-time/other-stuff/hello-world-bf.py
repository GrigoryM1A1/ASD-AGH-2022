def hello_world():
    res = ""
    Dictionary = "abcdefghijklmnopqrstuvwxyz "
    word = "hello world"
    length = 0
    while length < 11:
        for i in range(len(Dictionary)):
            print(Dictionary[i])
            if Dictionary[i] == word[length]:
                res += Dictionary[i]
                length += 1
                print(res)
                break
    print(res)


hello_world()
