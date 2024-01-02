import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file, xml_file):
    # Create the root of the XML
    root = ET.Element('Folders')

    # Read the CSV file
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Create a folder element for each row
            folder = ET.SubElement(root, 'Folder')
            
            # Add child elements for Filepath, Identity, and Filesystemrights
            ET.SubElement(folder, 'Filepath').text = row.get('Filepath', '')
            ET.SubElement(folder, 'Identity').text = row.get('Identity', '')
            ET.SubElement(folder, 'Filesystemrights').text = row.get('Filesystemrights', '')

    # Write the XML to a file
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

# Example usage
csv_file = r'FILEPATH'  # Replace with your CSV file path
xml_file = r'OUTPUTPATH'         # Output XML file path
csv_to_xml(csv_file, xml_file)
