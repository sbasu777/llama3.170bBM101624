{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Hypothetical inference time (in seconds) for processing a long context window of 4096 input tokens and 512 output tokens\
# for each GPU configuration\
\
# Context window size is fixed as per our scenario (4096 input tokens + 512 output tokens = 4608 tokens total)\
context_window_size = 4608  # total tokens\
\
# Hypothetical inference times (in seconds) for each GPU configuration\
# Assuming the multi-GPU H100 setup achieves the best (fastest) times\
# Values reflect relative speeds with multi H100 taking the least time\
a100_40gb_time = 60         # Longest time due to memory and processing limitations\
a100_80gb_time = 40         # Faster but limited by A100 architecture\
single_h100_80gb_time = 25  # Faster due to H100 architecture\
multi_h100_80gb_time = 15   # Fastest due to parallel processing\
\
# List of configurations and corresponding inference times\
configs = ['A100 40GB', 'A100 80GB', 'Single H100 80GB', 'Multi H100 80GB']\
inference_times = [a100_40gb_time, a100_80gb_time, single_h100_80gb_time, multi_h100_80gb_time]\
\
# Plotting the bar chart\
plt.figure(figsize=(10, 6))\
plt.bar(configs, inference_times, color=['blue', 'green', 'red', 'purple'], edgecolor='grey')\
plt.xlabel('GPU Configurations', fontweight='bold')\
plt.ylabel('Inference Time (seconds)', fontweight='bold')\
plt.title(f'Inference Time Across GPU Configurations\\nfor \{context_window_size\}-Token Context Window', fontweight='bold')\
plt.ylim(0, 70)  # Setting a consistent y-axis limit for clear comparison\
\
# Display the chart\
plt.tight_layout()\
plt.show()\
}