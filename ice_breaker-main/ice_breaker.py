from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

import os

# Set the OpenAI API key as an environment variable


name = "Elan Mask"

if __name__ == "__main__":
    print("Hello")
    print(os.environ["OPENAI_API_KEY"])


linkedin_profile_url = linkedin_lookup_agent(name="Dharmesh Baraskat , Hexaware")
linkedin_data= scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

username = twitter_lookup_agent(name=name)
tweetData =scrape_user_tweets(username=username,num_tweets=100)

summary_template = """
    given the linkedin information {linkedin_infromation} and twitter {twitter_information} about a person from I want you to create:
    1. a short summary 
    2. two instersting fact about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["linkedin_infromation","twitter_information"], template=summary_template
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=summary_prompt_template)

# linkedin_data= scrape_linkedin_profile(
#     linkedin_profile_url="https://www.linkedin.com/in/dharmesh-baraskar-8634b038/"
#     )


#print(linkedin_data)

# print(chain.run(infromation=infromation))

print(chain.run(linkedin_infromation=linkedin_data,twtter_information=tweetData))
#print(TweeterUserName)
