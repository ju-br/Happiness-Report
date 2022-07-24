# Are you happy? 
<p align="center">
    <iframe src="https://giphy.com/embed/chzz1FQgqhytWRWbp3" width="150" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/minions-minions-2-rise-of-gru-chzz1FQgqhytWRWbp3"></a></p>
</p>

**The World Happiness Report (WHR) claims that:**<p>
<div align="center"> The true measure of progress is the happiness of the people; that happiness can be measured; and that we know a lot about what causes it. Given this knowledge, it is now possible for policy-makers to make people’s happiness the goal of their policies. And each of us can live a wiser life.</div>
<p align="center">
<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" width="40" height="40" />
</p>


5 latent (psychological variables) are assessed:
1. Happiness:
           <p> “Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. The top of the ladder represents the best possible life for you and the bottom of the ladder represents the worst possible life for you. On which step of the ladder would you say you personally feel you stand at this time?”
           </p> 
 2. Social Support
           <p> “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”
           Response scale: O e 1.
             </p> 
3. Freedom to make life choices
           <p> “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”
            Response scale: O e 1.
              </p> 
4. Generosity
            <p> “Have you donated money to a charity in the past month?”
            Generosity is the residual of regressing national average of response to the GWP question “Have you donated money to a charity in the past month?” on GDP per capita
              </p> 
5. Perception of Corruption:
            <p>  “Is corruption widespread throughout the government or not” and “Is corruption widespread within businesses or not?” The overall perception is just the average of the two 0-or-1 responses.
             </p>

 Additionaly, *gdp per capta* and *healthy life expectancy at birth* are also assed.

## Exploratory analysis
### Distribution of WHP variables per continent
![distribution] (https://github.com/ju-br/World-Happiness-Project2/blob/main/figures/Life%20ladder.png?raw=true)

![distribution] (https://github.com/ju-br/World-Happiness-Project2/blob/main/figures/Freedom%20to%20make%20choices.png)

![distribution] (https://github.com/ju-br/World-Happiness-Project2/blob/main/figures/Freedom%20to%20make%20choices.png)


### Correlations between WHP variables
The variables of the WHR are either strongly correlated (*log gdp per capta*,*social support*,*life expectancy*) or moderated correlated (*freedom to make choices*, *negative affect*, *positive affect*, and *corruption*). Generosity is weakly correlated and is the only one in the reverse direction than expected.
<p> 

![correlation WHP] (https://github.com/ju-br/World-Happiness-Project2/blob/main/figures/correlation%20heatmap%20happiness.png)
</p>

### Correlations between happiness and data from other sources
![correlation] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

However, when we are measuring latent variables we have to be sure that we are measuring what we want to assess.
<div align="center">

## Can we trust this data?
</div>

### How to measure latent variables?
As latent variables cannot be observed, there are some criteria that should be met:<p>

  **1. Multiple items to operationalize:**</p>
       <p>Life ladder ❌
       <p>Social Support ❌
      <p>Corruption ❌
       <p>Freedom of choice ❌
      <p>Generosity ❌
  **WHP:** latent variables measured with a single item

*With one item you cannot check reliability statistics*
</p>

 **2. To aggregate data, in a higher level, measured with a different referent we need to check if the higher level influence (country) the smaller one(person). Aggregation statistics:**
 </p>
<p>Icc 1 - Percentage of aggregated influence of country level on person ❌
<p>ANOVA - variance between countries ❌
<p>ADI - agreement within countries ❌
<p>Alternative: multilevel measure ❌
</p>
 **WHP:** average national response of the overall perception at the individual level

**3. Content validity:** 
Refers to how well a survey or test measures the construct that it sets out to measure.
       <p>Life ladder ❌
       <p>Social Support :white_check_mark:
      <p>Corruption :white_check_mark:
       <p>Freedom of choice :white_check_mark:
      <p>Generosity ❌

**4. Criterion validity:** 
Criterion validity indicates how well the scores or responses of a test converge with criterion variables with which the test is supposed to converge.
<p>

Life ladder - inequality :white_check_mark:


![ladder-inequality] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

<p>

Life ladder - depression :white_check_mark:

![ladder-depression] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

<p>Life ladder - alcohol use ❌

![ladder-alcohol] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

<p>Life ladder - drug use ❌

![ladder-drug] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

<p>Life ladder - anxiety  ❌

![ladder-anxiety] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

<p>Life ladder - suicide  ❌

![ladder-suicide] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

*It might be the case the latent variables within WHR are highly correlated due to self report bias*

<p>Curiosity: Life ladder - temperature  (omitted variable?)❌

![ladder-temperature] (/Users/Juliana/Desktop/Ironhack/Projects/World-Happiness-Project2/figures/correlation heatmap happiness.png)

</p>

### Can we say all the countries agree in what is happiness?
Cross-cultural explorations reveal varying, multiple and often conflicting
beliefs within and between groups. Happiness research has been criticised 
for producing not simply descriptive but prescriptive accounts based 
upon unacknowledged value judgments and (western) social norms.

Moreover, to attest that all countries have the same perception and, therefore, their scores are comparable,
measurement invariance should be evaluated.

   ### Is this evidence strong enough to base public policies?
In recent years, interest in happiness has been growing across numerous disciplines, particularly
in the fields of psychology and economics. It has also become an increasingly significant object
of public policy both domestically and internationally with governments around the world considering
measures of happiness, or ‘subjective well-being,’ as progress indicators and tools for appraising
policy. Yet, the findings from happiness surveys are nonetheless often taken to be data
about an objectively verifiable construct (rather than a socially mediated expression
of feelings), and are used to issue advice to governments about policies that should maximise
happiness’ (Duncan 2005). This, according to Jugureanu et al., (2014), is the ‘axiomatic error’
of happiness studies: ‘the search for an eternal, unchanging, all-encompassing definition of happiness
involves the epistemological fallacy that happiness “has” a kind of essence that can be rendered
conceptually. However, there is often mixed, weak or inadequate evidence to support frequent
claims. Further problems are: claims and activities of advocacy
groups are often cited as ‘research evidence’ (Ecclestone 2007:460), conclusions drawn from
findings not replicated in subsequent research (Freese et al. 2007; Lazarus 2003b; Mongrain
and Anselmo-Matthews 2012)5 or extrapolated from small studies or unrepresentative groups
(Fitzpatrick 2006; Miller 2008; Morrall 2009), and correlations treated causally (Ehrenreich
2009, Miller 2008; Saunders and Evans 2010).

## Why people data, in general, is not reliable?
 The majority of variables of interest focus on abstract phenomena and one cannot measure them directly (e.g. job engagement). In order to subsidize strategic decision making, the ability to choose or develop assessments valid and reliable data is an essential capability to be successful. Using validated measures is the safest and more economical choice. They are more reliable and developed following a strict process. An alternative to finding such measures is the Academy of Management Measurement Chest. Problems with measures’ reliability and validity often lead to unreliable metrics. For example, usually, in-house solutions are developed without a rigorous literature review to define the phenomena and to formulate items.

For more about why HR measures fail: [https://www.aihr.com/blog/in-house-hr-assessment/?utm_source=linkedin&utm_medium=social&utm_campaign=blog&utm_content=a-hr-assessment]

For more on measurement developments: [https://link.springer.com/article/10.1007/s10551-021-04864-7]