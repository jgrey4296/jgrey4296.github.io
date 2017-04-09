from doctester import Document, DocTestRunner, DocException, SizedShould

# Setup root_logger:
import logging as root_logger
LOGLEVEL = root_logger.DEBUG
LOG_FILE_NAME = "DocTestExample.log"
root_logger.basicConfig(filename=LOG_FILE_NAME, level=LOGLEVEL, filemode='w')

console = root_logger.StreamHandler()
console.setLevel(root_logger.INFO)
root_logger.getLogger('').addHandler(console)
logging = root_logger.getLogger(__name__)
##############################

#doctester non-terminals: have, a, near, come, after, use, at, than at
#doctester terminals: mention, cite, precede, section, chapter, tag, regex,
#paragraphs, sentences, words, citations, 
#comparisons: larger, smaller, equal, least, most



class DocTests(DocTestRunner):

    def __init__(self):
        super().__init__()
        self.d = Document('./chapters')
 
    def test_chapters(self):
        self.d.should.have.chapter('Introduction')

    def test_intro_structure(self):
        intro = self.d.chapter('Introduction')
        intro.should.have.subsections(5)
        intro.should.have.section('Motivation')
        intro.should.have.section('Current Limitations of media')
        intro.should.have.section('Vignettes')
        intro.should.have.section('Research Questions')
        intro.should.have.section('Conclusion')
        
        intro.section('Motivation').should.precede('Research Questions')
        all([x.should.precede('Conclusion') for x in intro.sections() if not x.titleIs('conclusion')])

    def test_research_questions(self):
        researchQs = self.d.chapter('Introduction').section('Research Questions')
        researchQs.should.have.tag('instStructure')
        researchQs.should.have.tag('instChange')
        
    def test_mentions_and_citations(self):
        intro = self.d.chapter('Introduction')
        #People:
        intro.should.mention('Graeber')
        intro.should.mention('Bicchieri')
        intro.should.mention('Vi Hart')
        #Concepts
        intro.should.mention('Games')
        intro.should.mention('Explorables')
        intro.should.mention('Norms')
        #Games:
        intro.should.mention('Tyranny')

        

    def test_lengths(self):
        SizedShould.WordsInAPage = 50
        self.d.should.have.length.larger.than(2).pages()
        for chapter in self.d.chapters():
            chapter.should.have.length.larger.than(5).paragraphs()

        intro = self.d.chapter('Introduction')
        for section in intro.sections():
            section.should.have.length.at.least(1).paragraphs()
            
        #intro.section('Research Questions').should.have.length.at.most(4).paragraphs()
        #self.d.should.have.length.larger.than(10).sentences()

        
##############################
if __name__ == '__main__':
    logging.info("Setting up")
    runner = DocTests()
    runner()
