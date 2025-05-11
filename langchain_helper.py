import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

os.environ['GOOGLE_API_KEY'] = "AIzaSyDOmG9VLDhhCnOt8bUnMw5oURysaTsCzVM"


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Use "gemini-1.5-flash" for the fast model
    temperature=0.6,
    convert_system_message_to_human=True
)


def generate_restaurant_name_and_items(cuisine):

    #chain 1 :
    prompt_restaurant_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "suggest me a good name of my new restaurat which is {cuisine} in type , suggest only one name"

    )
    name_chain = LLMChain(llm = llm , prompt = prompt_restaurant_name , output_key = "restaurant_name")


    #chain 2 :
    prompt_restaurant_item_names = PromptTemplate(
        input_variables = ["restaurant_name"],
        template = "suggest the list of items that could be available in the {restaurant_name}"
    )

    restaurant_chain = LLMChain(llm = llm , prompt = prompt_restaurant_item_names , output_key = "menu_list")

    # Sequential Chain
    chain = SequentialChain(
        chains = [name_chain , restaurant_chain],
        input_variables = ["cuisine"],
        output_variables = ['restaurant_name' , 'menu_list']
    )

    response = chain({"cuisine" : cuisine })
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items(Indian))