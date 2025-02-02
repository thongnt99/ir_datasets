import re
import unittest
from ir_datasets.formats import TrecQrel
from ir_datasets.datasets.trec_fair_2021 import FairTrecDoc, FairTrecQuery, FairTrecEvalQuery
from .base import DatasetIntegrationTest


class TestFairTrec(DatasetIntegrationTest):
    def test_docs(self):
        self._test_docs('trec-fair-2021', count=6280328, items={
            0: FairTrecDoc('12', 'Anarchism', re.compile('^\n\n\n\n\n\n\n\n\nAnarchism is a political philosophy and movement that is sceptical of authority and rejects.{46355}ance without government\n\n\nList of anarchist political ideologies\n\n\nList of books about anarchism\n\n\n\n$', flags=48), re.compile('^\\{\\{short description\\|Political philosophy and movement\\}\\}\n\\{\\{redirect2\\|Anarchist\\|Anarchists\\|other uses\\|.{96002}al movements\\]\\]\n\\[\\[Category:Political ideologies\\]\\]\n\\[\\[Category:Social theories\\]\\]\n\\[\\[Category:Socialism\\]\\]$', flags=48), 'https://en.wikipedia.org/wiki/Anarchism', 0.909, [], 'FA'),
            9: FairTrecDoc('316', 'Academy Award for Best Production Design', re.compile("^\n\n\nThe Academy Award for Best Production Design recognizes achievement for art direction in film\\. Th.{829} Award for Best Production Design\n\n\nCritics' Choice Movie Award for Best Art Direction\n\n\n\nNotes\n\n\n\n\n$", flags=48), re.compile('^\\{\\{Use mdy dates\\|date=June 2013\\}\\}\n\\{\\{Infobox award\n\\| name      = Academy Award for Best Production Des.{97494}\\]\n\\[\\[Category:Best Art Direction Academy Award winners\\|\\*\\]\\]\n\\[\\[Category:Awards for best art direction\\]\\]$', flags=48), 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Production_Design', 0.67862654, ['Northern America'], 'GA'),
            6280327: FairTrecDoc('67277921', 'Oldřich I of Rosenberg', re.compile('^\n\n\n\nOldřich I of Rosenberg \\(died 4 March 1390\\) was the fourth son of the Peter I of Rosenberg and hi.{345}II, Duke of Austria\\. The dispute was eventually mediated by Czech King Wenceslas IV\\.\n\nCitations\n\n\n\n\n$', flags=48), re.compile('^\\{\\{inline\\|date=April 2021\\}\\}\n\\{\\{short description\\|14th\\-century Bohemian nobleman\\}\\}\n\\{\\{Infobox noble\\|type.{3160}gory:1390 deaths\\]\\]\n\\[\\[Category:14th\\-century Bohemian people\\]\\]\n\\[\\[Category:Medieval Bohemian nobility\\]\\]$', flags=48), 'https://en.wikipedia.org/wiki/Oldřich_I_of_Rosenberg', 0.55746955, ['Europe'], 'B'),
        })

    def test_queries(self):
        self._test_queries('trec-fair-2021/train', count=57, items={
            0: FairTrecQuery('1', 'Agriculture', ['agriculture', 'crops', 'livestock', 'forests', 'farming'], 'This WikiProject strives to develop and improve articles at Wikipedia related to crop production, livestock management, aquaculture, dairy farming and forest management. The project also covers related areas, including both governmental and NGO regulatory agencies, agribusiness, support agencies such as 4H, agricultural products including fertilizers and herbicides, pest management, veterinary medicine and farming equipment and facilities.', 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Agriculture'),
            9: FairTrecQuery('10', 'Buddhism', ['buddhism', 'buddha', 'buddhist', 'buddhist temple', 'gautama buddha', 'monk'], 'WikiProject Buddhism is a group of people dedicated to improving Buddhism-related contents in Wikipedia.', 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Buddhism'),
            56: FairTrecQuery('57', 'Nigeria', ['nigeria', 'nigerians', 'nigerian languages', 'nigerian history'], 'This WikiProject aims to help coordinate efforts to improve and maintain pages related to: Nigeria, the history of Nigeria, languages of Nigeria, Nigerians, Local government areas of Nigeria', 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Nigeria'),
        })
        self._test_queries('trec-fair-2021/eval', count=49, items={
            0: FairTrecEvalQuery('101', 'Mathematicians', ['mathematician', 'arithmetician', 'trigonometrician', 'geometer', 'algebraist', 'statistician', 'geometrician', 'number theorist'], 'WikiProject Mathematicians aims to improve Wikipedia coverage of all articles on persons that have notable achievements in the field of mathematics.'),
            9: FairTrecEvalQuery('110', 'Clean Energy', ['clean energy', 'sustainable energy', 'renewable energy', 'emissions', 'carbon capture', 'carbon storage'], 'Wikiproject Clean Energy aims to improve Wikipedia coverage of all aspects relating to sustainable and renewable energy sources, such as wind, hydro, solar and geothermal energy.'),
            48: FairTrecEvalQuery('150', 'Street Art', ['street art', 'street performance', 'graffiti', 'busking'], 'This WikiProject aims to improve the coverage and quality of Wikipedia articles relating to street art and its creators. We are interested in both static street art, such as graffiti and murals, and dynamic street performances and theater. Both authorized and unauthorized art is in our scope.'),
        })

    def test_qrels(self):
        self._test_qrels('trec-fair-2021/train', count=2185446, items={
            0: TrecQrel("1", "572", 1, "0"),
            9: TrecQrel("1", "4514", 1, "0"),
            2185445: TrecQrel("57", "67253426", 1, "0"),
        })


if __name__ == '__main__':
    unittest.main()
