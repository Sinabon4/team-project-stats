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
        
    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()