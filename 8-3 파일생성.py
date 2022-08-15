# 파일 생성순서: 1. 파일변수생성 -> 변수 = open("파일이름", "파일용도", encoding = "utf8")  
score_file = open("score.txt", "w", encoding="utf8") # w는 적는 용도라는 것을 의미
print("수학 : 0", file = score_file) # print("넣을 내용", file = 파일변수)
print("영어 : 50", file = score_file)
score_file.close() # 파일을 열었으면 항상 닫아야 한다.

score_file = open("score.txt", "a", encoding="utf8") # a는 기존파일에 추가로 적는 용도라는 것을 의미
score_file.write("과학 : 80") # write() -> write()함수로 ()의 값을 적는 것을 의미 
score_file.write("\n코딩 : 100") # 줄바꿈 \n
score_file.close() 




