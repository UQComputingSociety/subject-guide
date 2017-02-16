# UQCS Subject Guide

[UQCS Subject Guide PDF](https://jenkins.uqcs.org.au/job/subject-guide/lastSuccessfulBuild/artifact/tex/_build/main.pdf)

[![Build Status](https://jenkins.uqcs.org.au/buildStatus/icon?job=subject-guide)](https://jenkins.uqcs.org.au/job/subject-guide)

## About

This project is designed to give students information about courses taken by
past students. Courses are grouped into categories to help you pick courses
when specialising.

## Building

It is recommended to use a Linux environment to build this document with at 
least v15 of texlive-latex. A Dockerfile is also provided for building on
other platforms or in a sandboxed environment. Make is required for 
convenience purposes. TeXstudio and a recent version of MiKTeX work well on
Windows, simply open and build `main.tex`.

To Build:

` make `

This will run pdflatex 4 to 5 times, the output can be found in `tex/_build`

To Clean:

` make clean `

If you encounter build errors, ensure you have an up to date Latex compiler.

## Contributing

Pull requests are the only way to contribute to the project.
For a new course review to be accepted, at least 3 other members must approve 
it (thumbsup or LGTM). This is to ensure that reviews are appropriate and
correctly formatted.

### Creating a Review

#### The course file:

Find the course you wish to review in `tex/courses/subjects`, if it 
 does not exist; copy one of the other course files and rename it 
 (keeping the code capitalised). 
 
To fill in the template please follow the guideline below:

- **code**: all caps e.g. `CSSE2002`
- **title**: the official course title e.g. `Programming in the Large`
- **score**: number between 0 - 5
- **contact**: comma separated number letter combinations e.g. `1L, 2T` for
    one lecture, two tutorials
- **coordinator**: name of course coordinator
- **assessment**: `&` separated information of Name/Weighting/Description e.g.
    ` MyPyTutor & 10\% & Weekly online problems `
- **review**: your review
- **preparation**: list of advice for the subject e.g. `\item buy the textbook`

#### Having trouble:

If you have any problems or questions, drop by [our Slack channel](https://slack.uqcs.org.au/) and say hi!
