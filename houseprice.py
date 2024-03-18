from all_imports import *

communes_cantons = {
    'Howald': 'Luxembourg',
    'Hautcharage': 'Pétange',
    'Luxembourg-Belair': 'Luxembourg',
    'Luxembourg': 'Luxembourg',
    'Esch-sur-Alzette': 'Esch-sur-Alzette',
    'Remich': 'Remich',
    'Erpeldange (Ettelbruck)': 'Diekirch',
    'Dudelange': 'Dudelange',
    'Rodange': 'Pétange',
    'Differdange': 'Differdange',
    'Stegen': 'Diekirch',
    'Lintgen': 'Mersch',
    'Schifflange': 'Schifflange',
    'Mersch': 'Mersch',
    'Mensdorf': 'Grevenmacher',
    'Pétange': 'Pétange',
    'Mamer': 'Capellen',
    'Steinfort': 'Capellen',
    'Heisdorf': 'Walferdange',
    'Reckange': 'Mersch',
    'Garnich': 'Capellen',
    'Bertrange': 'Luxembourg',
    'Capellen': 'Capellen',
    'Bascharage': 'Pétange',
    'Moesdorf': 'Mersch',
    'Cruchten': 'Mersch',
    'Useldange': 'Redange',
    'Wiltz': 'Wiltz',
    'Beringen': 'Mersch',
    'Hobscheid': 'Hobscheid',
    'Luxembourg-Kirchberg': 'Luxembourg',
    'Bettembourg': 'Bettembourg',
    'Luxembourg-Limpertsberg': 'Luxembourg',
    'Luxembourg-Bonnevoie': 'Luxembourg',
    'Erpeldange': 'Diekirch',
    'Kehlen': 'Capellen',
    'Luxembourg-Gasperich': 'Luxembourg',
    'Ettelbruck': 'Diekirch',
    'Strassen': 'Luxembourg',
    'Walferdange': 'Walferdange',
    'Steinsel': 'Walferdange',
    'Schengen': 'Remich',
    'Dalheim': 'Remich',
    'Belvaux': 'Esch-sur-Alzette',
    'Diekirch': 'Diekirch',
    'Perl': 'Perl',
    'Luxembourg-Cessange': 'Luxembourg',
    'Ell': 'Redange',
    'Koerich': 'Capellen',
    'Oberkorn': 'Differdange',
    'Luxembourg-Cents': 'Luxembourg',
    'Luxembourg-Gare': 'Luxembourg',
    'Leudelange': 'Luxembourg',
    'Sanem': 'Esch-sur-Alzette',
    'Rumelange': 'Esch-sur-Alzette',
    'Mondorf-les-Bains': 'Remich',
    'Flaxweiler': 'Grevenmacher',
    'Luxembourg-Dommeldange': 'Luxembourg',
    'Luxembourg-Neudorf': 'Luxembourg',
    'Luxembourg-Centre': 'Luxembourg',
    'Soleuvre': 'Esch-sur-Alzette',
    'Biwer': 'Grevenmacher',
    'Bereldange': 'Walferdange',
    'Luxembourg-Hollerich': 'Luxembourg',
    'Bissen': 'Mersch',
    'Niedercorn': 'Differdange',
    'Keispelt': 'Capellen',
    'Rollingen': 'Mersch',
    'Weiswampach': 'Clervaux',
    'Junglinster': 'Grevenmacher',
    'Beckerich': 'Redange',
    'Dippach': 'Capellen',
    'Sandweiler': 'Luxembourg',
    'Troisvierges': 'Clervaux',
    'Senningerberg': 'Luxembourg',
    'Lieler': 'Clervaux',
    'Belval': 'Esch-sur-Alzette',
    'Moutfort': 'Luxembourg',
    'Hellange': 'Differdange',
    'Wasserbillig': 'Remich',
    'Schuttrange': 'Luxembourg',
    'Alzingen': 'Hesperange',
    'Hamm': 'Luxembourg',
    'Roder': 'Clervaux',
    'Goeblange': 'Capellen',
    'Weimershof': 'Luxembourg',
    'Mondercange': 'Esch-sur-Alzette',
    'Hagen': 'Capellen',
    'Bettange-sur-Mess': 'Luxembourg',
    'Bridel': 'Capellen',
    'Stolzembourg': 'Clervaux',
    'Kopstal': 'Capellen',
    'Boxhorn': 'Wincrange',
    'Müllendorf': 'Walferdange',
    'Kayl': 'Esch-sur-Alzette',
    'Aubange': 'Aubange',
    'Crauthem': 'Luxembourg',
    'Baschleiden': 'Wiltz',
    'Hautbellain': 'Troisvierges',
    'Medernach': 'Diekirch',
    'Bettendorf': 'Diekirch',
    'Pontpierre': 'Mondercange',
    'Weiler': 'Putscheid',
    'Bech-Kleinmacher': 'Remich',
    'Uebersyren': 'Schuttrange',
    'Vianden': 'Vianden',
    'Wallendorf-Pont': 'Echternach',
    'Oberanven, Bei der Aarnescht': 'Niederanven',
    'Buederscheid': 'Wiltz',
    'Putscheid': 'Putscheid',
    'Ehlange': 'Reckange-sur-Mess',
    'Eischen': 'Hobscheid',
    'Sehndorf': 'Perl',
    'rue de la piscine': 'Pétange',
    'rue Emile Mayrisch': 'Schifflange',
    'Hosingen': 'Parc Hosingen',
    'Hoscheid': 'Parc Hosingen',
    'Colmar-Berg': 'Mersch',
    'Oberdonven': 'Flaxweiler',
    'Ingeldorf': 'Erpeldange',
    'Eisenborn': 'Junglinster',
    'Lamadelaine': 'Pétange',
    'Perl-Nennig': 'Perl',
    'Scheidgen': 'Consdorf',
    'Echternach': 'Echternach',
    'Fingig': 'Pétange',
    'Grevenmacher': 'Grevenmacher',
    'Bollendorf-Pont': 'Echternach',
    'Altwies': 'Remich',
    'Clemency': 'Käerjeng',
    'Perl-Besch': 'Perl',
    'Hupperdange': 'Clervaux',
    'Bitburg': 'Germany',
    'Esch-sur-Sûre': 'Wiltz',
    'Schwebach': 'Saeul',
    'Colpach-Haut': 'Ell',
    'Grevels': 'Wahl',
    'Wincrange': 'Wincrange',
    'Itzig': 'Hesperange',
    'Roedt': 'Waldbredimus',
    'Berbourg': 'Manternach',
    'Oberpallen': 'Beckerich',
    'Tétange': 'Kayl'
}


def get_price(area, bedrooms, facilities, commune):
    canton = communes_cantons[commune]

    all_facilities = ['Attic', 'Terrace', 'Basement', 'Balcony', 'Garden']

    facilities_dict = {}
    for facility in all_facilities:
        if facility in facilities:
            facilities_dict[facility] = 1
        else:
            facilities_dict[facility] = 0

    basic_dict = {'Surface area': area, 'Bedrooms': bedrooms, 'Commune': commune, 'Canton': canton}

    X_test = pd.DataFrame([{**basic_dict, **facilities_dict}])

    pipe = joblib.load('pipe.joblib')
    X_test = pipe.transform(X_test)

    stacking_regressor = joblib.load('stack.joblib')
    voting_regressor = joblib.load('vote.joblib')

    y_pred_stacking = stacking_regressor.predict(X_test)
    y_pred_voting = voting_regressor.predict(X_test)
    y_pred_average = (y_pred_stacking + y_pred_voting) / 2

    print('\n')
    print(y_pred_stacking)
    print(y_pred_voting)
    print(y_pred_average)

    return y_pred_average
