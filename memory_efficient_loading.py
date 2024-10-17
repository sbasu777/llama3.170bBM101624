{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Now, I'll proceed to convert the notebook content to a `.py` script,\
# and I'll make the variable name changes while providing the list of changes.\
\
# First, I'll initialize the list of variable names and write the code to the file.\
new_code = """\
# Memory Efficient Weight Loading Script\
\
from importlib.metadata import version\
import gc\
import time\
import torch\
import os\
import psutil\
from threading import Thread\
\
# Check version of required packages\
required_packages = ["torch"]\
for pkg in required_packages:\
    print(f"\{pkg\} version: \{version(pkg)\}")\
\
# Memory Tracking Functions\
def initialize_memory_tracking():\
    \\"\\"\\"Initialize GPU memory tracking.\\"\\"\\"\
    if torch.cuda.is_available():\
        torch.cuda.reset_peak_memory_stats()\
    else:\
        print("This script is intended for CUDA GPUs but CUDA is not available.")\
\
def display_gpu_memory_usage():\
    max_gpu_mem = torch.cuda.max_memory_allocated() / (1024 ** 3)\
    print(f"Max GPU memory allocated: \{max_gpu_mem:.1f\} GB")\
\
def memory_cleanup():\
    gc.collect()\
    torch.cuda.empty_cache()\
    time.sleep(3)\
    torch.cuda.reset_peak_memory_stats()\
    max_memory = torch.cuda.max_memory_allocated() / (1024 ** 3)\
    print(f"Max GPU memory allocated: \{max_memory:.1f\} GB")\
\
# Model Configurations\
from previous_chapters import GPTModel\
\
# Base Model Config\
base_model_config = \{\
    "vocab_size": 50257,\
    "context_length": 1024,\
    "drop_rate": 0.0,\
    "qkv_bias": True\
\}\
\
# GPT2 Model Configurations\
gpt2_configurations = \{\
    "gpt2-small (124M)": \{"emb_dim": 768, "n_layers": 12, "n_heads": 12\},\
    "gpt2-medium (355M)": \{"emb_dim": 1024, "n_layers": 24, "n_heads": 16\},\
    "gpt2-large (774M)": \{"emb_dim": 1280, "n_layers": 36, "n_heads": 20\},\
    "gpt2-xl (1558M)": \{"emb_dim": 1600, "n_layers": 48, "n_heads": 25\}\
\}\
\
# Selected Model\
selected_model = "gpt2-xl (1558M)"\
base_model_config.update(gpt2_configurations[selected_model])\
\
# Function for loading model weights\
def load_model_weights():\
    initialize_memory_tracking()\
    model_instance = GPTModel(base_model_config)\
    device_instance = torch.device("cuda")\
    model_instance.to(device_instance)\
\
    # Loading weights\
    model_instance.load_state_dict(torch.load("model.pth", map_location=device_instance, weights_only=True))\
    display_gpu_memory_usage()\
\
# Run Model\
load_model_weights()\
\
# Cleanup\
del model_instance\
memory_cleanup()\
\
"""\
\
# Variable name changes list\
variable_changes = \{\
    "pkgs": "required_packages",\
    "start_memory_tracking": "initialize_memory_tracking",\
    "print_memory_usage": "display_gpu_memory_usage",\
    "cleanup": "memory_cleanup",\
    "BASE_CONFIG": "base_model_config",\
    "model_configs": "gpt2_configurations",\
    "CHOOSE_MODEL": "selected_model",\
    "model": "model_instance",\
    "device": "device_instance"\
\}\
\
# Saving to a file\
file_path = "/mnt/data/memory_efficient_loading.py"\
with open(file_path, "w") as file:\
    file.write(new_code)\
\
# Displaying the path for the user and the changes\
file_path, variable_changes\
}