from all_imports import *

attractions_df = pd.read_csv('itineraryProcessedDataset.csv')

nlp = spacy.load('en_core_web_md')


def calculate_similarity(attraction_description, user_description):
    attraction_doc = nlp(attraction_description)
    user_doc = nlp(user_description)
    return attraction_doc.similarity(user_doc)


# Compute similarity scores for each attraction
def compute_similarities(attractions_df, user_description):
    attractions_df['Similarity'] = attractions_df['Details'].apply(lambda x: calculate_similarity(x, user_description))
    return attractions_df.sort_values(by='Similarity', ascending=False)


# Generate itinerary for the specified number of days based on user's description
def generate_itinerary(user_description, num_days):
    itinerary = defaultdict(lambda: defaultdict(list))
    suggested_attractions = set()
    for day in range(1, num_days + 1):
        # Reset meal flags
        breakfast_done = False
        lunch_done = False
        dinner_done = False
        # Compute similarity scores for attractions
        similarities = compute_similarities(attractions_df, user_description)
        # Filter attractions for each segment of the day
        for idx, attraction in similarities.iterrows():
            if attraction['Name'] not in suggested_attractions:
                if not breakfast_done and len(itinerary[f'Day {day}']['Morning']) < 2:
                    itinerary[f'Day {day}']['Morning'].append((attraction['Name'], attraction['Type']))
                    suggested_attractions.add(attraction['Name'])
                    breakfast_done = True
                elif not lunch_done and len(itinerary[f'Day {day}']['Afternoon']) < 2:
                    itinerary[f'Day {day}']['Afternoon'].append((attraction['Name'], attraction['Type']))
                    itinerary[f'Day {day}']['Afternoon'].append("Lunch at a nearby café")
                    suggested_attractions.add(attraction['Name'])
                    lunch_done = True
                elif not dinner_done and len(itinerary[f'Day {day}']['Evening']) < 2:
                    itinerary[f'Day {day}']['Evening'].append((attraction['Name'], attraction['Type']))
                    itinerary[f'Day {day}']['Evening'].append("Dinner at a nearby restaurant")
                    suggested_attractions.add(attraction['Name'])
                    dinner_done = True
            if breakfast_done and lunch_done and dinner_done:
                break

    print("Recommended Itinerary:")
    for day, segments in itinerary.items():
        print(f"{day}:")
        for segment, attractions in segments.items():
            print(f"  - {segment}:")
            if not attractions:
                print("    - No attractions recommended")
            else:
                for attraction in attractions:
                    if isinstance(attraction, tuple):
                        print(f"    - {attraction[0]} ({attraction[1]})")
                    else:
                        print(f"    - {attraction}")

    return itinerary
