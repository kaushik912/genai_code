{
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Ollama Models\n",
        "\n",
        "Steps to run\n",
        "- Start ollama locally using `ollama serve`\n",
        "- Download the required model using `ollama pull <model>`\n",
        "- Set OPENAI_API_KEY to your open-api key in ~/.bashrc or ~/.zshrc\n",
        "- Below is the example for gemma model\n"
      ],
      "metadata": {
        "id": "cR-LhRljMd7n"
      },
      "id": "cR-LhRljMd7n"
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from langchain_community.chat_models import ChatOllama\n",
        "\n",
        "OPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\n",
        "\n",
        "## The LLM piece is now changing to gemma\n",
        "llm=ChatOllama(model=\"gemma:2b\")\n",
        "\n",
        "## Everything else remains same!\n",
        "\n",
        "question = input(\"Enter the question\")\n",
        "response = llm.invoke(question)\n",
        "print(response.content)\n",
        "\n"
      ],
      "metadata": {
        "id": "X__7IPv6tXRy"
      },
      "id": "X__7IPv6tXRy",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now with langchain, we can substitute the model and we'll get results from that model.\n",
        "\n",
        "- Mistral LLM\n",
        "\n",
        "  `llm=ChatOllama(model=\"mistral\")`\n"
      ],
      "metadata": {
        "id": "FH_oPhNsdtrO"
      },
      "id": "FH_oPhNsdtrO"
    },
    {
      "cell_type": "markdown",
      "source": [
        "The code would like below"
      ],
      "metadata": {
        "id": "sNizrI3uezg1"
      },
      "id": "sNizrI3uezg1"
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from langchain_community.chat_models import ChatOllama\n",
        "\n",
        "OPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\n",
        "\n",
        "## The LLM piece is now changing to mistral\n",
        "llm=ChatOllama(model=\"mistral\")\n",
        "\n",
        "## Everything else remains same!\n",
        "\n",
        "question = input(\"Enter the question\")\n",
        "response = llm.invoke(question)\n",
        "print(response.content)\n",
        "\n"
      ],
      "metadata": {
        "id": "407MZHo1e1zl"
      },
      "id": "407MZHo1e1zl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "[gemma_demo notebook](https://colab.research.google.com/github/kaushik912/genai_code/blob/main/Langchain/basics/gemma_demo.ipynb)"
      ],
      "metadata": {
        "id": "WN0Q373Sfvrd"
      },
      "id": "WN0Q373Sfvrd"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.12.1"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
