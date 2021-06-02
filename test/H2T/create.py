

class h2t :
    
    tags = ['h1','p','div']

    def h1(self,content="",inside = False, tag = [],inside_content = ""):
        if not inside :
            return f"<h1>{content}</h1>"

        if isinstance(tag, list) :
            all_the_text = []
            ''' taking the whole list and matching it with the predefined list of the class to avoid errors '''
            for index,i_tag in enumerate(tag) :
                if i_tag in self.tags  :

                    #appending all the tags to an array 
                    all_the_text.append(self.search_tag(i_tag,inside_content[index]))

            return "<h1>{}</h1>".format("\n".join(all_the_text))
        return "oops"       
            

    def deeph1(self,content = " ",tag =[], deep = []) :
        if isinstance(tag, list) and isinstance(deep, list) :
            pass      

    def search_tag(self,tag_name,inside_content) :
        if tag_name == "h1" :
            return self.h1(content=inside_content)
        elif tag_name == "p" :
            pass
        elif tag_name == "div":
            pass
        else :
            raise Exception("Invalid entry ")                

    def checking(self, sam,dam):
        print(sam)
        dam(sam)


class sam :
    def assam(self,sar ="",sim = "") :
        print(sar)
        print("this is sim : ",sim)

jock = h2t()

print(jock.h1(content="sssss",inside= True, tag=["h1","h1"],inside_content=["test","traigning"]))
