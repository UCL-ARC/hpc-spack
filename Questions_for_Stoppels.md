# Questions for Harmen Stoppels

A list of things to ask Harmen on his visit on 30 January 2022

## 1. Continuious Integration type workflow for providing updated versions of the stack

There is a suggestion for a periodic workflow at:  [Slack link](https://ucl-arc.slack.com/archives/G6E0K3ZGD/p1674475763789409)

- What does Harmen think of it?

## 2. How to do Python and R bundles

- What options are there for creating Python and R bundles (of Pyhton or R packages, to accessed by the user as a single module command)?

- How does a __user__ add packages to such a bundle?

## 3. Review of new packages made by UCL

- What does Harmen think of the packages in this repo at hpc-spack/repos/dev/packages?

?? ANY QUESTIONS ARISING FROM THESE???

- some of our own build scripts require the module gcc-libs/4.9.2. What is the equivalent, if any, in the spack framework?

- The generic package class has 
``` make()
    make("install") ```
are these just suggestions of things the packager might provide so can be deleted, or are in fact essential functions?
