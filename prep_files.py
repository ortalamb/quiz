ques = """\
what color are flowers?
    (a) Blue1
    (b) Red1
    (c) bhhh1 
    (d) njnj1

what is the ans?
    (a) Blue2
    (b) Red1
    (c) bhhh1
    (d) njnj1

who is the prime?
  (a) Blue3
  (b) Red1
  (c) bhhh1
  (d) njnj1
  
what are hggy?
 (a) Blue4
 (b) Red1
 (c) bhhh1
 (d) njnj1
 """

f = open('questions.txt', 'w')
print(ques, file=f)
f.close()

ans = """\
'a'
'b'
'c'
'a'
"""

f = open('answers.txt', 'w')
print(ans, file=f)
f.close()