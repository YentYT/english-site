import datetime
import math
from googletrans import Translator
from flask import Flask, render_template, request, url_for, session, redirect
app = Flask(__name__)
app.secret_key = 'asdfgh'
data = [{'title': 'city', 'content': 'There are 300000 of people live in this city', 'time':datetime.datetime.now() }, {'title': 'country', 'content': 'There are fifty million of people in this country', 'time': datetime.datetime.now()}, {'title': 'army', 'content': 'There are one million of people in army', 'time': datetime.datetime.now()}]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/news')
def news():
    data.append({'title': 'economy', 'content': 'the dollar rate fell to 60', 'time': datetime.datetime.now()})
    data[0]['content'] = 'Population of city grew to 400000'
    d = sorted(data, key=lambda x: x['time'], reverse=True)
    return render_template('news.html', news=d)
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username1 = request.form['username']
        password1 = request.form['password']
        level1 = request.form['level']
        session['username'] = username1
        session['password'] = password1
        session['level'] = level1
        return redirect(url_for('profile'))
    return render_template('register.html')
@app.route('/profile')
def profile():
    if 'username' and 'level' and 'password' in session:
        username1 = session['username']
        password1 = session['password']
        level1 = session['level']
        return render_template('profile.html', username=username1, level=level1, password=password1)
    else:
        return redirect(url_for('register'))
@app.route('/program')
def program():
    return render_template('program.html')
@app.route('/avprogram')
def av_program():
    return render_template('avprogram.html')
@app.route('/highprogram')
def high_program():
    return render_template('highprogram.html')
@app.route('/text')
def text():
    return render_template('text.html')
@app.route('/hightext')
def high_text():
    return render_template('hightext.html')
@app.route('/middletext')
def middle_text():
    return render_template('middle.html')
@app.route('/film')
def film():
    return render_template('film.html')
@app.route('/avfilm')
def av_film():
    return render_template('avfilm.html')
@app.route('/highfilm')
def high_film():
    return render_template('highfilm.html')
@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'POST':
        tail1 = request.form['tail']
        cow1 = request.form['cow']
        window1 = request.form['window']
        degree1 = 'новичок'
        degree2 = 'средний'
        degree3 = 'продвинутый'
        if tail1.lower() == 'хвост' and cow1.lower() == 'корова' and window1.lower() == 'окно':
            return render_template('result.html', level = degree3)
        elif tail1.lower() == 'хвост' and cow1.lower() == 'корова' and window1.lower() != 'окно' or tail1.lower() == 'хвост' and window1.lower() == 'окно' and cow1.lower() != 'корова' or cow1.lower() == 'корова' and window1.lower() == 'окно' and tail1.lower() != 'хвост':
            return render_template('result.html', level = degree2)
        else:
            return render_template('result.html', level=degree1)
    return render_template('test.html')
@app.route('/easytest', methods = ['GET', 'POST'])
def easy_test():
    if request.method == 'POST':
        sing1 = request.form['sing']
        heard1 = request.form['heard']
        speak1 = request.form['speak']
        cook1 = request.form['cooked']
        watch1 = request.form['watched']
        young1 = request.form['younger']
        night1 = request.form['night']
        said1 = request.form['said']
        blue1 = request.form['blue']
        listening1 = request.form['listening']
        guilty1 = request.form['виновный']
        remote1 = request.form['удаленный']
        recent1 = request.form['недавний']
        relevant1 = request.form['актуальный']
        curious1 = request.form['любопытный']
        correct_answers = ['sing', 'heard', 'speak', 'cooked', 'watched', 'younger', 'night', 'said','blue', 'listening', 'виновный','удаленный', 'недавний', 'актуальный', 'любопытный']
        user_answers = [sing1, heard1, speak1, cook1, watch1, young1, night1, said1, blue1, listening1, guilty1, remote1, recent1, relevant1, curious1]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count/15) * 100))
        if  percent >= 87:
            session['level'] = f'Поздравляем, вы отлично усвоили метериал! У вас  {percent} % правильных ответов. Теперь вы можете двигаться дальше и переходить к программе для среднего уровня.'
        elif 70 <= percent < 87:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти кследующему уровню."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу для новичков."
        return redirect(url_for('easy_result'))
    return render_template('easytest.html')
