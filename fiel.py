def target_string(filename, target):

    try:
        fh = open(filename, "r+")
        gh = fh.read()
        lis = gh.split()

    except Exception as a:
        print(a)
    finally:
        count = 0
        for i in lis:
            if i == target:
                count = count + 1
        print(count)
        print("the list of words in the file")
        print(lis)
        fh.close()


target_string("example.txt", "line")
