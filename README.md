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

## 11/12/2021 - A few thoughts
Game On, Allow me to Rebuttle!

1. How far down the hypervisor rabbit hole do we go? because I'm all for building out a distributed system that learns the most successful configuration from previous experience and predicts the most successfull 'relative_network' of nodes relative to the 'requesting node'.

2. Where is the training data coming from? There might be a record ofa single distributed systems performance over x years, but if not we should have a standard in place for generating continuous and uncontinuous data to be sure the network is comfortable not only with gradual, continuous changes in network bandwidth, but also for sudden outages / (re)introduction of nodes into the system.

### Data
The data schema for a neural network friendly record of how the network performed with the nodes around it will need to store data about the nodes themselves, the paths between them, and possibly most importantly, a precompiled configuration of

to handle dynamic networks (a distributed system where a new node being added, an old node being removed, or the ) there should be a screenshot of the network as a whole or the nodes explored as a part of a combined map for the network to relate nodes to one another.


## REPLY 11/12/2021
I think you forgot to add some directories... server is missing on my end?

1. I believe that the correct model for the data is not a global NN, but a dynamic one. each neuron in the NN only contains training data relevant to its local nodes. I think that a classical backpropogated CNN is not what will make this work. I would like to use an ergotic model that views the correct network config as an attractor, not a 'solution'. A reinforcement (reward/loss) genetic algorithm could work very well, since the training can be done with a simple ping command. Think of how the N > 2 body problem (ex: Sun, earth, moon) has several 'stable' solutions, and a zillion transient ones. the goal of the machine learning model is to converge upon a local solution to a globally chaotic system. rather than trying to find one orbit that stabilizes all 3+ bodies. I'm thinking out loud here.  

2. I will work on the geometry problem of how to correlate the data points. You're right that it has to be NN friendly, but ideally the data model itself is the NN, not just an input for it. As for adding/removing nodes, youll love this. We'll use wavelet compression! effectively each node has a linear string of other nodes (L) as they request connection. We want to 'sort' this list into fastest/slowest right? but how do you know if/where you need to re-sort? you make a differential graph, basically a copy of the list L, but rather than storing the latency, it stores the change in latency! because nodes are moving! then we just increase the frequency of connection with nodes that change the most, and reduce the frequency of connection with nodes that change the least. this way we are 'smart' sorting (updating the model only where necessary). This also handles the 'sudden outage' problem, because it prompts a gobal resorting of local nodes, automatically done in parallel, so although the math may have to be done for NxN connections, each node must only perform N operations. but it will also handle local outages/changes without effecting the rest of the network. i think this entire thing could be done with local wavelets.

3. How is it preditive? you train a local NN with the wavelet coefficients as inputs, (essentially a modified DMD) and the future coefficients as outputs. Since these coefficients are multiscale, they capture predictive data automatically, just like you can reconstruct an image from a subset of pixels if you can from those pixels extract the fourier transform of the image at large, which is highly structured, you can construct a global 'movie' of how the network is changing if you can extract the Wavlet coefficients for nearby nodes. please ask questions, that was a lot. 



### Scoring
Stability
Consistency (same as stability?)
success in future predictions

## 11/10/2021 - First Commit
Code Repo for ReX, (Robust eXa-scale computing)

please do not use for real rockets

also Nick Stine  Sucks Biiiiiiig Fat thiiiiiiqqqqqq juicy Monkey swingers.......

#####################################