@app.route('/easyresult')
def easy_result():
    level = session.get('level')
    return render_template('easyresult.html', level=level)
@app.route('/avtest', methods = ['GET', 'POST'])
def av_test():
    if request.method == 'POST':
        contribute1 = request.form['contribute']
        escape1 = request.form['escape']
        abolished1 = request.form['abolished']
        squeeze1 = request.form['squeeze']
        delivery1 = request.form['delivery']
        exchange1 = request.form['exchange']
        observed1 = request.form['observed']
        earn1 = request.form['earn']
        connection1 = request.form['connection']
        districts1 = request.form['districts']
        fortune1 = request.form['удача']
        confidence1 = request.form['уверенность']
        compliant1 = request.form['соответствующий']
        influence1 = request.form['влияние']
        devotion1 = request.form['преданность']
        correct_answers = ['contribute', 'escape', 'abolished', 'squeeze', 'delivery', 'exchange', 'observed','earn', 'connection', 'districts', 'удача', 'уверенность', 'соответствующий', 'влияние', 'преданность']
        user_answers = [contribute1, escape1, abolished1, squeeze1, delivery1, exchange1, observed1, earn1, connection1, districts1, fortune1, confidence1, compliant1, influence1, devotion1]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 15) * 100))
        if percent >= 87:
            session[
                'level'] = f'Поздравляем, вы отлично усвоили метериал! У вас  {percent} % правильных ответов. Теперь вы можете двигаться дальше и переходить к программе для высокого уровня.'
        elif 70 <= percent < 87:
            session[
                'level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему уровню."
        else:
            session[
                'level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу для среднего уровня."
        return redirect(url_for('av_result'))
    return render_template('avtest.html')
@app.route('/avresult')
def av_result():
    level = session.get('level')
    return render_template('avresult.html', level=level)
@app.route('/highresult')
def high_result():
    level = session.get('level')
    return render_template('highresult.html', level=level)
@app.route('/hightest', methods = ['GET', 'POST'])
def high_test():
    if request.method == 'POST':
        lease1 = request.form['lease']
        waver1 = request.form['waver']
        follow1 = request.form['follow-up']
        prevail1 = request.form['prevail']
        axes1 = request.form['axes']
        pattern1 = request.form['pattern']
        harsh1 = request.form['harsh']
        indecisive1 = request.form['indecisive']
        outline1 = request.form['outline']
        cognition1 = request.form['cognition']
        oversight1 = request.form['надзор']
        instance1 = request.form['экземпляр']
        unveiling1 = request.form['разоблачение']
        adverse1 = request.form['неблагоприятный']
        grim1 = request.form['мрачный']
        correct_answers = ['lease', 'waver', 'follow-up', 'prevail', 'axes', 'pattern', 'harsh','indecisive', 'outline', 'cognition', 'надзор', 'экземпляр', 'разоблачение', 'неблагоприятный', 'мрачный']
        user_answers = [lease1, waver1, follow1, prevail1, axes1, pattern1, harsh1, indecisive1, outline1, cognition1, oversight1, instance1, unveiling1, adverse1, grim1]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 15) * 100))
        if percent >= 87:
            session['level'] = f'Поздравляем, вы отлично усвоили метериал! У вас  {percent} % правильных ответов. Вы освовили программу самого высокого уровня раздела лексики и можете переходить к следующему разделу - грамматике.'
        elif 70 <= percent < 87:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему разделу."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу для среднего уровня."
        return redirect(url_for('high_result'))
    return render_template('hightest.html')
@app.route('/result')
@app.route('/grammar')
def grammar():
    return render_template('grammar.html')
@app.route('/grammartest', methods = ['GET', 'POST'])
def grammar_test():
    if request.method == 'POST':
        test1 = request.form['go']
        test2 = request.form['completed']
        test3 = request.form['was walking']
        test4 = request.form['will be defending']
        test5 = request.form['had gone']
        test6 = request.form['have been waiting']
        test7 = request.form['went']
        test8 = request.form['will do']
        test9 = request.form['will have been working']
        test10 = request.form['will have done']
        correct_answers = ['go', 'completed', 'was walking', 'will be defending', 'had gone', 'have been waiting', 'went', 'will do','will have been working', 'will have done']
        user_answers = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 10) * 100))
        if percent >= 87:
            session['level'] = f'Поздравляем, вы отлично усвоили метериал! У вас  {percent} % правильных ответов. Вы освовили программу  раздела грамматики и можете переходить к следующему разделу - грамматике.'
        elif 70 <= percent < 87:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему разделу."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу."
        return redirect(url_for('grammar_result'))
    return render_template('grammartest.html')
