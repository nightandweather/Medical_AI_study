import numpy as np

list_data =[1,2,3]
array = np.array(list_data)

print(array.size)
print(array.dtype)
print(array[2])


# 0부터 10까지 배열 만들기
array1 = np.arange(4)
print(array1)

array2= np.zeros((4,4), dtype=float) # 특정데이터 생성시 각 데이터 0 초기화/ dtype 파라미터 설정
print(array2)

array3 = np.ones((3,3), dtype=str) #dtype str :문자열
print(array3)

#0부터 9까지 랜덤하게 초기화 된 배열 생성
array4 = np.random.randint(0,10,(3,3))
print(array4)

#평균 0, 표편1 표준정규 띄는 배열 (표준정규분포)
array5= np.random.normal(0,1,(3,3))
print(array5)


#데이터 가로축 합치기 : 두개 배열 연달아 붙이기 : concatenate([],[])

array6 = np.array([1,2,3])
# [1,2,3]
array7= np.array([4,5,6])
# [4,5,6]
array8 = np.concatenate([array11, array22])

print(array8)
#[[1,2,3,4,5,6]]
  
# 데이터 세로축 합치기  : concatenate, axis=0

array9= np.arange(4).reshape(1,4) # [1,2,3,4]
array10= np.arange(8).reshape(2,4) # [[1,2,3,4][5,6,7,8]]

print(array9,array10)
array11= np.concatenate([array9,array10], axis=0) [[1,2,3,4][1,2,3,4][5,6,7,8]]
print(array11)


# 배열 형태 바꾸기 : reshape, rotate, 

array12= np.array([1,2,3,4])
array13= array44.reshape((2,2))
print(array55)


# 배열나누기 axis=1: 열기준 분리
array222
left, right = np.split(array222, [2], axis=1)
print(left.shape) # 나뉘어진 좌측 배열확인
print(right.shape)
print("-----")
print(array222)
print(left)
