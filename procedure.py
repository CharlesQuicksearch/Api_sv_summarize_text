import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from Logger_Config.logger import logging

with open("model_config.json", "r") as f:
    config = json.load(f)

model_path = config.get("model_path")

logging.info(f"Loading model and tokenizer from {model_path}")
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)


def summarize_text(text):
    logging.info("Start summarize text.")
    tokens = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=tokens, max_length=130, num_beams=5, num_return_sequences=1)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    logging.info(f"End Summarize text. Returning results.")

    return result[0]
