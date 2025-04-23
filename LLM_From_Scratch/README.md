# Custom Language Model

*A character-level language model built from scratch*

---

## 📊 Key Stats

| Metric             | Value  | Description                                                |
|--------------------|--------|------------------------------------------------------------|
| **Total Tokens**   | 2.93M  | Number of individual characters processed during training |
| **Model Parameters** | 2.42M  | Learnable values that define how the model processes text |
| **Vocabulary Size** | 255    | Unique characters the model can understand and generate   |

---

## 🤖 What This Model Does

This language model reads text **character by character** and learns to **predict what comes next**. After training, it can generate new text that resembles the style of what it learned from.

> **In simple terms**: Think of it like a person who's read a lot of text and can now write similar content based on what they've learned, one character at a time.

---

## 🔧 Key Technical Details

- **Context Window**: 16 characters  
  *The model looks at 16 characters at once to predict the next one (like reading a small snippet of text)*

- **Batch Size**: 32  
  *The model processes 32 different text examples in parallel to learn more efficiently*

- **Training Length**: 1000 + 800 epochs  
  *The model went through the training dataset 1,800 times to learn patterns*

- **Attention Heads**: 8  
  *The model has 8 different "ways of focusing" on the input text*

- **Model Layers**: 4  
  *The model processes information through 4 successive layers*

---

## ⚙️ How It Works

This model uses a **Transformer architecture**, similar to (but much smaller than) models like GPT.

### Processing Steps:

1. Text is broken down into individual characters  
2. Each character is converted to a numerical representation  
3. The model processes these through 4 layers with 8 attention heads  
4. For any sequence of 16 characters, the model predicts what comes next  
5. During generation, this prediction is used to create new text one character at a time  

---

## 🚀 Using the Model

Run the following to generate text:

```bash
# Generate text after training
generated_text = generate(model, starting_text="Once upon a time", max_new_chars=200)
