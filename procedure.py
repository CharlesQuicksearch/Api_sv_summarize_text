from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained('model')
tokenizer = AutoTokenizer.from_pretrained('model')

def summarize_text(input):
    tokens = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=tokens, max_length=130, num_beams=5, num_return_sequences=1)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return result
