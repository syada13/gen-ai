#!/usr/bin/env python
# coding: utf-8

from helper_functions import *
journal = read_journal("journal_entries/cape_town.txt") 
print(journal)

# As you can see, there is a lot of text, and finding the important information can take some time. You can use LLMs to highlight the important information for you. For instance, the restaurants and their specialties.
prompt = f"""
Given the following journal entry from a food critic, identify the restaurants and their specialties.
For each restaurant, highlight its name and specialties in bold and use different colors for each.
Provide the output as HTML suitable for display in a Jupyter notebook.

Journal entry:
{journal}
"""
html_response = get_llm_response(prompt)
display_html(html_response)


