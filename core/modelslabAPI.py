import requests
import json
import time
import os

API_KEY = os.environ['MODELSLAB_API_KEY']

def controlnet_api(input_img_url, p_prompt, n_prompt):

    p_prompt = "professional photograph, high quality, film grain, Fujifilm XT3, ultra high resolution"
    n_prompt = "pencil sketch, cartoon, illustration, 3d render, cgi, anime, drawing, sketch, painting, animation, low resolution, low quality, low detail, disfigured, bad anatomy"
    api_endpoint = "https://modelslab.com/api/v5/controlnet"
    key = f"{API_KEY}" #mashudhassandev api key

    payload = json.dumps({
            "key": key,
            "controlnet_model": "canny,scribble",
            "controlnet_type": "scribble",
            "model_id": "realistic-vision-51",
            "auto_hint": "yes",
            "guess_mode": "no",
            "prompt": p_prompt,
            # "a model mugshot, ultra high resolution, 4K image"
            "negative_prompt": n_prompt,
            # + "cartoon, illustration, anime, drawing, grayscale",
            "init_image": input_img_url,
            "mask_image": None,
            "width": "512",
            "height": "512",
            "samples": "1",
            "scheduler": "UniPCMultistepScheduler",
            "num_inference_steps": "30",
            "safety_checker": "no",
            "enhance_prompt": "yes",
            "guidance_scale": 7.5,
            # "controlnet_conditioning_scale": 3,
            "strength": 1,
            "lora_model": None,
            "tomesd": "yes",
            "use_karras_sigmas": "yes",
            "vae": None,
            "lora_strength": None,
            "embeddings_model": None,
            "seed": None,
            "webhook": None,
            "track_id": None
    })
    
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request('POST', url=api_endpoint, headers=headers, data=payload)
        json_response = response.json()
        pretty_json_response = json.dumps(json_response, indent=3)
        # output and future links are always list type
        output = json_response.get('output', '')
        future_links = json_response.get('future_links', '')
        error_msg = json_response.get('message', '')

        if output:
            print("\n", "<=== JsonResponse ===>", "\n", pretty_json_response)
            print("\n", "<=== Generated Image Url: ===>", "\n", output)
            return output[0], json_response
        
        elif future_links:
            wait_time = json_response.get('eta', 0) + 15 # Adding 15 seconds buffer time
            print("\n", "<=== JsonResponse ===>", "\n", pretty_json_response)
            print("\n", f"Waiting for {wait_time} seconds before fetching result...")
            time.sleep(wait_time)
            print("\n","<=== Fetched Future Image Url: ===>", "\n", future_links[0])
            return future_links[0], json_response
        
        elif error_msg:
            print("\n", "Output is empty. Trying to fetch result...")
            print("\n", "<== JsonResponse ==> ", "\n", pretty_json_response)
            print("\n", "<== Error ==> ", "\n", error_msg)
            return None, json_response

    except requests.RequestException as e:
        print(f'Request Failed: {e}')
        