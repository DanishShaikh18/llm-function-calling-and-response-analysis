import os
import time

from dotenv import load_dotenv
from google import genai

from functions import calculate
from functions import get_weather

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================
# Helper
# ==========================================

def generate_response(prompt, temperature=0.7, max_retries=5):
    start_time = time.time()

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "temperature": temperature
                }
            )
            break
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"\n[Warning] API Error: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"\n[Error] Failed after {max_retries} attempts.")
                raise

    end_time = time.time()

    latency = round(end_time - start_time, 2)

    return response.text, latency


# ==========================================
# 1. Temperature Testing
# ==========================================

def temperature_test():
    print("\n" + "=" * 60)
    print("TEMPERATURE TEST")
    print("=" * 60)

    prompt = "Suggest a name for an AI startup."

    temperatures = [0.0, 0.3, 0.7, 1.0]

    for temp in temperatures:

        output, latency = generate_response(
            prompt,
            temperature=temp
        )

        print(f"\nTemperature: {temp}")
        print(f"Latency: {latency} sec")
        print(output)


# ==========================================
# 2. Context Testing
# ==========================================

def context_test():
    print("\n" + "=" * 60)
    print("CONTEXT TEST")
    print("=" * 60)

    question = "How many leave days do employees receive?"

    print("\nCase A : No Context")

    output_a, latency_a = generate_response(question)

    print(f"Latency: {latency_a} sec")
    print(output_a)

    with open("policy.txt", "r") as file:
        policy = file.read()

    prompt_with_context = f"""
    Context:

    {policy}

    Question:
    {question}
    """

    print("\nCase B : With Context")

    output_b, latency_b = generate_response(
        prompt_with_context
    )

    print(f"Latency: {latency_b} sec")
    print(output_b)


# ==========================================
# 3. Hallucination Test
# ==========================================

def hallucination_test():
    print("\n" + "=" * 60)
    print("HALLUCINATION TEST")
    print("=" * 60)

    question = "Who is the CEO of Mars Colony Corporation?"

    print("\nCase A : Normal Prompt")

    output_a, latency_a = generate_response(question)

    print(f"Latency: {latency_a} sec")
    print(output_a)

    constrained_prompt = f"""
    You are a factual assistant.

    If information is unknown,
    respond only with:

    I don't know.

    Do not guess.

    Question:
    {question}
    """

    print("\nCase B : Anti-Hallucination Prompt")

    output_b, latency_b = generate_response(
        constrained_prompt
    )

    print(f"Latency: {latency_b} sec")
    print(output_b)


# ==========================================
# 4. Function Calling Demo
# ==========================================

def function_calling_demo():
    print("\n" + "=" * 60)
    print("FUNCTION CALLING DEMO")
    print("=" * 60)

    user_queries = [
        "What is 234 multiplied by 56?",
        "What is the weather in Mumbai?"
    ]

    for query in user_queries:

        print("\nUser Query:")
        print(query)

        lower_query = query.lower()

        if "multiplied" in lower_query:

            result = calculate(
                234,
                56,
                "multiply"
            )

            print("\nFunction Selected:")
            print("calculate")

            print("\nFunction Result:")
            print(result)

            final_prompt = f"""
            User asked:

            {query}

            Function result:

            {result}

            Generate final response.
            """

            response, latency = generate_response(
                final_prompt,
                temperature=0
            )

            print("\nFinal Response:")
            print(response)

            print(f"\nLatency: {latency} sec")

        elif "weather" in lower_query:

            result = get_weather("Mumbai")

            print("\nFunction Selected:")
            print("get_weather")

            print("\nFunction Result:")
            print(result)

            final_prompt = f"""
            User asked:

            {query}

            Function result:

            {result}

            Generate final response.
            """

            response, latency = generate_response(
                final_prompt,
                temperature=0
            )

            print("\nFinal Response:")
            print(response)

            print(f"\nLatency: {latency} sec")


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    temperature_test()

    context_test()

    hallucination_test()

    function_calling_demo()