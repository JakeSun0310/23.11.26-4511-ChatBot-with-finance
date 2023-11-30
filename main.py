# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
os.environ['OPENAI_API_KEY'] = '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'

from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

#在此处进行prompt的修改，角色任务的设定
template = """Extract the following structured information from this conversation between an investor and fund manager:
Investment Strategy - percentage allocations to different sectors:
Risk Management - details on risk management approach:
Investment Performance - historical returns:
{history}
Human: {human_input}
Assistant:"""


prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

output = chatgpt_chain.predict(human_input="{Investor: We plan to focus the new capital on the technology sector, allocating 50% to emerging internet companies and 30% to cybersecurity. The remaining 20% will be kept in cash to maintain liquidity. Fund Manager: That sector concentration is quite high. Can you walk me through your risk management process? Investor: We have a robust risk management team that monitors position sizes, industry exposures, and portfolio liquidity daily. We also run regular stress tests to model potential losses in a downturn scenario. Fund Manager: Okay, that provides helpful context on your strategy and risk controls. What has your historical performance been over the last 5 years? Investor: Our fund has returned an average of 22% net annually over the last 5 years. Last year was 32% driven by our internet stock holdings.}")
print(output)



'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''