import matplotlib.pyplot as plt
import streamlit as st

def fun():
    with open('data.csv') as file:
        file.readline()
        count_do_30_0 = 0
        count_do_30_all = 0
        count_do_30_60_0 = 0
        count_d0_30_60_all = 0
        count_60_0 = 0
        count_60_all = 0
        for line in file.readlines():
            data = line.split(',')
            if data[1] == '' or data[6] == '':
                continue
            survived = data[1]
            age = float(data[6])
            if age <= 30:
                count_do_30_all += 1
                if survived == '0':
                    count_do_30_0 += 1
            if age > 30 and age < 60:
                count_d0_30_60_all += 1
                if survived == '0':
                    count_do_30_60_0 += 1
            if age >= 60:
                count_60_all += 1
                if survived == '0':
                    count_60_0 += 1
    return count_do_30_0 / count_do_30_all, count_do_30_60_0 / count_d0_30_60_all, count_60_0 / count_60_all


val1, val2, val3 = fun()
print('Доля погибших в группе до 30 лет:', val1)
print('Доля погибших в группе старше 30 и меньше 60:', val2)
print('Доля погибших в группе старше 60 лет:', val3)

def var11_main():
    st.title('Пассажиры Титаника ')
    st.image('f.png')
    st.header('Доля погибших и спасенных пассажиров')
    st.subheader('Возрастная категория')
    st.markdown('1. «молодой» (до 30 лет)\n'
                '2. «среднего возраста» (от 30 до 60)\n'
                '3. «старый» (более 60 лет)\n')
    st.write('Чтобы узнать долю выживших в определенной возратной категории, выберите возраст')
    choise = selectbox('Выберете возраст:',
                   ["до 30 лет",
                       "от 30 до 60 лет",
                       "старше 60 лет"])
    x = ['до 30', 'от 30 до 60', 'от 60']
    y = [val1, val2, val3]
    st.tab = {'Возраст пассажиров': x, 'Доля погибших пассажиров': y}
    dataframe(tab)

    fig = plt.figure(figsize=[10, 5])
    plt.bar(x, y)
    plt.xlabel('Возраст пассажиров')
    plt.ylabel('Доля погибших пассажиров')
    plt.title('Диаграмма')
    plt.legend()
    pyplot(fig)
    var11_main()
