import json
from flask import Flask


def json_read():
    with open("candidates.json", "r", encoding='UTF-8') as f:
        list_candidates = json.load(f)
        return list_candidates


# ПЕРВЫЙ ШАГ ДЗ - выводим ВСЁ
def show_all_users(candidates_list):
    """
    Функция принимает список юзеров и возвращает строку со ВСЕМИ пользователями.
    :return:
    """
    candidates_string = ''
    for candidate in candidates_list:
        candidate_str = f'name: {candidate["name"]}\n' \
                        f'position: {candidate["position"]}\n' \
                        f'skills: {candidate["skills"]}\n\n'

        candidates_string += candidate_str
    return candidates_string


def find_user_by_id(candidate_list, user_id):
    """Функция возвращает информацию о юзере по ID"""
    user_string = ""
    for candidate in candidate_list:
        if candidate["id"] == user_id:
            user_string += f'<img src = "{candidate["picture"]}">\n\n' \
                           f'name: {candidate["name"]}\n' \
                           f'position: {candidate["position"]}\n' \
                           f'skills: {candidate["skills"]}\n\n'
            break
    else:
        user_string += "Неправильный ввод ID"
    return user_string


def find_user_by_skills(candidate_list, skills):
    """Функция возвращает информацию о юзере по навыкам(skills)"""
    user_string = ""
    for candidate in candidate_list:
        skill_list = candidate["skills"].lower().split(", ")
        if skills.lower() in skill_list:
            user_string += f'name: {candidate["name"]}\n' \
                           f'position: {candidate["position"]}\n' \
                           f'skills: {candidate["skills"]}\n\n'
    return user_string



# ЗАГРУЗКА ВОПРОСОВ в список
list_candidates = json_read()

# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)


@app.route("/")
def page_index():
    all_candidates = show_all_users(list_candidates)
    return f"<pre>{all_candidates}</pre>"


@app.route("/candidate/<int:id>")
def page_candidate(id):
    return f'<pre>{find_user_by_id(list_candidates, id)}</pre>'


@app.route("/skills/<skill>")
def page_user_skills(skill):
    return f'<pre>{find_user_by_skills(list_candidates, skill)}</pre>'


app.run()
# https://github.com/Kirill-oss67/homework_10
