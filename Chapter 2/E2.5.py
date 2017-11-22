import array
symbols = "!@#$%^&*"
#print(tuple(ord(symbol) for symbol in symbols))
#print(array.array('I',(ord(symbol)for symbol in symbols)))
lax_coordinates=(33.9425,-118.408056)
city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)
traverler_ids=[('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
# for passport in sorted(traverler_ids):
#     print('%s/%s'%passport)
# for country,_ in traverler_ids:
#     print(country)
# for _,id in traverler_ids:
#     print(id)
latitude,longitude=lax_coordinates
print(latitude)
print(longitude)
print(divmod(20,8))
t = (20,8)
print(divmod(*t))