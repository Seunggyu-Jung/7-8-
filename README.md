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

