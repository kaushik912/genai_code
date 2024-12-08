### Troubleshooting
    Error with OpenAI 1.56.0 - Client.__init__() got an unexpected keyword argument ‘proxies’

Step1
```
!pip install langchain_openai
!pip install langchain_community
!pip install wikipedia
!pip install duckduckgo-search
!pip install openai==1.55.3 httpx==0.27.2 --force-reinstall --quiet
```

Step2
```
import os
os.kill(os.getpid(), 9)
```

Step3
```
import os
import base64
import getpass
def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")
```

Step4
```
from langchain_community.chat_models import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
#from numpy.f2py.crackfortran import verbose

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
## The LLM piece is now changing to gemma
llm=ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

question = input("Enter the question")
response = llm.invoke(question)
print(response.content)

```
