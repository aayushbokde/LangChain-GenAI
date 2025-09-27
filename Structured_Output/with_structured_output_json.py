from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import Optional, Literal
import os
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model = 'models/gemini-flash-lite-latest',
    api_key=os.getenv("GOOGLE_API_KEY")
)


# data validation cannot be applied here
#create a schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}
structured_model = model.with_structured_output(json_schema)


result = structured_model.invoke("""

Apple's iPad lineup continues to dominate the tablet market in late 2025, offering a polished and powerful range of devices that cater to nearly every type of user. From the lightweight iPad Air, perfect for students and casual consumers, to the powerhouse iPad Pro, which now genuinely rivals laptops in performance, Apple has solidified the iPad as the go-to device for portable entertainment, creativity, and productivity. The seamless integration with the broader Apple ecosystem remains a cornerstone of its appeal, creating a user experience that is intuitive, secure, and incredibly fluid.

The iPad's strength lies in its incredible versatility, powered by Apple's custom silicon that handles demanding apps and games with ease. This raw performance is paired with a stunning Liquid Retina or XDR display, creating a brilliant canvas for media consumption and professional creative work. The experience is further elevated by a mature ecosystem of accessories, like the Apple Pencil and Magic Keyboard, which effectively transform the tablet into a dynamic tool for artists, writers, and students. Combined with its premium build quality, the iPad feels like a polished and capable device for a wide range of tasks.

Despite its capabilities, choosing an iPad requires careful consideration of its place in a user's workflow. The operating system, iPadOS, has made significant strides in productivity but still operates with certain constraints compared to a full desktop OS like macOS or Windows, particularly in areas like advanced file management and true multitasking. This distinction is crucial for those looking to completely replace a traditional laptop. Furthermore, the ecosystem comes at a premium, as the cost of the device and its key accessories can quickly approach high-end laptop territory.

Pros
Exceptional Performance: Apple's custom silicon chips deliver incredibly fast and fluid performance for apps and games.

Stunning Displays: The Liquid Retina and XDR screens are bright, color-accurate, and a joy to use.

Vast App Library: The App Store offers a massive selection of high-quality, tablet-optimized applications.

Versatile Accessories: The Apple Pencil and Magic Keyboard are best-in-class accessories that significantly boost productivity and creativity.

Premium Build Quality: iPads are well-built with high-end materials, feeling both durable and reliable.

Seamless Ecosystem Integration: Works flawlessly with other Apple devices like iPhone, Mac, and Apple Watch.

Cons
High Price Tag: The initial cost of an iPad, especially the Pro models, is significant.

Expensive Accessories: Essential accessories like the Pencil and Keyboard are sold separately and add a considerable amount to the overall cost.

iPadOS Limitations: The operating system is still not as capable as a full desktop OS for certain professional workflows and multitasking.

No Expandable Storage: You are locked into the storage configuration you buy, with no option for a MicroSD card.

Limited File Management: While improved, managing files is not as straightforward or powerful as on a Mac or PC.

review by : Aayush Bokde
""")


print(result)