# UQCS Subject Guide

[UQCS Subject Guide PDF](https://jenkins.trm.io/job/UQCS%20subject%20guide/ws/tex/_build/main.pdf)

## About

This project is designed to be be able to give students information about
subjects from the past generations. It also helps group subjects into groups
so that if an intended specification is wanted the student can easy plan it.

## Building

It is recommended to be using a linux environment to build this document 
with texlive-latex at v15 min. A docker file is also provided for being on
other platforms or in a sandboxed environment. Make is also required for 
convenience purposes.

To Build:

` make `

This will run pdflatex 4 to 5 times, the output can be found in tex/_build

To Clean:

` make clean `

## Contributing

To be able to contribute a review, atleast 3 other members must approve 
it (thumbsup or LGTM). This is to ensure that reviews are sanitised and 
are appropriate. Pull requests are the only method that contributions will
be accepted into the project.

### Creating a Review

#### The course file:

find the course you wish to review in `tex/courses/subjects`, if it 
 does not exist; copy one of the other course files and rename it 
 (keeping the code capitalised). 
 
To fill in the template please follow the guideline below:

- code: all caps e.g. `CSSE2002`
- title: the official course title e.g. `Programming in the Large`
- score: number between 0 - 5
- contact: comma separated number letter combinations e.g. `1L, 2T`
- cordinator: name of course coordinator
- assessment: & seperated information e.g. ` MyPyTutor & 10\% & Weekly online problems `
- review: your review goes here
- preparation: list of advice for the subject e.g. `\item buy the textbook`

#### Having trouble:

If you experience any issues or trouble please feel free to express these
to the community on our slack channel @ [https://slack.uqcs.org.au/](https://slack.uqcs.org.au/)