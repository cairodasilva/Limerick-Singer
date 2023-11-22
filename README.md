# poetry-generator


1. **Download all of the necessary elements**
   - pip install spotify
   - pip install py3-tts
   - pip install spacy
   - pip install lyricsgenius
   - pip install spotipy
2. **How to run**
   - from terminal cd in poetry-generator (or what the file is saved as)
   - run main.py by running python3 ./main.py
   - select if you want to generate a new poem or say an old one ( to say an old poem you have to cd into previous_poems and look at all of the previous ones)
   - if you select generate give it the number of generations you want(3-4 is optimal) and the song name and title
   - if you select recite give it the filename of the poem you want, as long it's in previous_poems
3. **Description**
   This poem uses a genetic algorithm to create limericks based off of a song the user inputs. It makes limericks that have five lines, an AABBA rhyme scheme, an anapestic trimeter and are usually funny and lighthearted. The generator uses the nouns and verbs in the song as well as the valence (which is a rating of a song's positivity from 0 to 1 based on lyrics and sound) of the song to mutate on an inspiring set of limericks. It's  mutations are changing a rhyme word to another word that rhymes, swapping a noun from the song with a similar noun from the poem and swapping a verb from the song with a similar verb from the poem. It selects poems based on how well it aligns with the rules of limericks and how well it aligns with the lyrics and valence of the song.
4. **Inspiring Research**
   There were a few published papers I used to help inspire this project, the first one used an Finite state automata to fit the rhyme and meter requirements and an RNN to calculate fitness(Ghazvininejad et al, 2016). While I didn't use their exact techniques, I used the same idea to first get all of the rhyme words and then make poems off of those. However, their model selects for rhyme words that are closer to the inputted topic while mine selected rhyme words that are closer to the rhyme structure of the poem to rhyme scheme of the limerick at the expense of coherence. The next paper used a genetic algorithm, but prioritzed meaning over meter and scheme. However, they used a tree adjoining grammar to generate sentences and mutated those trees based on possible ways a sentence structure could change(Manurung et al., 2012). This method allows for much more coherence, but doesn't allow for new sentence structures to be made which is a key part of poetry as poems aren't restricted by linguistic rules. A good introduction to poetry generation and all of the ways poems could be made was Hugo Olivera's PoeTryMe model which outlines multiple strategies for generating and evaluating poems in portuguese, however many of them were outside of the scope of this project(Olivera, 2012).
5. **Challenges as a programmer**
I learned a lot about NLP and other APIs that can be used to generate and evaluate sentences. Even if I didn't use them, I learned a lot about spacy matching and pipelines.
I learned a lot about word matrices from the spacy similarity function, but I want to learn more about sentence embeddings and how to use other matrix based embeddings and well as how matrices can be used to represent text among other things.
I also challenged myself a lot in trying a lot of things that I didn't end up implementing ie. Noun chunks, webscraping, using the popularity of google searches for each line or noun chunk.
6. **Ways I could improve**
   I think one big way I could improve would by using sentence embeddings trained on a maybe that artists lyrics or another model and use those to evaluate how fit a replacement is. With a genetic algoritm, there are only so many ways a line can be mutated, but with sentence embeddings, sentences can be made from scratch and using an inspiring set of a poems as well as a song lyric a much more broad range of poem lines can be made that still fit the scheme of a limerick
			
8. **Citations**
   Ghazvininejad, M., Shi, X., Choi, Y., & Knight, K. (2016, November). Generating topical poetry. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (pp. 1183-1191).
   
   Manurung, R., Ritchie, G., & Thompson, H. (2012). Using genetic algorithms to create meaningful poetic text. Journal of Experimental & Theoretical Artificial Intelligence, 24(1), 43-64.
   
   Oliveira, H. G. (2012). PoeTryMe: a versatile platform for poetry generation. Computational Creativity, Concept Invention, and General Intelligence, 1, 21.
