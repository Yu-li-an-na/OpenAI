from flask import Flask, render_template, request, jsonify
import base64
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="TU_MA_BYT_API_KEY")  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        image_data = data["image"]
        query = data.get("query", "")

        header, encoded = image_data.split(",", 1)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Analyzuj obrázok extrémne presne. "
                                "Tvojou úlohou je pomáhať nevidiacemu používateľovi. "
                                "Používaj jasné, stručné a orientačné opisy priestoru. "
                                "Vždy odpovedaj podľa typu otázky nasledovne:\n\n"

                                "1) Ak sa používateľ pýta na konkrétny predmet "
                                "(napr. 'kde je pohár', 'nájdi ovládač'), "
                                "vždy uveď presnú polohu objektu: "
                                "'vľavo hore', 'vpravo dole', 'v strede', "
                                "'na stole vpravo', 'pred televízorom', "
                                "'pri okraji gauča', '20 cm od ľavého okraja stola'. "
                                "Ak predmet nevidíš, povedz to jasne.\n\n"

                                "2) Ak sa používateľ pýta na navigáciu "
                                "(napr. 'čo je predo mnou', 'čo je napravo'), "
                                "popíš priestor ako navigačný asistent: "
                                "'Pred tebou je stôl, za ním televízor. "
                                "Vpravo je kreslo. Vľavo je polica.'\n\n"

                                "3) Ak sa pýta na všeobecný opis, popíš scénu stručne, "
                                "ale informatívne.\n\n"

                                "4) Ak sa pýta na viac objektov, popíš ich polohu "
                                "relatívne k sebe.\n\n"

                                f"Odpovedz na otázku: {query}"
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded}"
                            }
                        }
                    ]
                }
            ]
        )

        text = response.choices[0].message.content
        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"text": f"Chyba: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
