footer: SURFsara, 12-10-2015
slidenumbers: true
autoscale: true

# Databases - Part II
### SNE Master: Essential Skills

# [fit]![inline 100%](sources/db_landscape.png)

---

### Today

__Part II: NoSQL and NewSQL__
- NoSQL driving forces
- CAP Theorem
- Data models
- Hype? 
- NewSQL

![right 50%](sources/nosql.png)

---
### NoSQL - driving forces  

1. *Scaling out*: partitioning
2. *Performance*: remove complexity, simplify assumptions
4. *Impedance mismatch*: from relational data structures to programming language constructs

---
### Partitioning for RDBMS?
![original, right 75%](sources/joins.png)
![original, left 75%](sources/acid.jpg)

---
### Performance: The cost of not being on time
![original, 100%](sources/costs.png)

---
### Performance: The cost of not being on time
![original, 150%](sources/ing1.png)

---
### Impedance mismatch
![original, 100%](sources/impedancem1.png)

---
__Object oriented__
*vs.* __Relational__ data structures

![original, 100%](sources/ORMS.png)

---
### Impedance mismatch
![original, 100%](sources/impedancem2.png)

---
### Partitioning

![original 100%](sources/part1.png)

---
### Partitioning

![original 100%](sources/part2.png)

---
### Partitioning

![original 100%](sources/part3.png)

---
### Partitioning and CAP

![original 160%](sources/cap1.png)

---
### Partitioning and CAP
__Consistency__: All nodes see the same data at the same time

__Availability__: A guarantee that every request receives a response about whether it succeeded or failed

__Partition tolerance__: Ability to cope with a partitioned network of system nodes

---
### Partition tolerance
 1. The network is reliable
 2. Latency is zero
 3. Bandwidth is infinite
 4. The network is secure
 5. Topology doesn't change
 6. There is one administrator
 7. Transport cost is zero
 8. The network is homogeneous

![original, right 100%](sources/networks.png)

---
### Visual Guide to NoSQL systems
![original 120%](sources/nosql_visual.png)

---
### CAP Misconceptions
1. CA?
2. No CA when P?
3. C is all or nothing
4. CAP is all about eventual consistency

---
### PACELC
__If Partioned__:
Tradeoff Availability and Consistency

__Else__:
Tradeoff Latency and Consistency

__Types of systems__:
- PC/EC -> Most consistent
- PA/EL -> No consistency but low latency
- PA/EC -> Give up consistency when partitioned
- PC/EL -> Madness? See PNUTS

---
### Consistency: atomicity and ordering
![original 100%](sources/aando.png)

---
### Consistency: vector clocks
![original 100%](sources/vectorclocks.png)

---
### Consistency: tunable CAP
__Riak__:
*N*: number of total copies
*R*: minimal number of responding clients when reading
*W*: minimal number of responding clients when writing

__Cassandra__:
Tunable write consistency
Tunable read consistency

__MongoDB__:
Write result setting
Read result setting

![right, 20%](sources/knobs.jpg)

---
### Tunable CAP: Amazon shopping Basket

Amazon uses DynamoDB for shopping baskets. DynamoDB, like Riak is a distributed key-value store where N-R-W can be set for operation.

If you were Amazon, how would you choose N-R-W for a shopping basket?

---
### Eventual consistency

__Key property of non-ACID__
    - If no further changes
    - All nodes will end up consistent

__Weak guarantee__
    - When is eventually? It doesn’t say..
    - In practice: expect inconsistency; always!

__In practice__:
    - Stronger guarantees: predicting/measuring behavior
    - Systems often appear strongly consistent

---
### Eventual consistency
__Nodes must exchange information on writes__:
    - Inform replicas
    - Inform client


__Deal with conflicts__:
    - Last write win?
    - Vector clocks
    - Multiversion storage
    - Hardware clocks

---
### Data models
![original, fit](sources/dmodels.png)

---
### Data model: Column based
__Column stores__:
- HBase
- Cassandra
- MonetDB
- Google: BigTable

![right 150%](sources/columnstores.png)

---
### Data model: Key-value
Similar to dictionaries and (hash)maps

__Key-value stores__:
- Riak
- DynamoDB
- Redis
- memcached

![right 150%](sources/kvstores.png)

---
### Data model: Key-value
JSON Documents as data.

__Document stores__:
- MongoDB
- CouchDB
- CouchBase

![right 150%](sources/docstores.png)


---
### Data model: Graphs
Graphs and graph queries as first class citizens.

__Graph stores__:
- Neo4J
- OpenLink
- Titan

![right 150%](sources/graphstores.png)


---
### Data model: Specialized
Distributed 
Lucene 
Indexes

![original 150%](sources/es.png)

---
### Hype?
![original 100%](sources/endor.png)

---
### Hype?
![original 100%](sources/oracles.png)

---
### Hype?
![original 150%](sources/jobtrends1.png)

---
### Hype?
![original 150%](sources/jobtrends2.png)

---
### Hype?
![original 150%](sources/jobtrends3.png)

---
### Hype?
![original 150%](sources/jobtrends4.png)

---
### Hype?
![original 150%](sources/oodb.png)

---
### Hype?
![original 150%](sources/xmldb.png)

---
### Hype?
![original 150%](sources/nosqldb.png)

---
### Hype?
![original 100%](sources/trendsovertime.png)

---
### Future directions
- Internal polyglot support
- Multi-model systems
- NewSQL: Can you have a scalable databases without going NoSQL? (“beating” CAP)
- Further support for NoSQL in RDBMs
- DBaaS and Baas

---
### Meanwhile at
![original 100%](sources/Google.png)

---
### NewSQL
![original 100%](sources/f1_1.png)

---
### NewSQL
![original 100%](sources/f1_2.png)

---
### NewSQL
Some Requirements:

__Scalable__
    - By adding hardware
    - No manual sharding
    
__Available__
    - No downtime,  ever

__Consistent__
    - Full ACID

__Usable__
    - Full SQL with indexes
   
![original, right 100%](sources/f1_3.png) 

---
### NewSQL

__Spanner__:
- Semi-relational distributed DB
    - SQL queries
    - Versioned data
- Consistent reads/writes
- Atomic schema updates
- High availability
- Removing nodes has no effect except on throughput (PC/EC)

__TrueTime__:
- Timestamp: consistent ordering on transactions
- Uses: GPS and atomic clocks

![original, right 150%](sources/paxos.png) 

---
### NewSQL
__F1__:
- Distributed SQL queries
- Consistent indexes
- Automatic change history (triggers)

![original, right 150%](sources/f1_4.png) 

---
### NewSQL
F1:
- 100 TB of uncompressed data 
    - Over 5 data centers
    - Five nines uptime

- Hundreds of thousands of request/second

- SQL queries scan trillions of rows/day

- No observable increase of latency compared to MySQL

- NoSQL (key -> row) and full SQL


![right 100%](sources/f1_5.png) 

---

### Beware of vendor speak
![original 100%](sources/vendorspeak.png)

---
# Questions?

---

[^1]: [A Relational Model of Data for Large Shared Databanks](). Communications of the ACM, 13, June.

[^2]: [The Entity-Relationship Model: Toward a unified view of data](). ACM Transactions on Database Systems, 1, March.