@app.route('/grammarresult')
def grammar_result():
    level = session.get('level')
    return render_template('grammarresult.html', level=level)
@app.route('/easylistening', methods = ['GET', 'POST'])
def easy_listening():
    if request.method == 'POST':
        blank1 = request.form['mountains']
        blank2 = request.form['nurse']
        blank3 = request.form['Italy']
        blank4 = request.form['board']
        blank5 = request.form['mathematics']
        correct_answers = ['mountains', 'nurse', 'Italy', 'board', 'mathematics']
        user_answers = [blank1, blank2, blank3, blank4, blank5]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 5) * 100))
        if percent >= 80:
            session['level'] = f'Поздравляем, вы отлично усвоили метериал! У вас  {percent} % правильных ответов. Вы освовили программу начального уровня раздела аудирования и можете переходить к среднему уровню.'
        elif 60 <= percent < 80:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему уровню."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу."
        return redirect(url_for('listening_result'))
    return render_template('easylistening.html')
@app.route('/listeningresult')
def listening_result():
    level = session.get('level')
    return render_template('listeningresult.html', level=level)
@app.route('/avlistening', methods = ['GET', 'POST'])
def av_listening():
    if request.method == 'POST':
        blank1 = request.form['analytical']
        blank2 = request.form['developing']
        blank3 = request.form['chemical']
        blank4 = request.form['bachelor’s']
        blank5 = request.form['implementation']
        correct_answers = ['analytical', 'developing', 'chemical', 'bachelor’s', 'implementation']
        user_answers = [blank1, blank2, blank3, blank4, blank5]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 5) * 100))
        if percent >= 80:
            session['level'] = f'Поздравляем, вы отлично усвоили материал! У вас  {percent} % правильных ответов. Вы освовили программу среднего уровня  раздела аудирования и можете переходить к продвинутому уровню.'
        elif 60 <= percent < 80:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему уровню раздела."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу."
        return redirect(url_for('av_listening_result'))
    return render_template('avlistening.html')
@app.route('/avlisteningresult')
def av_listening_result():
    level = session.get('level')
    return render_template('avlisteningresult.html', level=level)
@app.route('/profile')
@app.route('/highlistening', methods = ['GET', 'POST'])
def high_listening():
    if request.method == 'POST':
        blank1 = request.form['1863']
        blank2 = request.form['150']
        blank3 = request.form['controversial']
        blank4 = request.form['the Tube']
        blank5 = request.form['right']
        correct_answers = ['1863', '150', 'controversial', 'the Tube', 'right']
        user_answers = [blank1, blank2, blank3, blank4, blank5]
        count = sum(ans == corr for ans, corr in zip(user_answers, correct_answers))
        percent = (math.ceil((count / 5) * 100))
        session['high_test_passed'] = True
        session['high_test_percent'] = percent
        if percent >= 80:
            session['level'] = f'Поздравляем, вы отлично усвоили материал! У вас  {percent} % правильных ответов. Вы освовили программу продвинутого уровня  раздела аудирования.'
        elif 60 <= percent < 80:
            session['level'] = f"Вы неплохо справились, у вас  {percent} % правильных ответов. Нужно еще немного потренироваться, чтобы улучшить результат и перейти к следующему уровню раздела."
        else:
            session['level'] = f"У вас {percent} % правильных ответов. Советуем вам заново тщательно изучить программу."
        return redirect(url_for('high_listening_result'))
    return render_template('highlistening.html')
@app.route('/highlisteningresult')
def high_listening_result():
    level = session.get('level')
    return render_template('highlisteningresult.html', level=level)
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/translate', methods=['GET', 'POST'])
def translate():
    translator = Translator()
    translation_result = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        dest_language = request.form.get('language', 'en')
        translation_result = translator.translate(text_to_translate, dest=dest_language).text
    return render_template('translate.html', result=translation_result)
app.run(debug=True)