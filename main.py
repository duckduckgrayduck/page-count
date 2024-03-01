"""
Simple Add-On to count the number of pages in a document set
"""

from documentcloud.addon import AddOn


class PageCounter(AddOn):
    """Counts pages in a document set and displays it"""

    def main(self):
        """ For each page take the page count and add it to tally"""
        page_count=0

        # add a hello note to the first page of each selected document
        for document in self.get_documents():
            page_count += document.page_count
        self.set_message(f"This document set is comprised of {page_count} pages")

if __name__ == "__main__":
    PageCounter().main()
