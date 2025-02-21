from bs4 import BeautifulSoup

def get_recipe_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    recipe_links = []
    
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if '/recepty/' in href and href.endswith(tuple(str(i) for i in range(10))):
            if not href.startswith('https://eda.ru'):
                href = 'https://eda.ru' + href
            recipe_links.append(href)
            
    return list(set(recipe_links))

if __name__ == "__main__":
    with open("pages.html", "r") as file:
        html_content = file.read()
    with open("recipe_links.txt", "w") as file:
        for link in get_recipe_links(html_content):
            file.write(link + "\n")