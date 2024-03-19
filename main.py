from all_imports import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


all_facilities = ['Attic', 'Terrace', 'Basement', 'Balcony', 'Garden']

all_communes = ['Luxembourg', 'Hautcharage', 'Mersch', 'Luxembourg-Belair', 'Howald',
                'Esch-sur-Alzette', 'Mamer', 'Steinfort', 'Differdange', 'Dudelange',
                'Erpeldange (Ettelbruck)', 'Aubange', 'Mensdorf', 'Remich', 'Moesdorf',
                'Rodange', 'Kehlen', 'Stegen', 'Schifflange', 'Strassen', 'Ettelbruck',
                'Pétange', 'Bettembourg', 'Belvaux', 'Lintgen', 'Wasserbillig',
                'Bertrange', 'Heisdorf', 'Hobscheid', 'Steinsel', 'Walferdange',
                'Wiltz', 'Rumelange', 'Garnich', 'Bascharage', 'Perl', 'Sanem',
                'Useldange', 'Bereldange', 'Hellange', 'Erpeldange', 'Schengen',
                'Cruchten', 'Koerich', 'Junglinster', 'Ell', 'Moutfort', 'Biwer',
                'Mondercange', 'Schuttrange', 'Leudelange', 'Diekirch', 'Keispelt', 'Dippach', 'Weiler',
                'Mondorf-les-Bains', 'Dalheim', 'Flaxweiler', 'Senningerberg',
                'Grevenmacher', 'Weiswampach', 'Capellen', 'Bissen', 'Troisvierges',
                'Kayl', 'Bridel', 'Beckerich', 'Hosingen', 'Roder', 'Roedt',
                'Schwebach', 'Alzingen', 'Vianden', 'Stolzembourg', 'Berbourg',
                'Sandweiler', 'Lieler', 'Dubai', 'Boxhorn', 'Clemency', 'Kopstal',
                'Colmar-Berg', 'Esch-sur-Sûre', 'Perl-Nennig', 'Bech-Kleinmacher',
                'Bollendorf-Pont', 'Fingig', 'Beringen', 'Echternach', 'Eischen',
                'Sehndorf', 'Wallendorf-Pont', 'Bitburg', 'Hupperdange', 'Bettendorf',
                'Medernach', 'Putscheid', 'Buederscheid', 'Crauthem', 'Scheidgen',
                'Reckange', 'Oberanven, Bei der Aarnescht', 'Baschleiden', 'Grevels',
                'Wincrange', 'Itzig', 'Uebersyren']


@app.route('/properties.html')
def properties():
    return render_template('properties.html', options=all_communes, options2=all_facilities)


@app.route('/submit_properties', methods=['POST'])
def submit_properties():
    area = request.form['formArea'].strip()
    bedrooms = request.form['formBedrooms'].strip()
    facilities = request.form.getlist('formFacilities')
    commune = request.form['formCommune']

    errors = validate_properties_form(area, bedrooms)
    if errors:
        return render_template('properties.html', errors=errors, area=area, bedrooms=bedrooms, facilities=facilities,
                               commune=commune, options=all_communes, options2=all_facilities)

    price = get_price(area=area, bedrooms=bedrooms, facilities=facilities, commune=commune)
    print(price)

    return render_template('properties.html', options=all_communes, options2=all_facilities, predicted_price='{:,.0f}'.format(int(price[0])))


def validate_properties_form(area, bedrooms):
    errors = []

    try:
        area = float(area)
        if area < 25 or area > 10000:
            errors.append('Enter a valid Surface Area between 25 sq. meters and 1500 sq. meters')
    except:
        errors.append('Enter a valid Area in square meters')

    try:
        bedrooms = int(bedrooms)
        if bedrooms < 1 or bedrooms > 10:
            errors.append('Enter a valid Number of Bedrooms between 1 and 10')
    except:
        errors.append('Enter valid Number of Bedrooms')

    return errors


@app.route('/news.html')
def news():
    return render_template('news.html')


@app.route('/submit_news', methods=['POST'])
def submit_news():
    title = request.form['formTitle'].strip()
    description = request.form['formDescription'].strip()

    errors = validate_news_form(title, description)
    if errors:
        return render_template('news.html', errors=errors, title=title, description=description)

    st_score, sd_score, so_score, st, sd, so = sentiment_score(title=title, description=description)
    print(st_score, sd_score, so_score, st, sd, so)

    return render_template('news.html', st_score=st_score, sd_score=sd_score, so_score=so_score, st=st, sd=sd, so=so)


def validate_news_form(title, description):
    errors = []
    pattern = r'[^a-zA-Z0-9\s]'

    try:
        title = re.sub(pattern, '', title)
        if len(title) < 10 or len(title) > 100:
            errors.append('Enter a valid News Title of length between 25 characters and 100 characters')
    except:
        errors.append('Enter a valid News Title')

    try:
        description = re.sub(pattern, '', description)
        if len(description) < 25 or len(description) > 250:
            errors.append('Enter a valid News Description of length between 25 characters and 250 characters')
    except:
        errors.append('Enter a valid News Description')

    return errors


@app.route('/itinerary.html')
def itinerary():
    return render_template('itinerary.html')


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
    days = request.form['formDays'].strip()
    description = request.form['formDescription'].strip()

    errors = validate_itinerary_form(days, description)
    if errors:
        return render_template('itinerary.html', errors=errors, days=days, description=description)

    geniti = generate_itinerary(user_description=description, num_days=int(days))

    return render_template('itinerary.html', geniti=geniti)


def validate_itinerary_form(days, description):
    errors = []
    pattern = r'[^a-zA-Z0-9\s]'

    try:
        days = int(days)
        if days < 1 or days > 5:
            errors.append('Enter a valid Number of Days between 1 and 5 days')
    except:
        errors.append('Enter a valid Number of Days')

    try:
        description = re.sub(pattern, '', description)
        if len(description) < 25 or len(description) > 250:
            errors.append('Enter a valid Description of length between 25 characters and 250 characters')
    except:
        errors.append('Enter a valid Description')

    return errors


@app.route('/food.html')
def food():
    template = render_template('food.html')
    return template


@app.route('/submit_food', methods=['POST'])
def submit_food():
    img = request.files['formFile']
    file_path = os.path.join(app.root_path, 'static', 'img', img.filename)
    img.save(file_path)
    image_path = os.path.abspath(file_path)
    predicted_food = predict_with_vgg_model(image_path)

    print("Here is predicted class", predicted_food)
    source = f'/static/img/{img.filename}'
    return render_template('food.html', food=predicted_food, file_path=source)


if __name__ == "__main__":
    app.run(debug=True)
