#standalone app - output to file 
import os
import sys
from pypdf import PdfReader
import PyPDF2
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLineHorizontal

def parse_pdf(filename, output_file):
    reader = PdfReader(filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(f'\n{page.extract_text()}\n')

def extract_links_from_pdf(pdf_path, output_file):
    links = []
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num, page in enumerate(pdf_reader.pages):
            page_links = []
            if '/Annots' in page:
                annotations = page['/Annots']
                
                for annotation in annotations:
                    annotation_object = annotation.get_object()
                    
                    if annotation_object['/Subtype'] == '/Link':
                        if '/A' in annotation_object:
                            action = annotation_object['/A']
                            if '/URI' in action:
                                uri = action['/URI']
                                
                                if '/Rect' in annotation_object:
                                    rect = annotation_object['/Rect']
                                    x1, y1, x2, y2 = [float(coord) for coord in rect]
                                    
                                    page_links.append((uri, x1, y1, x2, y2))
            
            if page_links:
                page_text = extract_text_with_positions(pdf_path, page_num)
                links.extend(associate_text_with_links(page_text, page_links))
    
    merged_links = merge_adjacent_links(links)
    
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("\n---\n")
        for link, text in merged_links:
            f.write(f"Link Text: {text}\n")
            f.write(f"Link: {link}\n")
            f.write("---\n")

def extract_text_with_positions(pdf_path, page_num):
    text_with_positions = []
    for page_layout in extract_pages(pdf_path, page_numbers=[page_num]):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLineHorizontal):
                        for character in text_line:
                            if isinstance(character, LTChar):
                                text_with_positions.append((character.get_text(), character.x0, character.y1))
    return text_with_positions

def associate_text_with_links(page_text, page_links):
    associated_links = []
    for uri, x1, y1, x2, y2 in page_links:
        link_text = []
        for char, char_x, char_y in page_text:
            if x1 <= char_x <= x2 and y1 <= char_y <= y2:
                link_text.append(char)
        associated_links.append((uri, ''.join(link_text), y1))
    return associated_links

def merge_adjacent_links(links):
    merged_links = []
    current_url = None
    current_text = ""
    
    for url, text, _ in sorted(links, key=lambda x: (-x[2], x[0])):
        if url == current_url:
            current_text += " " + text
        else:
            if current_url:
                merged_links.append((current_url, current_text.strip()))
            current_url = url
            current_text = text
    
    if current_url:
        merged_links.append((current_url, current_text.strip()))
    
    return merged_links

def process_pdf(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_name = os.path.basename(pdf_path)
    output_file = os.path.join(output_dir, f"{os.path.splitext(pdf_name)[0]}.txt")
    
    parse_pdf(pdf_path, output_file)
    extract_links_from_pdf(pdf_path, output_file)

def find_data_directory():
    possible_locations = [
        os.path.join(os.getcwd(), 'data'),
        os.path.join(os.path.dirname(sys.executable), 'data'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'),
        os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'data'),
    ]
    
    for location in possible_locations:
        if os.path.exists(location):
            return location
    
    return None

def main():
    input_dir = find_data_directory()
    
    if input_dir is None:
        print("Error: Unable to find the 'data' directory. Please ensure it exists in the same directory as the executable or its parent directory.")
        print("Current working directory:", os.getcwd())
        print("Executable location:", sys.executable)
        return

    output_dir = os.path.join(os.path.dirname(input_dir), 'Output')
    
    print(f"Using data directory: {input_dir}")
    print(f"Output will be saved to: {output_dir}")

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in the '{input_dir}' directory.")
        return

    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        try:
            print(f"Processing {filename}...")
            process_pdf(pdf_path, output_dir)
            print(f"Finished processing {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            import traceback
            print(traceback.format_exc())

    print("All PDF files have been processed.")
    print(f"Output files can be found in: {output_dir}")

if __name__ == '__main__':
    main()