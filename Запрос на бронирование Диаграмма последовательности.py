import matplotlib.pyplot as plt  # <- мұны қоспағандықтан қате шыққан

fig2, ax2 = plt.subplots(figsize=(14, 8))

participants = ["Клиент", "Система", "Платежный шлюз", "Администратор", "Подрядчики", "Менеджер"]
x_positions = [0, 3, 6, 9, 12, 15]

# Вертикальные линии участников
for i, p in enumerate(participants):
    ax2.plot([x_positions[i], x_positions[i]], [0, -12], color='black', linestyle='--')
    ax2.text(x_positions[i], 0.5, p, ha="center", va="bottom", fontsize=10, fontweight='bold')

def message(frm, to, y, text, async_msg=False):
    x1 = x_positions[participants.index(frm)]
    x2 = x_positions[participants.index(to)]
    arrow_style = '->'
    linestyle = '--' if async_msg else '-'
    ax2.annotate("", xy=(x2, y), xytext=(x1, y),
                 arrowprops=dict(arrowstyle=arrow_style, linestyle=linestyle, linewidth=1.2))
    ax2.text((x1+x2)/2, y+0.2, text, ha="center", va="bottom", fontsize=9)

# Сообщения процесса бронирования
message("Клиент", "Система", -1, "Запрос доступности")
message("Система", "Клиент", -2, "Информация о доступности")
message("Клиент", "Система", -3, "Подтверждение бронирования")
message("Система", "Платежный шлюз", -4, "Запрос предоплаты")
message("Платежный шлюз", "Система", -5, "Платеж успешен?", async_msg=True)
message("Система", "Клиент", -6, "Подтверждение бронирования")
message("Система", "Администратор", -6, "Уведомление о задаче")
message("Администратор", "Подрядчики", -7, "Задачи для выполнения", async_msg=True)
message("Подрядчики", "Система", -8, "Подтверждение выполнения", async_msg=True)
message("Система", "Менеджер", -9, "Отчет по мероприятию")
message("Система", "Клиент", -10, "Запрос отзывов")
message("Клиент", "Система", -11, "Отзывы")

ax2.set_xlim(-1, 16)
ax2.set_ylim(-12, 1)
ax2.axis('off')
plt.title("Диаграмма последовательности: Бронирование мероприятия", fontsize=14, fontweight='bold')
plt.show()
