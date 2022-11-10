#list adalah tipe data yang terbentuk dari beberapa objek, dan mendukung ordered baik slicing ataupun indexing
#tuple adalah tipe data yang mendukung ordered ditandai dengan () dan bersifat abadi atau immutable
#set adalah tipe data yang tidak mendukung ordered hanya bisa menggunakan objek dan objeknya harus unik dan ditandai dengan {}
#dictionary adalah tipe data yang mendukung ordered dan tersusun dengan key dan value dan ditandai dengan {}

a = ["1", "13b", "aa1", "1.32", "22.1", "2.34"]
print (a [1:5])
a = [
    [5, 9, 8],
    [0, 0, 6]
]
print (a [1][1:])
a = [
    [5, 9, 8],
    [0, 0, 6]
]
a [0][2]=10
a [1][0]=11
print (a)
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
areas.pop(8)
areas.pop(9)
print (areas)
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
T = S[0::2]
print (T)
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ['itali']= 'roma'
print (europe)
print (8 >= 2 and 3 <= 2)
print (9 > 9 or 'A' != 'a')
print (not 1 > 2) 
A = 40000
if A > 100000:
    print ('high')
elif A > 50000:
    print ('medium')
elif A <= 50000:
    print ('low')