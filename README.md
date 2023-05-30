# Process_of_Puasson-s

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Arial+Black&weight=800&size=30&pause=1000&color=F70000&center=true&vCenter=true&width=800&height=100&lines=Puasson's)](https://git.io/typing-svg)


<p align="center">
  <img src="myplot.png" alt="Puasson's">
</p>

<div>
<h1>Процес Пуассона</h1>
<p>Код створює об'єктно-орієнтовану реалізацію процесу Пуассона в Python і 
використовує matplotlib для візуалізації отриманих траєкторій.</p>


<h2>Імпорт необхідних бібліотек:</h2>

<p>Numpy використовується для генерації випадкових чисел із відповідних розподілів.
matplotlib.pyplot використовується для створення графіків. mplcyberpunk використовується для застосування кіберпанкового стилю до графіків.</p>

<h2>Клас PoissonProcess</h2>
<p>Клас PoissonProcess створюється з двома методами:</p>

<p>Конструктор __init__ приймає інтенсивність intensity та граничний час T для процесу Пуассона.
Метод generate_trajectory генерує траєкторію процесу Пуассона відповідно до вказаної інтенсивності і граничного часу.
Функція plot_trajectories приймає список траєкторій процесів Пуассона і список відповідних міток і візуалізує кожну траєкторію на окремому підграфіку.</p>

<p>В блоку if __name__ == "__main__":</p>

<p>Визначаються значення інтенсивності (lambdas) і граничний час (T).
За кожним значенням інтенсивності створюється об'єкт PoissonProcess і генеруються дві траєкторії, які зберігаються в списку trajectories.
Створюється список міток labels для кожного процесу Пуассона.
Викликається функція plot_trajectories для візуалізації траєкторій.</p>

</div>

