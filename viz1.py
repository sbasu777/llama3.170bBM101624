{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import matplotlib.pyplot as plt\
import numpy as np\
\
# Data for the visualization based on the comparisons discussed\
\
# Categories\
categories = ['Memory Usage (GB)', 'Performance (Relative Units)']\
\
# Values for A100 GPUs\
a100_40gb = [40, 60]  # 40GB VRAM; lower relative performance due to limitations\
a100_80gb = [80, 80]  # 80GB VRAM; moderate relative performance\
\
# Values for H100 GPUs\
single_h100_80gb = [80, 70]  # 80GB VRAM; decent performance but limited by single GPU\
multi_h100_80gb = [80, 100]  # Multi-GPU; better VRAM distribution and max performance\
\
# Bar Width\
bar_width = 0.2\
\
# Positions of bars\
r1 = np.arange(len(categories))\
r2 = [x + bar_width for x in r1]\
r3 = [x + bar_width for x in r2]\
r4 = [x + bar_width for x in r3]\
\
# Plotting\
plt.figure(figsize=(12, 8))\
\
# Bar charts for each setup\
plt.bar(r1, a100_40gb, color='blue', width=bar_width, edgecolor='grey', label='A100 40GB')\
plt.bar(r2, a100_80gb, color='green', width=bar_width, edgecolor='grey', label='A100 80GB')\
plt.bar(r3, single_h100_80gb, color='red', width=bar_width, edgecolor='grey', label='Single H100 80GB')\
plt.bar(r4, multi_h100_80gb, color='purple', width=bar_width, edgecolor='grey', label='Multiple H100 80GB')\
\
# Adding labels and title\
plt.xlabel('Factors', fontweight='bold')\
plt.ylabel('Values', fontweight='bold')\
plt.title('Comparative Analysis of GPU Configurations for LLaMA 70B Inference', fontweight='bold')\
plt.xticks([r + bar_width for r in range(len(categories))], categories)\
\
# Adding a legend\
plt.legend()\
\
# Displaying the plot\
plt.tight_layout()\
plt.show()\
}