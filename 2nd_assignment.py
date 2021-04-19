
import numpy as np #numpy 모듈 불러오기


# numpy 객체 Save&Load
array = np.arange(0, 10)
print(array)
#[0,1,2,3,4,5,6,7,8,9]
np.save('saved.npy', array) # array 객체 저장
#in directory

result = np.load('saved.npy') # array 객체 로드
print(result)

# numpy 다수의 객체 Save&Load
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1, array2=array2) # 다수의 array 객체 저장

#npy, npz difference 
# https://stackoverflow.com/questions/54238670/what-is-the-advantage-of-saving-npz-files-instead-of-npy-in-python-regard


data = np.load('saved.npz') # npz파일 로드
result1 = data['array1'] # npz파일의 arrya1 객체
result2 = data['array2'] # npz파일의 arrya2 객체
print(result1)
print(result2)

# numpy array 원소 오름차순 정렬
array = np.array([3, 10, 15, 7, 32])
array.sort()
print(array)

# numpy array 원소 내림차순 정렬
array = np.array([3, 10, 15, 7, 32])
array.sort()
print(array[::-1])

## sort, natsort difference
# https://mentha2.tistory.com/171


# 행,열을 기준으로 정렬
array = np.array([[7, 10, 22, 4, 11], [87, 5, 10, 40, 9]])
array.sort(axis=0) # 열을 기준으로 정렬
print(array)
array.sort(axis=1) #행을 기준으로 정렬
print(array)

# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 2) # 0부터 10사이의 5개 데이터를 균일하게 뽑아 array 생성
print(array)

# 난수 생성과 시드
np.random.seed(7) # 시드값 적용
print(np.random.randint(0, 10, (2, 3)))

# numpy 객체 복사
array1 = np.arange(0, 10)
array2 = array1.copy()
print(array2)

# 중복된 원소 제거
array = np.array([1, 1, 2, 3, 3, 3, 1])
print(np.unique(array))
