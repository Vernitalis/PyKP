[out:json];
area["name"="Polska"]->.polska;
(
node
  [railway=halt]
  (area.polska);
node
  [railway=station]
  (area.polska);
);
out;
