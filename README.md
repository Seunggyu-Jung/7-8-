# 나도 코딩 파이썬: 8강 입출력 포멧

# 1. 표준 입출력 포멧

- sep = "" : 나누는 ,를 어떻게 나타낼 것인지 표시
- end = "" : ""로 끝내고 밑에 있는 문장을 붙이는데 사용
```
print("python", "Java", sep = ",") 
print("python", "Java", sep = " vs ")

print("python", "Java", sep = ",", end = " ? ") 
print("무엇이 더 재미있을까요?")
-> 
python,Java
python vs Java
python,Java ? 무엇이 더 재미있을까요?
```

- .items() : key, value를 쌍으로 출력
- str() : 정수의 문자화
- ljust() : ()칸 만큼 공간확보 및 왼쪽 정렬
- rjust() : ()칸 만큼 공간확보 및 오른쪽 정렬
```
scores = {"수학":20, "영어":50, "코딩":100}
for subject, score in scores.items():  # key, value를 쌍으로 출력 ->.items()로 출력
    print(subject.ljust(8),str(score).rjust(4), sep = ":")

-> 
수학      :  20
영어      :  50
코딩      : 100
```

- .zfill() : ()수 만큼 0을 넣는다.
```
for num in range(1,21):
    print("대기순번 :" + str(num).zfill(3)
->
대기순번 :001
대기순번 :002
대기순번 :003
...
대기순번 :020
```

- input() : 모든 값을 문자화 시키기 때문에 정수에 str을 따로 할 필요는 없다.
```
answer = input("아무값이나 입력하세요 : ") 
print(answer)
-> 
아무값이나 입력하세요 : 하이
하이
```

# 2. 다양한 포멧 출력
- {0: >10} : 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
```
print("{0: >10}".format(500))
-> 
       500
```

- {0: >+10} : 양수일 땐 +로 표시, 음수일 땐 -로 표시 -> 숫자 앞에 부호 적기
```
print("{0: >+10}".format(+500))
print("{0: >+10}".format(-500))
->
      +500
      -500
```

- {0:_<10} : 왼쪽 정렬하고, 빈칸을 _로 채움
```
print("{0:_<10}".format(500))
->
500_______
```

- {0:,} : 3자리 마다 콤마를 찍어주기
```
print("{0:,}".format(100000000000000))
-> 
100,000,000,000,000
```

- {0:+,} : 3자리 마다 콤마를 찍어주고, +- 부호도 붙이기
```
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))
->
+100,000,000,000,000
-100,000,000,000,000
```

- {0:^<+30,} : 3자리 마다 콤마 찍고, +-부호 붙이고, 나머지 빈칸엔 ^표시, 왼쪽 정렬
```
print("{0:^<+30,}".format(100000000000000))
->
+100,000,000,000,000^^^^^^^^^^
```

- {0:.nf} : 소숫점 n째자리까지만 표시
```
print("{0:.2f}".format(5/3))
->
1.67
```

# 3. 파일생성 및 출력
파일변수생성 -> 변수 = open("파일이름", "파일용도", encoding = "utf8")
파일을 열었으면 항상 닫아야 한다.
- w : 적는 용도
```
score_file = open("score.txt", "w", encoding="utf8") 
print("수학 : 0", file = score_file) 
print("영어 : 50", file = score_file)
score_file.close()
```

- a : 기존파일에 추가하는 용도
- .write() : write()함수로 ()의 값을 적는 것을 의미
```
score_file = open("score.txt", "a", encoding="utf8") 
score_file.write("과학 : 80") # write()  
score_file.write("\n코딩 : 100") # 줄바꿈 \n
score_file.close()
```

- r : 다른 파일에서 읽어온다는 것 의미
```
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.read())
score_file.close()
->
수학 : 0  
영어 : 50 
과학 : 80 
코딩 : 100
```

- .readline() : 한 줄씩 읽음, 밑에 추가하면 한 칸 때고 다음 내용을 출력
```
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.readline()) 
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
->
수학 : 0

영어 : 50

과학 : 80

코딩 : 100
```

- while문으로 나타내기 : 파일의 내용이 얼마나 있는지 모를때 사용
```
score_file = open("score.txt", "r", encoding="utf8")
while True: # 무한루프
    line = score_file.readline() # line이라는 변수 생성
    if not line:
        break     #탈출
    print(line, end = "")  #아니면 계속 출력
score_file.close()
->
수학 : 0
영어 : 50
과학 : 80
코딩 : 100
```

- list로 묶어서 나타내기
```
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # readlines() -> list 형태로 저장
for line in lines:    #list는 for문으로 출력
    print(line, end ="")
score_file.close()
->
수학 : 0
영어 : 50
과학 : 80
코딩 : 100
```

# 4. pickle
pickle을 사용하기 위해 코드 상단에서 import pickle으로 시작

- wb : pickle에서 적는 용도
- .dump(profile,profile_file) : profile에 있는 정보를 file에 저장
```
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이":30 ,"취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile,profile_file) 
profile_file.close()
-> 
{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
```

- rb : pickle에서 파일을 읽는 용도
- .load(profile_file) : file에 있는 정보를 profile에 불러오기
```
import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)   
print(profile)
profile_file.close()
->
{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
```

# 5. with문
- 파일을 간편하게 작성하고 읽고자 할 때 사용
```
with open("study.txt", "w", encoding="utf8") as study_file: # 파일을 간편하게 작성하는 법
    study_file.write("파이썬을 열심히 공부하고 있어요.")

  
with open("study.txt", "r", encoding="utf8") as study_file:  # 파일을 간편하게 읽어오는법
           print(study_file.read())

-> 파이썬을 열심히 공부하고 있어요.
```







