const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
const myWatchedSeriesLength = 2;
const myWatchedSeriesSentence = "money heist and the big bang theory"

const myWatchedSeriesDefinition = "I watched " + myWatchedSeriesLength + " series: " + myWatchedSeriesSentence;

console.log (myWatchedSeriesDefinition);

const series3 = "the big bang theory";
myWatchedSeries[2] = "friends";

myWatchedSeries.push("white collars");

myWatchedSeries.unshift("blacklist");

delete myWatchedSeries [1];

console.log (myWatchedSeries[2][2]);

console.log (myWatchedSeries);

