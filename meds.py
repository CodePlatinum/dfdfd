import customtkinter as ctk


root = ctk.CTk()
root.title("Ліками")
root.geometry("350x200")


medications = {
    "Грип": "Парацетамол, Терафлю, Ібупрофен",
    "Застуда": "Фармазолін, Колдрекс, Вітамін C",
    "Біль у горлі": "Стрепсілс, Лізобакт, Тантум Верде",
    "Головний біль": "Ібупрофен, Цитрамон, Но-шпа",
    "Жар": "Парацетамол, Ібупрофен, Аспірин"
}


def show_medications():
    illness = illness_var.get()
    meds = medications.get(illness, "Немає інформації")
    result_label.configure(text=f"Рекомендовані ліки: {meds}")


illness_var = ctk.StringVar()
illness_menu = ctk.CTkOptionMenu(root, values=list(medications.keys()), variable=illness_var)
illness_menu.pack(pady=10)


findmeds_button = ctk.CTkButton(root, text="Дізнатися ліки", command=show_medications)
findmeds_button.pack(pady=10)


result_label = ctk.CTkLabel(root, text="Оберіть захворювання")
result_label.pack(pady=10)


root.mainloop()
