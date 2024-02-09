
import pandas as pd

# Sample dataset
data = {
    'Date': ['20-Nov', '20-Nov', '20-Nov', '21-Nov', '21-Nov', '21-Nov'],
    'AppsOpened': [
        ['word', 'youtube', 'whatsapp', 'instagram'],
        ['youtube', 'whatsapp', 'instagram'],
        ['whatsapp', 'instagram'],
        ['youtube', 'whatsapp', 'instagram'],
        ['whatsapp', 'instagram'],
        ['instagram']
    ]
}

df = pd.DataFrame(data)

# i) Number of times the user opened WhatsApp as his first time of the day
def count_whatsapp_as_first_choice(dataframe):
    whatsapp_first_count = 0
    for apps in dataframe['AppsOpened']:
        if 'whatsapp' in apps and apps.index('whatsapp') == 0:
            whatsapp_first_count += 1
    return whatsapp_first_count

whatsapp_first_count = count_whatsapp_as_first_choice(df)
print(f"Number of times WhatsApp was opened as the first choice: {whatsapp_first_count}")

# ii) Probability of opening WhatsApp as his first choice
def probability_whatsapp_as_first_choice(dataframe):
    total_days = len(dataframe)
    whatsapp_first_count = count_whatsapp_as_first_choice(dataframe)
    return whatsapp_first_count / total_days

prob_whatsapp_first_choice = probability_whatsapp_as_first_choice(df)
print(f"Probability of opening WhatsApp as the first choice: {prob_whatsapp_first_choice:.2f}")

# iii) Probability of opening WhatsApp as the second choice if Instagram was the first choice
def probability_whatsapp_after_instagram(dataframe):
    instagram_first_count = 0
    whatsapp_after_instagram_count = 0
    for apps in dataframe['AppsOpened']:
        if 'instagram' in apps and 'whatsapp' in apps:
            instagram_first_count += 1
            if apps.index('whatsapp') == 1:  # Check if WhatsApp is the second choice
                whatsapp_after_instagram_count += 1
    if instagram_first_count == 0:  # To avoid division by zero
        return 0
    return whatsapp_after_instagram_count / instagram_first_count

prob_whatsapp_after_instagram = probability_whatsapp_after_instagram(df)
print(f"Probability of opening WhatsApp after Instagram: {prob_whatsapp_after_instagram:.2f}")
