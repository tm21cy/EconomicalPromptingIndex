# The Economical Prompting Index - Data and Calculation Tools
This repository contains the detailed model interactions and Python-based calculation program used for the paper *Can We Afford The Perfect Prompt? Balancing Cost and Accuracy with the Economical Prompting Index*. This work will be published in the 31st International Conference on Computational Linguistics in January of 2025.

Authors: Tyler McDonald, Anthony Colosimo, Yifeng Li, Ali Emami
## Paper Abstract
As prompt engineering research rapidly evolves, evaluations beyond accuracy are crucial for developing cost-effective techniques. We present the Economical Prompting Index (EPI), a novel metric that combines accuracy scores with token consumption, adjusted by a user-specified cost concern level to reflect different resource constraints. Our study examines 6 advanced prompting techniques, including Chain-of-Thought, Self-Consistency, and Tree of Thoughts, across 10 widely-used language models and 4 diverse datasets. We demonstrate that approaches such as Self-Consistency often provide statistically insignificant gains while becoming cost-prohibitive. For example, on high-performing models like Claude 3.5 Sonnet, the EPI of simpler techniques like Chain-of-Thought (0.72) surpasses more complex methods like Self-Consistency (0.64) at slight cost concern levels. Our findings suggest a reevaluation of complex prompting strategies in resource-constrained scenarios, potentially reshaping future research priorities and improving cost-effectiveness for end-users.
## File Structure
The folder `Model_Interaction_Data` contains the sampled outputs from the employed testing suite of both closed- and open-source Large Language Models as described in the Experimental Setup section.

The folder `Interaction_Code` contains the Python program for calculating individual EPI values, for use in conveniently exploring the behavior of the EPI given custom inputs of accuracy and token count. 
## Operation Instructions
The `Interaction_Code/EPI_score_calculator.py` file can be run simply with `python EPI_score_calculator.py`. After initializing, the program will request the desired accuracy, token count, and preset Cost Concern class, before outputting a final EPI score. The `weight_mapping` dictionary can be altered at your discretion to present additional Cost Concern classes.
## Citation
*To be included.*
