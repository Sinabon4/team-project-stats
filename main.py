import os

# ============================================
# ЛАБОРАТОРНАЯ РАБОТА №3 - Git
# Вариант 2: Анализ курса валют
# Основной аккаунт: Sinabon4
# ============================================

def read_currency_data(filename):
    """
    Читает данные о курсе валют из CSV-файла.
    Возвращает список дат и список курсов.
    """
    dates = []
    rates = []
    
    # Проверяем, существует ли файл
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден!")
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Пропускаем заголовок (первая строка)
    for line in lines[1:]:
        if line.strip():  # пропускаем пустые строки
            parts = line.strip().split(',')
            date = parts[0]
            rate = float(parts[1])
            dates.append(date)
            rates.append(rate)
    
    return dates, rates
# ============================================
# ДОБАВЛЕНО ВТОРЫМ УЧАСТНИКОМ (me000001k)
# Функция для расчёта скользящей средней
# ============================================
def moving_average(data, window_size):
    """
    Вычисляет скользящую среднюю для заданного окна.
    Возвращает список средних значений.
    Автор: me000001k
    """
    if len(data) < window_size:
        return []
    
    result = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / window_size
        result.append(avg)
    
    return result

def main():
    """Основная функция программы"""
    print("=" * 50)
    print("📊 АНАЛИЗ КУРСА ВАЛЮТ")
    print("=" * 50)
    
    filename = "currency_data.txt"
    
    try:
        # Читаем данные
        dates, rates = read_currency_data(filename)
        
        print(f"\n📁 Загружено данных за {len(dates)} дней")
        print(f"📈 Курс: от {min(rates):.2f} до {max(rates):.2f} руб.")
        print(f"📊 Средний курс: {sum(rates)/len(rates):.2f} руб.")
        
        # Показываем таблицу
        print("\n" + "-" * 50)
        print(f"{'Дата':<15} {'Курс (руб.)':<15}")
        print("-" * 50)
        for i in range(len(dates)):
            print(f"{dates[i]:<15} {rates[i]:<15.2f}")
        print("-" * 50)
        
         # ============================================
        # ДОБАВЛЕНО ВТОРЫМ УЧАСТНИКОМ (me000001k)
        # Расчёт скользящей средней и прогноза
        # ============================================
        # Расчёт скользящей средней
        window_size = 5
        print(f"\n📊 СКОЛЬЗЯЩАЯ СРЕДНЯЯ (окно = {window_size} дней):")
                # Расчёт скользящей средней
        window_size = 5
        print(f"\n📊 СКОЛЬЗЯЩАЯ СРЕДНЯЯ (окно = {window_size} дней):")
        print("-" * 50)
        print(f"{'Дата':<15} {'Средняя':<15}")
        print("-" * 50)
        
        avg_values = moving_average(rates, window_size)
        
        if avg_values:
            for i in range(len(avg_values)):
                # Дата для средней - последняя дата в окне
                avg_date = dates[i + window_size - 1]
                print(f"{avg_date:<15} {avg_values[i]:<15.2f}")
            print("-" * 50)
            
            # Прогноз на следующий день
            last_avg = avg_values[-1]
            print(f"\n🔮 ПРОГНОЗ на следующий день: {last_avg:.2f} руб.")
        else:
            print("⚠️ Недостаточно данных для расчёта скользящей средней")
            
    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()