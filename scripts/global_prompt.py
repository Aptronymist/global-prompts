import modules.scripts as scripts
import gradio as gr

from modules.processing import StableDiffusionProcessing


class ExtensionTemplateScript(scripts.Script):

  def title(self):
          return "Global Prompts"

  def show(self, is_img2img):
    return scripts.AlwaysVisible

  def ui(self, is_img2img):
    with gr.Accordion('Global Prompts', open=False):
      with gr.Row():
        enabled = gr.Checkbox(False, label="Enable")

      with gr.Row():
        prePositive = gr.Textbox(
                info="Inserted before the main prompt",
                label= "Positive Prefix",
                lines=3,
                value=""
                )
        postPositive = gr.Textbox(
                info="Inserted after the main prompt",
                label= "Positive Postfix",
                lines=3,
                value=""
                )
        
      with gr.Row():
        preNegative = gr.Textbox(
                info="Inserted before the main negative prompt",
                label= "Negative Prefix",
                lines=3,
                value=""
                )
        postNegative = gr.Textbox(
                info="Inserted after the negative prompt",
                label= "Negative Postfix",
                lines=3,
                value=""
                )

    return [enabled, prePositive, postPositive, preNegative, postNegative]

  def process(self, p: StableDiffusionProcessing, enabled, prePositive, postPositive, preNegative, postNegative):

    if not enabled:
       return

    prompt = p.prompt
    negative_prompt = p.negative_prompt

    if prePositive:
      prompt = f"{prePositive}, {prompt}"
    if postPositive:
      prompt = f"{prompt}, {postPositive}"

    if preNegative:
      negative_prompt = f"{preNegative}, {negative_prompt}"
    if postNegative:
      negative_prompt = f"{negative_prompt}, {postNegative}"

    p.all_prompts[0] = prompt
    p.all_negative_prompts[0] = negative_prompt
