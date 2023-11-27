#Why we need numpy?Therefore, we have list in python.??????????
#------------------------new learning zip keyword----------------

#problem: 01
'''
Suppose we want to use climate data like the temperature, rainfall, and humidity
to determine if a region is well suited for growing apples.
A simple approach for doing this would be to formulate the relationship
between the annual yield of apples (tons per hectare) and the climatic 
conditions like the average temperature (in degrees Fahrenheit), 
rainfall (in millimeters) & average relative humidity (in percentage) as a linear equation.

yield_of_apples = w1 * temperature + w2 * rainfall + w3 * humidity
'''
kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]
weights = [0.3,0.2,0.5]
def crop(a,b):
    result = 0
    for w,x in zip(a,b):
        result += w * x
    return result

print(f"Expected Yield in kanto reagion: {crop(kanto,weights)} ")
print(f"Expected Yield in johto reagion: {crop(johto,weights)} ")
print(f"Expected Yield in johto reagion: {crop(hoenn,weights)} ")
print(f"Expected Yield in johto reagion: {crop(sinnoh,weights)} ")
print(f"Expected Yield in johto reagion: {crop(unova,weights)} ")


#Going from Python lists to Numpy arrays
import numpy as np

kanto_np =np.array(kanto)
johto_np =np.array(johto)
hoenn_np =np.array(hoenn)
sinnoh_np = np.array(sinnoh)
unova_np=np.array(unova)
weights_np=np.array(weights)
print("we have same result by using dot in numpy: ",end="")
print(np.dot(kanto_np,weights_np))
print(f"element wize multiplication: {kanto_np*weights_np}")
print(f"similarly: {(kanto_np*weights_np).sum()}")


#done the calcuation with more easier: (using matrix multiplicattion:)
print("--------------------matix of all reagion essential informaiton: ----------------")
matrix_all_reagion_info = np.array([kanto,johto,hoenn,sinnoh,unova])
print(matrix_all_reagion_info)
print(matrix_all_reagion_info.shape)
weights_np_array = np.array(weights,ndmin=2).reshape(3,1)
print(weights_np_array)
print("Multiplication : of the both matrix: ")
#similiary we can do with: a @ b (a matrix multiplication)
print(np.matmul(matrix_all_reagion_info,weights_np_array))


#-----------------------------Working with csv file-------------------------------:
#--------------------------------reading data from online source-------------------
print("--------------------------------reading data from online source-------------------")
import urllib.request 
urllib.request.urlretrieve(
    "https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv",
    "climate.txt"
)
climate_online_csv = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)
print(climate_online_csv.shape)
#weights_np_array
ans = np.matmul(climate_online_csv,weights_np_array)
print(ans)
print(ans.shape)

print("--------concatenation: of the array: -------------")
concatenate_ans = np.concatenate((climate_online_csv,ans),axis=1)
np.savetxt('concatenate_ans.txt',
           concatenate_ans,
           fmt='%.2f',
           header='temperature,rainfall,humidity,yield_apple'
           )
