'''
Created on Nov 3, 2015
I will create make functions for each of the 5 dictionaries necessary to store the tk.StringVar()'s for all the options
associated with each command line tool. These dictionaries are the 'wiring' hooking up each widget so that when the BLAST
button is pressed all the information on the page can be collected and sent to subprocess. Also, these dictionaries will allow
state information to be saved when flipping between the blast suite pages.

Supplemental list's, dictionaries and functions will also be here.
@author: Lathian
'''
import tkinter as tk

#The index of this list is the number that needs to be passed to the command line
#Options 6, 7, and 10 can be additionally configured to produce so I'm going to need to bind <<ComboboxSelected>> to handle it
blastn_outputfmt = ['pairwise'  , 'query-anchored showing identities'  , 'query-anchored no identities'  , 
                    'flat query-anchored, show identities'  , 'flat query-anchored, no identities'  , 'XML Blast output'  , 
                    'tabular'  , 'tabular with comment lines'  , 'Text ASN.1'  , 'Binary ASN.1'  , 'Comma-separated values'  , 
                    'BLAST archive format (ASN.1)'  , 'JSON Seqalign output'  , 'JSON Blast output'  , 'XML2 Blast output']
""" Just checking I did my regex correctly 
for i, val in enumerate(blastn_outputfmt):
    print(str(i) +'  '+val)
"""
# A dictionary containing all the valid options for the blastn command line tool. Note -h, -help, -version might need to be
# removed.
blastn_dict = { '-h' : None, '-help' : None, '-import_search_strategy' : None,
    '-export_search_strategy' : None, '-task_name' : None, '-db_name' : None,
    '-dbsize_letters' : None, '-gilist' : None, '-seqidlist' : None,
    '-negative_gilist' : None, '-entrez_query_query' : None,
    '-db_soft_mask_algorithm' : None, '-db_hard_mask_algorithm' : None,
    '-subject_input_file' : None, '-subject_loc' : None, '-query_file' : None,
    '-out_file' : None, '-evalue' : None, '-word_size_value' : None,
    '-gapopen_penalty' : None, '-gapextend_penalty' : None,
    '-perc_identity_value' : None, '-qcov_hsp_perc_value' : None,
    '-max_hsps_value' : None, '-xdrop_ungap_value' : None, '-xdrop_gap_value' : None,
    '-xdrop_gap_final_value' : None, '-searchsp_value' : None,
    '-sum_stats_value' : None, '-penalty' : None, '-reward' : None, '-no_greedy' : None,
    '-min_raw_gapped_score_value' : None, '-template_type' : None,
    '-template_length_value' : None, '-dust_options' : None,
    '-filtering_db_database' : None,
    '-window_masker_taxid_masker_taxid' : None,
    '-window_masker_db_masker_db' : None, '-soft_masking_masking' : None,
    '-ungapped' : None, '-culling_limit_value' : None, '-best_hit_overhang_value' : None,
    '-best_hit_score_edge_value' : None, '-window_size_value' : None,
    '-off_diagonal_range_value' : None, '-use_index' : None, '-index_name' : None,
    '-lcase_masking' : None, '-query_loc' : None, '-strand' : None, '-parse_deflines' : None,
    '-outfmt' : None, '-show_gis' : None, '-num_descriptions_value' : None,
    '-num_alignments_value' : None, '-line_length_length' : None, '-html' : None,
    '-max_target_seqs_sequences' : None, '-num_threads_value' : None, '-remote' : None,
    '-version' : None, }

def makeBlastnOptionDict (dictionary):
    """Loads tkinter String Variables (StringVar) as the values of the option dictionary. Mostly there is a one to one
    mapping of each dictionary key to each GUI widget. When the BLAST button if pressed stepping through this dictionary
    will give the data necessary to pass to the command line tool."""
    for opt in dictionary:
        dictionary[opt] = tk.StringVar()
    return dictionary