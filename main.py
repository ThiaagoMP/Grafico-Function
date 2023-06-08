import matplotlib.pyplot as plot

print('Digite os pontos x que voce deseja criar o gráfico: ')
print('Digite cancelar para parar')

x = []
y = []

while True:
    value = input().lower()
    if value == 'cancelar':
        break
    else:
        x.append(int(value))

print('Digite a função f(x)')

function = input().lower().split("=")[1]

for value in x:
    y.append(eval(function.replace('x', str(value))))

fig, ax = plot.subplots(figsize=(10, 10))
plot.style.use('seaborn')

plot.title('Função: ' + function)
plot.ylabel('y')
plot.xlabel('x')
plot.plot(x, y, marker = 'o')

for x1, y1 in zip(x, y):
    ax.annotate('({}, {})'.format(x1, y1), xy=(x1, y1))

plot.show()
