### Image Processing
We have an image and we want to use OpenAI to answer some questions based on the image.

- Define a method to encode the image to base64
```
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
```

- Create the prompt
```
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
image = encode_image("/content/sample_data/children.png")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"}, #message1
                {#message2
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

```

- Invoke the chain
```
chain = prompt | llm
response = chain.invoke({"input": "Explain"})
```

- Print the response content
```
print(response.content)
```
- Sample Response
```
The image depicts a group of five children happily playing together. 

1. The child on the left is sitting, wearing a pink outfit, and blowing bubbles.
2. Next to them, another child is sitting and holding a teddy bear, wearing a blue dress.
3. In the center, a child with a cap is playing with colorful blocks, including a cube, cylinder, and cone.
4. Another child, to the right, is standing with their arms raised, appearing excited, wearing a green shirt.
5. The child on the far right is sitting and laughing, holding a small teddy bear, wearing a purple outfit.

The children are engaged in playful activities, showing expressions of joy and excitement.
```

KEY NOTES:
- You can use any image of your choice.

- We create a ChatPromptTemplate from messages but its slightly different.
- First, it has a system message as "You are a helpful assistant that can describe images"
- Then the human message message has two sets of messages.
  - First message has
  ```
  {"type": "text", "text": "{input}"}
  ```
  So it has the input which is our image.

  - Second message has the image_url
  ```
   {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image}",
                    "detail": "low",
                },
   }
  ```
  
