import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Создание фигуры
fig, ax = plt.subplots(figsize=(14, 10))

def activity_block(name, x, y, w=5, h=1.2):
    box = FancyBboxPatch((x, y-h), w, h,
                         boxstyle="round,pad=0.3",
                         linewidth=1.5,
                         edgecolor="black",
                         facecolor="#D9F2D9")
    ax.add_patch(box)
    ax.text(x + w/2, y - h/2, name, ha="center", va="center", fontsize=10, fontweight='bold')
    return (x, y-h, w, h)

def connect_activity(c1, c2, style='-'):
    (x1, y1, w1, h1) = c1
    (x2, y2, w2, h2) = c2
    start = (x1 + w1/2, y1)
    end = (x2 + w2/2, y2 + h2)
    arrow = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=15,
                            linewidth=1.2, linestyle=style)
    ax.add_patch(arrow)

# Блоки действий
start = activity_block("Начало", 5, 18)
req_job = activity_block("Руководитель создает заявку", 5, 16)
hr_check = activity_block("HR проверяет заявку", 5, 14)
approved = activity_block("Заявка утверждена?", 5, 12)
notify_fix = activity_block("Уведомление о доработке", 2, 12)
publish_job = activity_block("Публикация вакансии", 5, 10)
apply_candidates = activity_block("Кандидаты подают заявки", 8, 10)
hr_screen = activity_block("HR проверяет анкеты", 5, 8)
interview = activity_block("Собеседование", 5, 6)
offer = activity_block("Оффер кандидату", 5, 4)
reject = activity_block("Отказ кандидату", 8, 6)
confirm = activity_block("Кандидат подтверждает оффер", 5, 2)
add_db = activity_block("Добавление сотрудника в БД", 5, 0)
notify_it = activity_block("Уведомление IT отдела", 8, 0)
end = activity_block("Конец", 5, -2)

# Соединения стрелками
connect_activity(start, req_job)
connect_activity(req_job, hr_check)
connect_activity(hr_check, approved)
connect_activity(approved, publish_job, style='-')   # если да
connect_activity(approved, notify_fix, style='--')   # если нет
connect_activity(publish_job, apply_candidates)
connect_activity(apply_candidates, hr_screen)
connect_activity(hr_screen, interview)
connect_activity(interview, offer, style='-')   # успешно
connect_activity(interview, reject, style='--')  # провал
connect_activity(offer, confirm)
connect_activity(confirm, add_db)
connect_activity(add_db, notify_it)
connect_activity(notify_it, end)
connect_activity(reject, end)

ax.set_xlim(0, 14)
ax.set_ylim(-3, 20)
ax.axis('off')
plt.title("Диаграмма деятельности: Найм сотрудников", fontsize=14, fontweight='bold')
plt.show()
