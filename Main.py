import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class Add_en():
    def __init__(self):
        def add_to_db():
            name = name_entry.get()
            address = address_entry.get()
            phone = phone_entry.get()

            # Установка соединения с базой данных MySQL
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='22345267',
                database='loan_db'
            )

            # Создание курсора для выполнения SQL-запросов
            cursor = conn.cursor()

            # Выполнение SQL-запроса для добавления данных в таблицу legal_entities
            cursor.execute(
                "INSERT INTO legal_entities (en_name, address, phone_number) "
                "VALUES (%s, %s, %s)",
                (name, address, phone))

            # Применение изменений
            conn.commit()

            def call_update(self):
                self.update_object.update_treeview()

            # Закрытие соединения с базой данных
            conn.close()

            messagebox.showinfo("Добавление.", "Запись занесена в базу данных.")


        entitie_add = Tk()
        entitie_add.title("Добавление юр. лица.")
        entitie_add['bg'] = '#fafafa'
        entitie_add.geometry('350x230')
        entitie_add.resizable(width=False, height=False)

        name_label = Label(entitie_add, text="Название", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        name_label.pack()
        name_entry = Entry(entitie_add)
        name_entry.pack()

        address_label = Label(entitie_add, text="Адрес", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        address_label.pack()
        address_entry = Entry(entitie_add)
        address_entry.pack()

        phone_label = Label(entitie_add, text="Номер телефона", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        phone_label.pack()
        phone_entry = Entry(entitie_add)
        phone_entry.pack()

        add_button = Button(entitie_add, text="Добавить в базу данных", command=add_to_db)
        add_button.pack(padx=10, pady=8)


class Add_lo():
    def __init__(self):
        def add_to_db():
            en_id = en_id_entry.get()
            amount = amount_entry.get()
            percent = percent_entry.get()
            term = term_entry.get()

            # Установка соединения с базой данных MySQL
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='22345267',
                database='loan_db'
            )

            # Создание курсора для выполнения SQL-запросов
            cursor = conn.cursor()

            # Операция проверк исуществования клиента
            cursor.execute("SELECT COUNT(*) FROM legal_entities WHERE entitie_id = %s", (en_id,))
            client_exists = cursor.fetchone()[0]

            if client_exists == 0:
                messagebox.showerror("Ошибка", "Клиент с указанным ID не существует.")

            else:
                # Выполнение SQL-запроса для добавления данных в таблицу legal_entities
                cursor.execute(
                    "INSERT INTO loans (entitie_id, amount, percent, term)"
                    "VALUES (%s, %s, %s, %s)",
                    (en_id, amount, percent, term))

                messagebox.showinfo("Добавление.", "Запись занесена в базу данных.")

            # Применение изменений
            conn.commit()

            # Закрытие соединения с базой данных
            conn.close()

        loan_add = Tk()
        loan_add.title("Добавление кредита.")
        loan_add['bg'] = '#fafafa'
        loan_add.geometry('350x300')
        loan_add.resizable(width=False, height=False)

        en_id_label = Label(loan_add, text="ID лица", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        en_id_label.pack()
        en_id_entry = Entry(loan_add)
        en_id_entry.pack()

        amount_label = Label(loan_add, text="Сумма", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        amount_label.pack()
        amount_entry = Entry(loan_add)
        amount_entry.pack()

        percent_label = Label(loan_add, text="Процент", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        percent_label.pack()
        percent_entry = Entry(loan_add)
        percent_entry.pack()

        term_label = Label(loan_add, text="Срок", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
        term_label.pack()
        term_entry = Entry(loan_add)
        term_entry.pack()

        add_button = Button(loan_add, text="Добавить в базу данных", command=add_to_db)
        add_button.pack(padx=10, pady=8)

class Show():
    def __init__(self):
        def open_lo_add():
            open = Add_lo()

        def open_en_add():
            open = Add_en()

        def update_treeview():
            table1.delete(*table1.get_children())
            table2.delete(*table2.get_children())

            # Установка соединения с базой данных MySQL
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='22345267',
                database='loan_db'
            )

            # Создание объекта cursor для выполнения SQL-запросов
            cursor1 = conn.cursor()

            # Выполнение SQL-запроса для выборки записей из таблицы
            cursor1.execute("SELECT * FROM legal_entities")

            # Получение всех выбранных записей
            en_lst_upd = cursor1.fetchall()

            # Создание объекта cursor для выполнения SQL-запросов
            cursor2 = conn.cursor()

            # Выполнение SQL-запроса для выборки записей из таблицы
            cursor2.execute("SELECT * FROM loans")

            # Получение всех выбранных записей
            lo_lst_upd = cursor2.fetchall()

            # Закрытие соединения с базой данных
            conn.close()

            for row in lo_lst_upd:
                table2.insert('', tkinter.END, values=row)

            for row in en_lst_upd:
                table1.insert('', tkinter.END, values=row)

        def search_en():
            search_value = en_searchfield.get()

            if search_value == '':
                messagebox.showerror(title='Ошибка', message='Поле должнобыть заполнено для поиска, изменения или удаления.')

            else:
                # Установка соединения с базой данных MySQL
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='22345267',
                    database='loan_db'
                )

                # Создание объекта cursor для выполнения SQL-запросов
                cursor = conn.cursor()

                query = "SELECT * FROM legal_entities WHERE entitie_id LIKE %s OR en_name LIKE %s OR address LIKE %s OR phone_number LIKE %s"
                cursor.execute(query, (
                    '%' + search_value + '%', '%' + search_value + '%', '%' + search_value + '%',
                    '%' + search_value + '%'))

                # Получение всех выбранных записей
                serched_en = cursor.fetchall()
                if serched_en == []:
                    messagebox.showinfo(title='Результат', message='Записи с такими данными не найдено.')

                else:
                    # Закрытие соединения с базой данных
                    conn.close()

                    table1.delete(*table1.get_children())

                    for row in serched_en:
                        table1.insert('', tkinter.END, values=row)

        def search_lo():
            search_value = lo_searchfield.get()

            if search_value == '':
                messagebox.showerror(title='Ошибка', message='Поле должнобыть заполнено для поиска, изменения или удаления.')
            else:
                # Установка соединения с базой данных MySQL
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='22345267',
                    database='loan_db'
                )

                # Создание объекта cursor для выполнения SQL-запросов
                cursor = conn.cursor()

                query = "SELECT * FROM loans WHERE loan_id LIKE %s OR entitie_id LIKE %s"
                cursor.execute(query, (
                '%' + search_value + '%', '%' + search_value + '%'))

                # Получение всех выбранных записей
                serched_lo = cursor.fetchall()

                # Закрытие соединения с базой данных
                conn.close()

                if serched_lo == []:
                    messagebox.showinfo(title='Результат', message='Записи с такими ID не найдено.')
                else:
                    table2.delete(*table2.get_children())

                    for row in serched_lo:
                        table2.insert('', tkinter.END, values=row)

        def delete_en():
            selected_items = table1.selection()

            if not selected_items:
                messagebox.showwarning("Предупреждение", "Пожалуйста, выберите элемент для удаления.")
                return  # Прерываем выполнение функции, если элемент не выбран

            selected_item = table1.selection()[0]
            item_values = table1.item(selected_item)["values"]
            en_id = item_values[0]

            responce = messagebox.askyesno(title='Подтверждение', message='Вы действительно хотите удалить запись?')
            if responce:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='22345267',
                    database='loan_db'
                )

                cursor = conn.cursor()

                # Выполнение SQL-запроса для удаления записи из таблицы
                command = "DELETE FROM legal_entities WHERE entitie_id = %s"
                cursor.execute(command, (en_id,))

                # Применяем изменения
                conn.commit()

                # Закрытие соединения с базой данных
                conn.close()

                messagebox.showinfo("Удаление", "Запись успешно удалена.")

                update_treeview()
            else:
                # Код, который нужно выполнить, если пользователь отказался от удаления
                messagebox.showinfo("Удаление", "Удаление отменено.")

        def delete_lo():
            selected_items = table2.selection()

            if not selected_items:
                messagebox.showwarning("Предупреждение", "Пожалуйста, выберите элемент для удаления.")
                return  # Прерываем выполнение функции, если элемент не выбран

            selected_item = table2.selection()[0]
            item_values = table2.item(selected_item)["values"]
            lo_id = item_values[0]

            responce = messagebox.askyesno(title='Подтверждение', message='Вы действительно хотите удалить запись?')
            if responce:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='22345267',
                    database='loan_db'
                )

                cursor = conn.cursor()

                # Выполнение SQL-запроса для удаления записи из таблицы
                command = "DELETE FROM loans WHERE loan_id = %s"
                cursor.execute(command, (lo_id,))

                # Применяем изменения
                conn.commit()

                # Закрытие соединения с базой данных
                conn.close()

                messagebox.showinfo("Удаление", "Запись успешно удалена.")

                update_treeview()
            else:
                # Код, который нужно выполнить, если пользователь отказался от удаления
                messagebox.showinfo("Удаление", "Удаление отменено.")

        def update_en():
            selected_items = table1.selection()

            if not selected_items:
                messagebox.showwarning("Предупреждение", "Пожалуйста, выберите элемент для изменеия.")
                return  # Прерываем выполнение функции, если элемент не выбран

            selected_item = table1.selection()[0]

            item_values = table1.item(selected_item)["values"]
            en_id = item_values[0]
            en_name = item_values[1]
            en_address = item_values[2]
            en_phone = item_values[3]

            def update():
                    responce = messagebox.askyesno(title='Подтверждение', message='Вы действительно хотите изменить запись?')
                    if responce:
                        upd_name = name_entry.get()
                        upd_address = address_entry.get()
                        upd_phone = phone_entry.get()

                        # Установка соединения с базой данных MySQL
                        conn = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='22345267',
                            database='loan_db'
                        )

                        # Создание курсора для выполнения SQL-запросов
                        cursor1 = conn.cursor()

                        # Выполнение SQL-запроса для удаления записи из таблицы
                        command = "UPDATE legal_entities SET en_name = %s, address = %s, phone_number = %s WHERE entitie_id = %s"
                        cursor1.execute(command, (upd_name, upd_address, upd_phone,  en_id,))

                        # Применение изменений
                        conn.commit()

                        conn.close()

                        messagebox.showinfo("Изменение.", "Запись успешно обновлена.")

                        update_treeview()

                        entitie_upd.destroy()

            entitie_upd = Tk()
            entitie_upd.title("Изменение юр. лица.")
            entitie_upd['bg'] = '#fafafa'
            entitie_upd.geometry('350x230')
            entitie_upd.resizable(width=False, height=False)

            name_label = Label(entitie_upd, text="Название", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            name_label.pack()
            name_entry = Entry(entitie_upd)
            name_entry.pack()
            name_entry.insert(0, en_name)

            address_label = Label(entitie_upd, text="Адрес", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            address_label.pack()
            address_entry = Entry(entitie_upd)
            address_entry.pack()
            address_entry.insert(0, en_address)

            phone_label = Label(entitie_upd, text="Номер телефона", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            phone_label.pack()
            phone_entry = Entry(entitie_upd)
            phone_entry.pack()
            phone_entry.insert(0, en_phone)

            add_button = Button(entitie_upd, text="Обновить", command=update)
            add_button.pack(padx=10, pady=8)

        def update_lo():
            selected_items = table2.selection()

            if not selected_items:
                messagebox.showwarning("Предупреждение", "Пожалуйста, выберите элемент для изменеия.")
                return  # Прерываем выполнение функции, если элемент не выбран

            selected_item = table2.selection()[0]

            item_values = table2.item(selected_item)["values"]
            lo_id = item_values[0]
            en_id = item_values[1]
            amount = item_values[2]
            percent = item_values[3]
            term = item_values[4]

            def update():
                    upd_en_id = en_id_entry.get()
                    upd_amount = amount_entry.get()
                    upd_percent = percent_entry.get()
                    upd_term = term_entry.get()

                    # Установка соединения с базой данных MySQL
                    conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='22345267',
                        database='loan_db'
                    )

                    # Создание курсора для выполнения SQL-запросов
                    cursor1 = conn.cursor()

                    # Операция проверк исуществования клиента
                    cursor1.execute("SELECT COUNT(*) FROM legal_entities WHERE entitie_id = %s", (upd_en_id,))
                    client_exists = cursor1.fetchone()[0]

                    if client_exists == 0:
                        messagebox.showerror("Ошибка", "Клиент с указанным ID не существует.")

                    else:
                        responce = messagebox.askyesno(title='Подтверждение', message='Вы действительно хотите изменить запись?')
                        if responce:
                            # Выполнение SQL-запроса для удаления записи из таблицы
                            command = ("UPDATE loans SET entitie_id = %s, amount = %s, percent = %s, term = %s WHERE loan_id = %s")
                            cursor1.execute(command, (upd_en_id, upd_amount, upd_percent, upd_term, lo_id))

                            messagebox.showinfo("Изменение.", "Запись успешно обновлена.")

                            loan_upd.destroy()

                        # Применение изменений
                        conn.commit()

                        update_treeview()

                        # Закрытие соединения с базой данных
                        conn.close()

            loan_upd = Tk()
            loan_upd.title("Изменение кредита.")
            loan_upd['bg'] = '#fafafa'
            loan_upd.geometry('350x300')
            loan_upd.resizable(width=False, height=False)

            en_id_label = Label(loan_upd, text="ID лица", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            en_id_label.pack()
            en_id_entry = Entry(loan_upd)
            en_id_entry.pack()
            en_id_entry.insert(0, en_id)

            amount_label = Label(loan_upd, text="Сумма", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            amount_label.pack()
            amount_entry = Entry(loan_upd)
            amount_entry.pack()
            amount_entry.insert(0, amount)

            percent_label = Label(loan_upd, text="Процент", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            percent_label.pack()
            percent_entry = Entry(loan_upd)
            percent_entry.pack()
            percent_entry.insert(0, percent)

            term_label = Label(loan_upd, text="Срок", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
            term_label.pack()
            term_entry = Entry(loan_upd)
            term_entry.pack()
            term_entry.insert(0, term)

            add_button = Button(loan_upd, text="Обновить", command=update)
            add_button.pack(padx=10, pady=8)

        show = Tk()
        show.title("Просмотр записей.")
        show['bg'] = '#fafafa'
        show.geometry('800x350')
        show.resizable(width=False, height=False)

        tab_control = ttk.Notebook(show)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Лица')
        tab_control.add(tab2, text='Кредиты')

        lb1 = Label(tab1, text='Лица', font='Arial 12 bold')
        lb1.grid(column=0, row=0, padx=8, pady=8)

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='22345267',
            database='loan_db'
        )

        # Создание объекта cursor для выполнения SQL-запросов
        cursor = conn.cursor()

        # Выполнение SQL-запроса для выборки записей из таблицы
        cursor.execute("SELECT * FROM legal_entities")

        # Получение всех выбранных записей
        en_lst = cursor.fetchall()

        heads = ['id', 'name', 'address', 'phone number']
        table1 = ttk.Treeview(tab1, show='headings')
        table1['columns'] = heads
        for row  in en_lst:
            table1.insert('', tkinter.END, values=row)
        for header in heads:
            table1.heading(header, text=header, anchor='center')
            table1.column(header, anchor='center')
        table1.column('id', stretch=NO, width= 50)
        table1.column('name', stretch=NO, width=120)
        table1.column('address', stretch=NO, width=200)
        table1.column('phone number', stretch=NO, width=120)
        table1.grid(column=0, row=1, padx=8, pady=8)

        open_en_add = Button(tab1, text='Добавить', command=open_en_add)
        open_en_add.grid(column=1, row=1, padx=8, pady=8)
        en_del = Button(tab1, text='Удалить', command=delete_en)
        en_del.grid(column=3, row=1, padx=8, pady=8)
        en_change = Button(tab1, text='Изменить',command=update_en)
        en_change.grid(column=2, row=1, padx=8, pady=8)
        en_update = Button(tab1, text='Обновить', command=update_treeview)
        en_update.grid(column=1, row=2, padx=8, pady=8)
        en_searchfield = Entry(tab1)
        en_searchfield.grid(column=2, row=2, padx=8, pady=8)
        en_searchbutton = Button(tab1, text='Поиск', command=search_en)
        en_searchbutton.grid(column=3, row=2, padx=8, pady=8)

        lb2 = Label(tab2, text='Кредиты', font='Arial 12 bold')
        lb2.grid(column=0, row=0, padx=8, pady=8)

        # Создание объекта cursor для выполнения SQL-запросов
        cursor = conn.cursor()

        # Выполнение SQL-запроса для выборки записей из таблицы
        cursor.execute("SELECT * FROM loans")

        # Получение всех выбранных записей
        lo_lst = cursor.fetchall()

        heads = ['loan id', 'entitie id', 'amount', 'percent', 'term']
        table2 = ttk.Treeview(tab2, show='headings')
        table2['columns'] = heads
        for row in lo_lst:
            table2.insert('', tkinter.END, values=row)
        for header in heads:
            table2.heading(header, text=header, anchor='center')
            table2.column(header, anchor='center')
        table2.column('loan id', stretch=NO, width=70)
        table2.column('entitie id', stretch=NO, width=70)
        table2.column('amount', stretch=NO, width=150)
        table2.column('percent', stretch=NO, width=70)
        table2.column('term', stretch=NO, width=120)
        table2.grid(column=0, row=1, padx=8, pady=8)

        open_lo_add = Button(tab2, text='Добавить', command=open_lo_add)
        open_lo_add.grid(column=1, row=1, padx=8, pady=8)
        lo_change = Button(tab2, text='Изменить', command=update_lo)
        lo_change.grid(column=2, row=1, padx=8, pady=8)
        lo_del = Button(tab2, text='Удалить', command=delete_lo)
        lo_del.grid(column=3, row=1, padx=8, pady=8)
        lo_update = Button(tab2, text='Обновить', command=update_treeview)
        lo_update.grid(column=1, row=2, padx=8, pady=8)
        lo_searchfield = Entry(tab2)
        lo_searchfield.grid(column=2, row=2, padx=8, pady=8)
        lo_searchbutton = Button(tab2, text='Поиск', command=search_lo)
        lo_searchbutton.grid(column=3, row=2, padx=8, pady=8)

        tab_control.pack(expand=1, fill='both')


def login():
    username = login_entry.get()
    password = password_entry.get()

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='22345267',
        database='loan_db'
    )

    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM employees WHERE login = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        # Успешная авторизация
        messagebox.showinfo("Успех", "Авторизация успешна!")
        show = Show()
        root.destroy()
    else:
        # Неверный логин или пароль
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")

root = Tk()
root.title("Авторизация.")
root['bg'] = '#fafafa'
root.geometry('450x200')
root.resizable(width=False, height=False)

main_label = Label(root, text='Авторизация', font='Arial 15 bold', bg='#fafafa')
main_label.pack()

login_label = Label(root, text="Логин", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
login_label.pack()

login_entry = Entry(root, bg='#fafafa', font='arial 12')
login_entry.pack()

password_label = Label(root, text="Пароль", font='Arial 11 bold', bg='#fafafa', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root, show="*", bg='#fafafa', font='arial 12')
password_entry.pack()

login_button = Button(root, text="Войти", command=login)
login_button.pack(padx=10, pady=8)

root.mainloop()


