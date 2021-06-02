def sample(content = "", tags = [], deep = [] ):
    reply_array = []
    for index,tag in enumerate(tags) :
        for _ in range(deep[index])  :
            reply_array.append(f"<{tag}>")

        reverse_array = reversed(reply_array)
        print(reverse_array)
        reply_array.append(content)



    return reply_array 

print(sample(content= "hey man",tags = ['h1','p'], deep = [2,4]))