import math
import requests
from urllib.parse import quote

check = input("Enter the steam appid you want to check: ")
if check.isnumeric():
    appid = int(check)
else:
    print("Please input a numbers only as the appid")

url = f"https://store.steampowered.com/appreviews/{appid}?json=1&filter=all&language=all&num_per_page=100"

session = requests.Session()

jData = session.get(url).json()

if jData['success'] != 1:
    print("Please input a valid appid")
    exit(1)

total_reviews =  jData['query_summary']['total_reviews']
total_positive = jData['query_summary']['total_positive']
total_negative = jData['query_summary']['total_negative']


if total_reviews == 0 or (total_positive == 0 or total_negative == 0):
    print("No reviews to check. Exiting!")
    exit(1)

print("Enter the minimum amount of minuts")
check = input("a review should have (can spereated by ,): ")

min_Minuts = []

if ',' in check:
    for num in check.split(','):
        if num.isnumeric():
            min_Minuts.append(int(num))
        else:
            print("Please input a numbers only as the minuts")
            exit(1)
else:
    if check.isnumeric():
        min_Minuts = [int(check)]
    else:
        print("Please input a numbers only as the minuts")
        exit(1)

total_rating = round(total_positive / total_reviews * 100,2)

cursor = jData['cursor']

reviews = jData['reviews']

total_reviews_hundrets = int(math.floor(total_reviews / 100.0)) * 100

total_rest_reviews = total_reviews - total_reviews_hundrets

review_sits = total_reviews_hundrets / 100

if total_rest_reviews > 0:
    review_sits += 1

print("Fatching all reviews")

for i in range(int(review_sits)):
    jData = session.get(url+"&cursor="+quote(cursor,safe='')).json()
    reviews.extend(jData['reviews'])
    cursor = jData['cursor']
    print(f"{round(i/int(review_sits)*100,2)}% done.")
print(f"100.00% done.")

print('\n---------------------------------------------------------------\n')
for minuts in min_Minuts:
    print(f'Cehcking for AppID: {appid} and minimum minuts of {minuts}')
    print('\n')

    reduced_positive = 0
    reduced_negative = 0

    for review in reviews:
        pTime = review['author']['playtime_at_review']
        upVote = review['voted_up']
        if pTime > minuts:
            if upVote:
                reduced_positive+=1
            else:
                reduced_negative+=1

    reduced_total = reduced_positive + reduced_negative

    reduced_rating = round(reduced_positive / reduced_total * 100,2)

    print(f'Total Votes: {total_reviews}\nTotal Up Votes: {total_positive}\nTotal Down Votes: {total_negative}\n Total Rating Ratio: {total_rating}')
    print('\n')
    print(f'Reduced Up Votes: {reduced_positive}\nReduced Down Votes: {reduced_negative}\nReduced Rating Ratio: {reduced_rating}')
    print('\n---------------------------------------------------------------\n')