import requests

import pandas as pd
from bs4 import BeautifulSoup

def parse_recipe(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    title = soup.find('h1', class_='emotion-1w4b10k').text.strip()
    
    cooking_time = soup.find('div', class_='emotion-my9yfq').text.strip()
    
    saves = soup.find('span', class_='emotion-1h7o5m3').text.strip()
    
    likes = soup.find('span', class_='emotion-a07nxg').text.strip()
    dislikes = soup.find_all('span', class_='emotion-a07nxg')[1].text.strip()
    
    calories = soup.find('span', attrs={'itemprop': 'calories'}).text.strip()
    protein = soup.find('span', attrs={'itemprop': 'proteinContent'}).text.strip()
    fat = soup.find('span', attrs={'itemprop': 'fatContent'}).text.strip()
    carbs = soup.find('span', attrs={'itemprop': 'carbohydrateContent'}).text.strip()
    
    recipe_data = {
        'title': title,
        'cooking_time': cooking_time,
        'saves': saves,
        'likes': likes,
        'dislikes': dislikes,
        'calories': calories,
        'protein': protein,
        'fat': fat,
        'carbs': carbs
    }
    
    return recipe_data


if __name__ == "__main__":
    df = pd.DataFrame()

    with open("recipe_links.txt", "r") as file:
        for link in file:
            try:
                response = requests.get(link.strip())
                html_content = response.text
                data = parse_recipe(html_content)
                data['link'] = link.strip()
                df = pd.concat([df, pd.DataFrame([data])])
            except Exception as e:
                print(f"Error parsing {link.strip()}: {e}")

    df.to_excel("recipes.xlsx", index=False)