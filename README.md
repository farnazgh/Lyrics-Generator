# Lyrics-Generator
(group project)

Develop a Python-based program which is able to
generate human-like song lyrics that mimic a specific genre

We used a sub-part of a large dataset of song lyrics containing only Folk/Country
lyrics in order to build a language model that generates song lyrics that resemble
this genre. Some data cleaning was performed prior to training the models.

As a first approach, we went for a word-based Long Short Term Memory
(LSTM) model. However, training this model turned out to be computationally
expensive. We had to train the model using a smaller part of our corpus and/or a
relatively small number of epochs. The results were unsatisfying.

Consequently, we opted for a simpler N-gram language model that could be
trained on our entire corpus. We built two unsmoothed maximum-likelihood
language models: a character-based model and a word-based model.

**Character-based Model**<br>
sample generated lyric: <br>
me and you/
you can see/
there’re holes in the silence/
and we all belong to the song of peace/
at the home of willie’s winter love but I call it trouble/
and then some/
’cause it’s changing us for money I do/
she’s got to be honest/
its better with my heart healed/
an old legend of a midnight angel, black angel/
on high with nothing left but empty shell inside/
?cause the road is looking for something about ya makes me know that soon he/
would know that you’ve been good to you/
lips would tell a mind/
she wakes me, she does’t love you love me/
I start to kissing you to stay/
last night I take the jib sail down the road/
to pick love up where you lift me up/
aw!, you could make you feelin’ again/
when once again in twenty-seven shows in twenty years/
I’ll give you ever gonna be a little longer/
wish it was/
a lot of room/
now don’t say maybe can’t you see I’ve thought of your favor/
reachin’ to be hard to find/
you’re here with me

**Word-based Model**<br>
sample generated lyric: <br>
remember when I awaken from my trembling spirit fly/
we somehow came together/
I know that you ’d always bring me a briar and twist it in a private jet,/
and no one ’s at hand/
and the good, do n’t/
I ’m going back,/
I would be saved and locked away/
it brings, ris ’ n the rain came pourindown/
pretty women that had dissatisfied you/
love is such a woman, child,/
that hammer down, I ’m happy

**Libraries**<br>
Grammar-check, NLTK, KenLM
