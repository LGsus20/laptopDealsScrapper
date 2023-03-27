from reddit_scrapper import webget


five_to_six = 'https://www.reddit.com/r/LaptopDeals/?f=flair_name%3A%22%F0%9F%9B%92%24500-%24600%F0%9F%9B%92%22'
six_to_seven = 'https://www.reddit.com/r/LaptopDeals/new/?f=flair_name%3A%22%F0%9F%9B%92%24600-%24700%F0%9F%9B%92%22'
seven_to_eight = 'https://www.reddit.com/r/LaptopDeals/new/?f=flair_name%3A%22%F0%9F%9B%92%24700-%24800%F0%9F%9B%92%22'
eight_to_nine = 'https://www.reddit.com/r/LaptopDeals/?f=flair_name%3A%22%F0%9F%9B%92%24800-%24900%F0%9F%9B%92%22'
nine_to_ten = 'https://www.reddit.com/r/LaptopDeals/new/?f=flair_name%3A%22%F0%9F%9B%92%24900-%241000%F0%9F%9B%92%22'

price_range = [five_to_six, six_to_seven, seven_to_eight, eight_to_nine, nine_to_ten]

titles = []
times = []
links = []
prices = []

for i in range(len(price_range)):
    result = webget(price_range[i])
    titles.extend(result[0])
    times.extend(result[1])
    links.extend(result[2])
    prices.extend(result[3])
my_data = {'titles': titles, 'times': times, 'links': links, 'prices': prices}

with open('All_discounts.txt', 'w', encoding='utf-8') as file:
    for i in range(len(my_data['titles'])):
        file.write(f"Title: {my_data['titles'][i]}\nPrice: ${my_data['prices'][i]}\nTime: {my_data['times'][i]}\nLink: {my_data['links'][i]}\n\n")
