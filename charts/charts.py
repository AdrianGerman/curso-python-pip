import matplotlib.pyplot as plt


def generate_pie_chart():
    # estos son los nombres que se mostraran en las gráficas
    labels = ['A', 'B', 'C']
    # estos son los valores de las gráficas
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('charts/img/pie.png')
    plt.close()