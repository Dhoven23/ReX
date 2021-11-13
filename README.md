# Instructionès
How to install, start, and update the client and server
# Prerequisites

1. Install Node.js
2. Install VS Code (or use your editor of choice, but vs code has a built in terminal)

## Installation
Open 2 terminals in VS Code
In the first terminal:

...\REX> cd server

...\REX\server> npm install

in the second terminal:

...\REX> cd client

...\REX\client> npm install

## Start
Open a terminal and run

...\REX> npm run dev

# Dev Conversation
## 11/12/2021 - reply to daniel's questions

1. This is zoom worthy, I probably have like an hour worth of questions (can you say podcast content? i <3 audio editing). Four questions in paticular:

    a) Ergotic Models, what de heck is dat?

    b) How does a single node acting as an attractor benefit us over using an over cnn to find a solution relative to all nodes?

    c) Are we pinging recursively, or just pinging a simple list of all adjacent nodes and sticking to a radius = 1 per node simulation

    d) N > 2 sounds to me like a regression problem, but I'll probe your thinking with this:

    [YouTube.com: WayMo Cars Taking Over Quiet SF Dead End Street](https://www.youtube.com/watch?v=2sZnGdBm_fs)

    What does this video bring to mind (I see a park of a network in a 'topographical lull', a local low point in regression where a better point exists, but because so many waymo, (weymo?) cars have gone that way the collective solution has been reinforced to recognize that dead end as a 'high scoring' solution when they need to find an autonomous route in that area)

2. Round 2 of questions:

    a) What is wavelet compression

    b) When increasing the frequency in connection to a node that's 'changing the most,' does the change in frecquency of connection correlate to a negative change in latency (a trend of decreasing latency) or does it always update when latency changes to account for both positive and negative increases. You know what, thinking aloud, I think it should be the latter!

    c) So we do use a global network controller! Sudden Outages, i.e non-continous breaks in outages are accounted for by a network supervisor, which handles threading / parallellization of a shared task across multiple nodes?


3. A single questioneier a la fourier: is the whole goal of point number three to only make changes to nodes that have local changes, without the need to loop / regress through the whole network? I leik dis but I meight need some direction with what youtube videos to watch lawl.

## REPLY 11/12/2021

1. I believe that the correct model for the data is not a global NN, but a dynamic one. each neuron in the NN only contains training data relevant to its local nodes. I think that a classical backpropogated CNN is not what will make this work. I would like to use an ergotic model that views the correct network config as an attractor, not a 'solution'. A reinforcement (reward/loss) genetic algorithm could work very well, since the training can be done with a simple ping command. Think of how the N > 2 body problem (ex: Sun, earth, moon) has several 'stable' solutions, and a zillion transient ones. the goal of the machine learning model is to converge upon a local solution to a globally chaotic system. rather than trying to find one orbit that stabilizes all 3+ bodies. I'm thinking out loud here.  

2. I will work on the geometry problem of how to correlate the data points. You're right that it has to be NN friendly, but ideally the data model itself is the NN, not just an input for it. As for adding/removing nodes, youll love this. We'll use wavelet compression! effectively each node has a linear string of other nodes (L) as they request connection. We want to 'sort' this list into fastest/slowest right? but how do you know if/where you need to re-sort? you make a differential graph, basically a copy of the list L, but rather than storing the latency, it stores the change in latency! because nodes are moving! then we just increase the frequency of connection with nodes that change the most, and reduce the frequency of connection with nodes that change the least. this way we are 'smart' sorting (updating the model only where necessary). This also handles the 'sudden outage' problem, because it prompts a gobal resorting of local nodes, automatically done in parallel, so although the math may have to be done for NxN connections, each node must only perform N operations. but it will also handle local outages/changes without effecting the rest of the network. i think this entire thing could be done with local wavelets.

3. How is it preditive? you train a local NN with the wavelet coefficients as inputs, (essentially a modified DMD) and the future coefficients as outputs. Since these coefficients are multiscale, they capture predictive data automatically, just like you can reconstruct an image from a subset of pixels if you can from those pixels extract the fourier transform of the image at large, which is highly structured, you can construct a global 'movie' of how the network is changing if you can extract the Wavlet coefficients for nearby nodes. please ask questions, that was a lot. 

## 11/12/2021 - A few thoughts

Game On, Allow me to Rebuttle!

1. How far down the hypervisor rabbit hole do we go? because I'm all for building out a distributed system that learns the most successful configuration from previous experience and predicts the most successfull 'relative_network' of nodes relative to the 'requesting node'.

2. Where is the training data coming from? There might be a record ofa single distributed systems performance over x years, but if not we should have a standard in place for generating continuous and uncontinuous data to be sure the network is comfortable not only with gradual, continuous changes in network bandwidth, but also for sudden outages / (re)introduction of nodes into the system.

### Data

The data schema for a neural network friendly record of how the network performed with the nodes around it will need to store data about the nodes themselves, the paths between them, and possibly most importantly, a precompiled configuration of

to handle dynamic networks (a distributed system where a new node being added, an old node being removed, or the ) there should be a screenshot of the network as a whole or the nodes explored as a part of a combined map for the network to relate nodes to one another.

### Scoring

Stability
Consistency (same as stability?)
success in future predictions

## 11/10/2021 - First Commit

Code Repo for ReX, (Robust eXa-scale computing)

please do not use for real rockets

also Nick Stine  Sucks Biiiiiiig Fat thiiiiiiqqqqqq juicy Monkey swingers.......

#####################################
