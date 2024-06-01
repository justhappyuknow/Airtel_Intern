
import openai

# Set up the OpenAI API key
openai.api_key = 'my-api-key'


prompt = """
Given the following customer profiles, generate:
1. A brief pitch for a salesperson to make to these customers, including relevant products and justifications, not more than 70 words.
2. Four leading questions a salesperson can ask each of the customers to discover helpful responses for a better and more customized sales pitch. The questions should be diverse.

CUSTOMER A:
Owner of a medium-sized business in Faridabad. Deals in distribution of bathroom-ware and fittings across Delhi, Haryana, and Punjab. Uses Jio Wi-Fi in his home and office set-up. Has a small 20-seater office and is currently hiring more employees. Is hard pressed for time and looking to optimize.

CUSTOMER B:
Procurement lead of a micro-finance company in Ahmedabad. Company is looking to expand its customer base in Gujarat. Uses Airtel Broadband – 100 mbps. Company currently employs 100 on-field salespeople. Is going to shift office location to another spot in Ahmedabad with a larger seating capacity. Currently under discussion with multiple OEM’s for different technology solutions.

Output format:
1. Pitch for Customer A: [Pitch]
2. Pitch for Customer B: [Pitch]
3. Questions for Customer A:
   - [Question 1]
   - [Question 2]
   - [Question 3]
   - [Question 4]
4. Questions for Customer B:
   - [Question 1]
   - [Question 2]
   - [Question 3]
   - [Question 4]
"""


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=250,
    temperature=0.7,
)

output = response.choices[0].message['content'].strip()
print(output)
