#comparing strings
word_1=input("enter The word1:")
word_2=input("enter The word2:")
if word_1>word_2:
    print(word_1)
elif word_2>word_1:
    print(word_2)


#print the greater total value with ascii
name_1=input("enter the name1:")
name_2=input("enter the name2:")
split_name_1=list(name_1)
total_name_1=0
for i in split_name_1:
    num=ord(i)
    total_name_1+=num
split_name_2=list(nme_2)
total_name_2=0
for i in split_name_2:
    num=ord(i)
    total_name_2+=num
if total_name_1>total_name_2:
    print(name_1)
else:
    print(name_2)


#finding Rubstings
#to given the sting last occurance of the sub sting value find()
#if the value not availble returns  -1
word="python is the low level programming launguage"
sub_string="g"
find_substring=word.rfind(sub_string)
print(find_substing)

#with input()
char=input("enter the char:")
substing=input("enter the subString:")
result=char.rfind(subSting)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result = value.rfind(subString,start,end)
print(result)


#join Strings
word="momin"

char="-"

result=char.join(word)
print(result)

element=input("enter the element:")
value=input("enter the value:")
join_val=value.join(element)
print(join_val)

list_a=["nithish","raju","prasad",]
join_word="ohm"
result=join_word.join(list_a)
print(result)

#removing space
word ="this is strip method"
value=word.strip()
print(value)

#particular left said deletion
word ="this is strip method "
value=word.lstrip()
lendth=len(value)
print(value)
print(length)
print(len(word))

#split strins
word="jai balaya"
result=word.split()
print(result)

second_result=word.split("i")
print(second_result)

word_2="m@o@m@i@n"
split_word=word_2.split("@")
print(split_word)

#replacing string
word="Iam king"
replace_word="Monstar"
result=word.replace("king",replace_word)
print(result)




