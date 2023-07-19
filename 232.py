# Решение с помощью рекурсии
def f(start,end):
    if start>end or start==12:
        return 0 #Значение, превышающие 21 и равное 12, мы присваем 0 
    if start==end:
        return 1 #Возвращаем 1, чтоб не потерять
    if start<end:
        #Считаем количество путей
        return f(start*2,end)+f(start+1,end)+f(start+3,end)+f(start+10,end)
#Выводим результат на экран
print(f(5,21)) 
