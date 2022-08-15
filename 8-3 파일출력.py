# read() 함수로 읽기
score_file = open("score.txt", "r", encoding="utf8") # "r" -> 다른 파일에서 읽어온다는 것 의미
print(score_file.read())
score_file.close()

#readline으로 하나씩 읽기
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.readline()) # 한 줄씩 읽음, 밑에 추가하면 다음 내용을 출력
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# while로 나타내기(파일의 내용이 얼마나 있는지 모를때 사용)
score_file = open("score.txt", "r", encoding="utf8")
while True: # 무한루프
    line = score_file.readline() # line이라는 변수 생성
    if not line:
        break     #탈출
    print(line, end = "")  #아니면 계속 출력
score_file.close()

# list로 묶어서 나타내기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # readlines() -> list 형태로 저장
for line in lines:    #list는 for문으로 출력
    print(line, end ="")
score_file.close()