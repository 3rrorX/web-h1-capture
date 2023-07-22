import requests
from bs4 import BeautifulSoup

def get_h1_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            h1_tags = soup.find_all('h1')
            return [h1.text.strip() for h1 in h1_tags]
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching {url}: {e}")
    return []

def main():
    input_file = "list_of_links.txt"
    output_file = "captured_h1_data.txt"

    with open(input_file, "r") as file:
        links = file.read().splitlines()

    captured_h1_data = {}

    for link in links:
        h1_tags = get_h1_from_url(link)
        captured_h1_data[link] = h1_tags

    with open(output_file, "w") as out_file:
        for link, h1_tags in captured_h1_data.items():
            out_file.write(f"H1 headings from {link}:\n")
            for h1 in h1_tags:
                out_file.write(f"{h1}\n")
            out_file.write("\n")

    print(f"Captured data saved in {output_file}")

if __name__ == "__main__":
    main()
