import pandas as pd
import re

def es_page_splitter(df, content_column, extension_column, split_no):
    """
    Overview: Explodes a dataframe using the content column. This essentially splits long text up into pages and adds a new row for each page.
    Date: 30/01/23

    Parameters:
        df: your dataframe that you want to explode
        content_column: the content you want to split into different rows
        extension_column: file type column for filtering
        split_no: number of words per row
    Returns: 
        df: processed dataframe
    To do:
        replace group by strings with extension_column
    """
    
    #keep only document files types
    ext_list = ['pdf', 'docx', 'doc', 'dot', 'dotm', 'dotx', 'html', 'htm', 'odt', 'pptx', 'pptm', 'ppt', 'xps', 'potm', 'poyt', 'ppsx', 'ppsm', 'pps', 'rtf', 'wps' ] #check your file type is included
    df = df[df[extension_column].isin(ext_list)].copy()
    
    
    #explode and group by
    df[content_column] = df[content_column].str.split(" ")
    df = df.explode(content_column).reset_index(drop=True)
    df = df.groupby([df.index // split_no, 'uuid', 'extension', 'name', 'path'], as_index=False)[content_column].agg(" ".join)
    
    #create new index
    df = df.reset_index(drop=True)
    df['id'] = df.index
    
    #turn back into dataframe
    df = pd.DataFrame(df)
    
    return df