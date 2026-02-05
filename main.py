import google.generativeai as genai

# 1. API Key ማገናኘት
API_KEY = "AIzaSyAIV3934aqSbTm23MIeIePmFQDt8jTtpMU"
genai.configure(api_key=API_KEY)

# 2. የ AIው ባህሪ (System Instruction)
# እዚህ ጋር ነው AIው በሰለፎች መንገድ ብቻ እንዲመልስ የምናዝዘው
generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
  model_name="gemini-pro",
  generation_config=generation_config,
  # እዚህ ጋር ነው ማንነቱን የምንሰጠው
  instruction="አንተ ኢስላማዊ ረዳት ነህ። መልሶችህ በሙሉ በቁርአን፣ በሀዲስና በሰለፎች (ለምሳሌ፡ ኢማም አህመድ፣ ኢብኑ ተይሚያህ፣ ኢብኑል ቀይም) አስተምህሮ ላይ ብቻ የተመሰረቱ መሆን አለባቸው። ያልታወቁ ወይም አዲስ መጤ እምነቶችን አትጠቀም። መልስ ስትሰጥ ማስረጃ ጥቀስ።"
)

def start_chat():
    chat = model.start_chat(history=[])
    print("እንኳን ደህና መጡ! እኔ በሰለፎች መንገድ ለጥያቄዎችዎ ምላሽ የምሰጥ AI ነኝ።")
    print("--------------------------------------------------")
    
    while True:
        user_input = input("ጥያቄዎን ይጠይቁ (ለማቆም 'exit' ይበሉ): ")
        if user_input.lower() == 'exit':
            break
        
        try:
            response = chat.send_message(user_input)
            print("\nምላሽ:\n", response.text)
            print("-" * 30)
        except Exception as e:
            print(f"ስህተት ተከስቷል: {e}")

# አፑን ማስጀመር
if __name__ == "__main__":
    start_chat()
