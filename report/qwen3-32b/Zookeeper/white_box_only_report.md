# Log Analysis Report

## Log matched templates
| Metric | Value |
|------|-----|
| Precision | 0.8511 (40/47) |
| Recall    | 0.9091 (40/44) |
| F1-Score  | 0.8791 |

## Statistical Overview
- Total log count: `2000`
- Matched log count: `1904`
- Log match rate: `95.20%`
- Number of matched templates: `47`

## Template Matching Details
| Template Pattern | Match Count |
|----------|----------|
| `Notification time out: <.*>` | 37 |
| `Received connection request <.*>` | 299 |
| `Send worker leaving thread` | 262 |
| `Interrupted while waiting for message on queue` | 314 |
| `Interrupted while waiting` | 314 |
| `Connection broken for id <.*>, my id = <.*>, error =` | 291 |
| `Interrupting SendWorker` | 266 |
| `caught end of stream exception` | 37 |
| `Client attempting to renew session <.*> at <.*>` | 3 |
| `Client attempting to establish new session at <.*>` | 41 |
| `Established session <.*> with negotiated timeout <.*> for client <.*>` | 50 |
| `Accepted socket connection from <.*>` | 48 |
| `Connection request from old client <.*>; will be dropped if server is in r-o mode` | 39 |
| `Server environment:<.*>` | 11 |
| `Cannot open channel to <.*> at election address <.*>` | 86 |
| `Expiring session <.*>, timeout of <.*>ms exceeded` | 40 |
| `******* GOODBYE <.*> ********` | 19 |
| `LOOKING` | 14 |
| `My election bind port: <.*>` | 1 |
| `Have smaller server identifier, so dropping the connection: (<.*>, <.*>)` | 1 |
| `FOLLOWING` | 7 |
| `New election. My id = <.*>, proposed zxid=<.*>` | 1 |
| `FOLLOWING - LEADER ELECTION TOOK - <.*>` | 2 |
| `Notification: <.*> (n.leader), <.*> (n.zxid), <.*> (n.round), <.*> (n.state), <.*> (n.sid), <.*> (n.peerEPoch), <.*> (my state)` | 12 |
| `LEADING` | 5 |
| `<.*> set to <.*>` | 8 |
| `autopurge.snapRetainCount set to <.*>` | 1 |
| `Revalidating client: <.*>` | 3 |
| `Exception causing close of session <.*> due to java.io.IOException: ZooKeeperServer not running` | 3 |
| `IOException` | 3 |
| `tickTime set to <.*>` | 2 |
| `Unexpected exception<.*>` | 12 |
| `Unexpected exception` | 192 |
| `Got user-level KeeperException when processing <.*> Error Path:<.*> Error:<.*>` | 1 |
| `Got user-level KeeperException when processing sessionid:<.*> type:create cxid:<.*> zxid:<.*> txntype:<.*> reqpath:<.*> Error Path:<.*> Error:KeeperErrorCode = NodeExists for <.*>` | 1 |
| `Starting quorum peer` | 1 |
| `Snapshotting: <.*> to <.*>` | 2 |
| `autopurge.purgeInterval set to <.*>` | 3 |
| `Follower sid: <.*> : info : <.*>` | 1 |
| `maxSessionTimeout set to <.*>` | 2 |
| `Have quorum of supporters; starting up and setting last processed zxid: <.*>` | 1 |
| `shutdown of request processor complete` | 1 |
| `First is <.*>` | 1 |
| `Reading snapshot <.*>` | 1 |
| `Sending DIFF` | 1 |
| `Getting a snapshot from leader` | 2 |
| `minSessionTimeout set to <.*>` | 4 |

## Matched Content Details
### pattern `Notification time out: <.*>`
**Match times**: 37

```text
Match example 1:
2015-07-29 17:41:44,747 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:FastLeaderElection@774] - Notification time out: 3200
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 23:52:26,272 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:FastLeaderElection@774] - Notification time out: 60000
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-24 15:36:13,663 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:FastLeaderElection@774] - Notification time out: 60000
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Received connection request <.*>`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:04:12,394 - INFO [/10.10.34.11:3888:QuorumCnxManager$Listener@493] - Received connection request /10.10.34.11:45307
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:13:24,370 - INFO [/10.10.34.11:3888:QuorumCnxManager$Listener@493] - Received connection request /10.10.34.13:57707
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:13:54,220 - INFO [/10.10.34.11:3888:QuorumCnxManager$Listener@493] - Received connection request /10.10.34.11:45382
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Send worker leaving thread`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:04:29,071 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@688] - Send worker leaving thread
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:13:17,524 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@688] - Send worker leaving thread
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:13:37,626 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@688] - Send worker leaving thread
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Interrupted while waiting for message on queue`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:04:29,079 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:13:34,382 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:14:04,406 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Interrupted while waiting`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:04:29,079 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:13:34,382 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:14:04,406 - WARN [SendWorker:188978561024:QuorumCnxManager$SendWorker@679] - Interrupted while waiting for message on queue
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Connection broken for id <.*>, my id = <.*>, error =`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:13:24,282 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@762] - Connection broken for id 188978561024, my id = 1, error =
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:13:27,721 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@762] - Connection broken for id 188978561024, my id = 1, error =
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:13:47,731 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@762] - Connection broken for id 188978561024, my id = 1, error =
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Interrupting SendWorker`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:14:07,559 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@765] - Interrupting SendWorker
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:14:24,329 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@765] - Interrupting SendWorker
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:14:47,593 - WARN [RecvWorker:188978561024:QuorumCnxManager$RecvWorker@765] - Interrupting SendWorker
────────────────────────────────────────────────────────────────────────────────
```

### pattern `caught end of stream exception`
**Match times**: 37

```text
Match example 1:
2015-07-29 19:52:05,118 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@349] - caught end of stream exception
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 17:11:54,937 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@349] - caught end of stream exception
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-30 17:22:34,245 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@349] - caught end of stream exception
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Client attempting to renew session <.*> at <.*>`
**Match times**: 3

```text
Match example 1:
2015-07-29 19:54:13,615 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@832] - Client attempting to renew session 0x24ed93119420016 at /10.10.34.13:37115
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-10 18:23:52,653 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@832] - Client attempting to renew session 0x14f05578bd8001b at /10.10.34.20:56374
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-10 18:25:27,964 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@832] - Client attempting to renew session 0x24f0557806a0020 at /10.10.34.17:55969
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Client attempting to establish new session at <.*>`
**Match times**: 41

```text
Match example 1:
2015-07-29 21:01:41,504 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@839] - Client attempting to establish new session at /10.10.34.19:33425
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 14:53:21,340 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@839] - Client attempting to establish new session at /10.10.34.11:50286
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-30 15:00:24,824 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@839] - Client attempting to establish new session at /10.10.34.11:50301
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Established session <.*> with negotiated timeout <.*> for client <.*>`
**Match times**: 50

```text
Match example 1:
2015-07-29 21:34:45,452 - INFO [CommitProcessor:1:ZooKeeperServer@595] - Established session 0x14ed93111f20027 with negotiated timeout 10000 for client /10.10.34.13:37177
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 21:34:48,285 - INFO [CommitProcessor:1:ZooKeeperServer@595] - Established session 0x14ed93111f2002b with negotiated timeout 10000 for client /10.10.34.22:47073
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 23:52:08,962 - INFO [CommitProcessor:1:ZooKeeperServer@595] - Established session 0x14ed93111f2005b with negotiated timeout 10000 for client /10.10.34.28:52117
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Accepted socket connection from <.*>`
**Match times**: 48

```text
Match example 1:
2015-07-29 21:39:24,986 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@197] - Accepted socket connection from /10.10.34.13:37196
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 21:39:28,234 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@197] - Accepted socket connection from /10.10.34.26:56952
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 23:52:09,163 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@197] - Accepted socket connection from /10.10.34.30:38562
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Connection request from old client <.*>; will be dropped if server is in r-o mode`
**Match times**: 39

```text
Match example 1:
2015-07-30 16:12:01,554 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@793] - Connection request from old client /10.10.34.19:33442; will be dropped if server is in r-o mode
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 16:18:36,818 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@793] - Connection request from old client /10.10.34.20:56418; will be dropped if server is in r-o mode
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-30 16:18:38,680 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:ZooKeeperServer@793] - Connection request from old client /10.10.34.42:34164; will be dropped if server is in r-o mode
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Server environment:<.*>`
**Match times**: 11

```text
Match example 1:
2015-07-30 17:43:58,186 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Environment@100] - Server environment:user.dir=/
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-31 19:30:07,445 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Environment@100] - Server environment:host.name=mesos-master-1
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-10 18:23:50,332 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Environment@100] - Server environment:java.vendor=Oracle Corporation
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Cannot open channel to <.*> at election address <.*>`
**Match times**: 86

```text
Match example 1:
2015-07-30 17:55:26,200 - WARN [WorkerSender[myid=1]:QuorumCnxManager@368] - Cannot open channel to 2 at election address /10.10.34.12:3888
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 23:44:01,784 - WARN [WorkerSender[myid=1]:QuorumCnxManager@368] - Cannot open channel to 2 at election address /10.10.34.12:3888
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-30 23:44:04,784 - WARN [WorkerSender[myid=1]:QuorumCnxManager@368] - Cannot open channel to 3 at election address /10.10.34.13:3888
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Expiring session <.*>, timeout of <.*>ms exceeded`
**Match times**: 40

```text
Match example 1:
2015-07-30 20:06:34,001 - INFO [SessionTracker:ZooKeeperServer@325] - Expiring session 0x24ede63a01b003b, timeout of 10000ms exceeded
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 20:13:46,001 - INFO [SessionTracker:ZooKeeperServer@325] - Expiring session 0x34ede65503f0036, timeout of 10000ms exceeded
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-30 23:03:52,001 - INFO [SessionTracker:ZooKeeperServer@325] - Expiring session 0x34ede65503f005c, timeout of 10000ms exceeded
────────────────────────────────────────────────────────────────────────────────
```

### pattern `******* GOODBYE <.*> ********`
**Match times**: 19

```text
Match example 1:
2015-07-30 23:43:22,414 - WARN [LearnerHandler-/10.10.34.12:35276:LearnerHandler@575] - ******* GOODBYE /10.10.34.12:35276 ********
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:04:30,989 - WARN [LearnerHandler-/10.10.34.11:52264:LearnerHandler@575] - ******* GOODBYE /10.10.34.11:52264 ********
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:13:46,128 - WARN [LearnerHandler-/10.10.34.11:52308:LearnerHandler@575] - ******* GOODBYE /10.10.34.11:52308 ********
────────────────────────────────────────────────────────────────────────────────
```

### pattern `LOOKING`
**Match times**: 14

```text
Match example 1:
2015-07-30 23:43:23,613 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:QuorumPeer@670] - LOOKING
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-31 19:30:07,398 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:QuorumPeer@670] - LOOKING
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-07 07:27:47,425 - INFO [WorkerReceiver[myid=1]:FastLeaderElection@542] - Notification: 3 (n.leader), 0x700000197 (n.zxid), 0x1 (n.round), LEADING (n.state), 3 (n.sid), 0x7 (n.peerEPoch), LOOKING (my state)
────────────────────────────────────────────────────────────────────────────────
```

### pattern `My election bind port: <.*>`
**Match times**: 1

```text
Match example 1:
2015-07-31 15:31:40,971 - INFO [Thread-1:QuorumCnxManager$Listener@486] - My election bind port: 0.0.0.0/0.0.0.0:3888
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Have smaller server identifier, so dropping the connection: (<.*>, <.*>)`
**Match times**: 1

```text
Match example 1:
2015-07-31 15:31:40,999 - INFO [WorkerSender[myid=1]:QuorumCnxManager@190] - Have smaller server identifier, so dropping the connection: (2, 1)
────────────────────────────────────────────────────────────────────────────────
```

### pattern `FOLLOWING`
**Match times**: 7

```text
Match example 1:
2015-07-31 15:31:42,213 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:QuorumPeer@738] - FOLLOWING
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-31 19:30:07,452 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Follower@63] - FOLLOWING - LEADER ELECTION TOOK - 49
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-07 07:27:47,650 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Follower@63] - FOLLOWING - LEADER ELECTION TOOK - 238
────────────────────────────────────────────────────────────────────────────────
```

### pattern `New election. My id = <.*>, proposed zxid=<.*>`
**Match times**: 1

```text
Match example 1:
2015-07-31 19:30:07,403 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:FastLeaderElection@740] - New election. My id = 1, proposed zxid=0x700000000
────────────────────────────────────────────────────────────────────────────────
```

### pattern `FOLLOWING - LEADER ELECTION TOOK - <.*>`
**Match times**: 2

```text
Match example 1:
2015-07-31 19:30:07,452 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Follower@63] - FOLLOWING - LEADER ELECTION TOOK - 49
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-07 07:27:47,650 - INFO [QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:Follower@63] - FOLLOWING - LEADER ELECTION TOOK - 238
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Notification: <.*> (n.leader), <.*> (n.zxid), <.*> (n.round), <.*> (n.state), <.*> (n.sid), <.*> (n.peerEPoch), <.*> (my state)`
**Match times**: 12

```text
Match example 1:
2015-08-07 07:27:47,425 - INFO [WorkerReceiver[myid=1]:FastLeaderElection@542] - Notification: 3 (n.leader), 0x700000197 (n.zxid), 0x1 (n.round), LEADING (n.state), 3 (n.sid), 0x7 (n.peerEPoch), LOOKING (my state)
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-20 17:14:12,326 - INFO [WorkerReceiver[myid=1]:FastLeaderElection@542] - Notification: 2 (n.leader), 0xb00000084 (n.zxid), 0x2 (n.round), LOOKING (n.state), 1 (n.sid), 0xb (n.peerEPoch), LOOKING (my state)
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-20 17:14:23,824 - INFO [WorkerReceiver[myid=1]:FastLeaderElection@542] - Notification: 3 (n.leader), 0xb0000007b (n.zxid), 0x2 (n.round), LOOKING (n.state), 3 (n.sid), 0xb (n.peerEPoch), FOLLOWING (my state)
────────────────────────────────────────────────────────────────────────────────
```

### pattern `LEADING`
**Match times**: 5

```text
Match example 1:
2015-08-07 07:27:47,425 - INFO [WorkerReceiver[myid=1]:FastLeaderElection@542] - Notification: 3 (n.leader), 0x700000197 (n.zxid), 0x1 (n.round), LEADING (n.state), 3 (n.sid), 0x7 (n.peerEPoch), LOOKING (my state)
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:56:54,754 - INFO [WorkerReceiver[myid=2]:FastLeaderElection@542] - Notification: 3 (n.leader), 0x10000006b (n.zxid), 0x2 (n.round), LOOKING (n.state), 3 (n.sid), 0x1 (n.peerEPoch), LEADING (my state)
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-18 16:09:22,982 - INFO [WorkerReceiver[myid=2]:FastLeaderElection@542] - Notification: 2 (n.leader), 0xa0000009a (n.zxid), 0x1 (n.round), FOLLOWING (n.state), 1 (n.sid), 0xa (n.peerEPoch), LEADING (my state)
────────────────────────────────────────────────────────────────────────────────
```

### pattern `<.*> set to <.*>`
**Match times**: 8

```text
Match example 1:
2015-08-10 18:23:49,901 - INFO [main:DatadirCleanupManager@78] - autopurge.snapRetainCount set to 3
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-24 15:26:54,494 - INFO [main:QuorumPeer@913] - tickTime set to 2000
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-31 15:31:15,575 - INFO [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 0
────────────────────────────────────────────────────────────────────────────────
```

### pattern `autopurge.snapRetainCount set to <.*>`
**Match times**: 1

```text
Match example 1:
2015-08-10 18:23:49,901 - INFO [main:DatadirCleanupManager@78] - autopurge.snapRetainCount set to 3
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Revalidating client: <.*>`
**Match times**: 3

```text
Match example 1:
2015-08-10 18:23:52,646 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:Learner@107] - Revalidating client: 0x14f05578bd80018
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-10 18:25:24,332 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:Learner@107] - Revalidating client: 0x14f05578bd80013
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-10 18:23:56,268 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:Learner@107] - Revalidating client: 0x24f0557806a001c
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Exception causing close of session <.*> due to java.io.IOException: ZooKeeperServer not running`
**Match times**: 3

```text
Match example 1:
2015-08-20 17:14:11,414 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-20 17:12:45,757 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-20 17:13:51,524 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
```

### pattern `IOException`
**Match times**: 3

```text
Match example 1:
2015-08-20 17:14:11,414 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-20 17:12:45,757 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-20 17:13:51,524 - WARN [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@354] - Exception causing close of session 0x0 due to java.io.IOException: ZooKeeperServer not running
────────────────────────────────────────────────────────────────────────────────
```

### pattern `tickTime set to <.*>`
**Match times**: 2

```text
Match example 1:
2015-08-24 15:26:54,494 - INFO [main:QuorumPeer@913] - tickTime set to 2000
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-24 15:26:54,494 - INFO [main:QuorumPeer@913] - tickTime set to 2000
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Unexpected exception<.*>`
**Match times**: 12

```text
Match example 1:
2015-07-29 19:03:35,413 - ERROR [LearnerHandler-/10.10.34.11:52225:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:03:54,584 - ERROR [LearnerHandler-/10.10.34.11:52241:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:04:30,989 - ERROR [LearnerHandler-/10.10.34.11:52265:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Unexpected exception`
**Match times**: 100

```text
Match example 1:
2015-07-29 19:03:35,413 - ERROR [LearnerHandler-/10.10.34.11:52225:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-29 19:03:35,413 - ERROR [LearnerHandler-/10.10.34.11:52225:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-29 19:03:35,413 - ERROR [LearnerHandler-/10.10.34.11:52225:LearnerHandler@562] - Unexpected exception causing shutdown while sock still open
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Got user-level KeeperException when processing <.*> Error Path:<.*> Error:<.*>`
**Match times**: 1

```text
Match example 1:
2015-07-29 19:37:27,222 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@627] - Got user-level KeeperException when processing sessionid:0x34ed93485090001 type:create cxid:0x55b8bb0f zxid:0x100000010 txntype:-1 reqpath:n/a Error Path:/home/curi/.zookeeper Error:KeeperErrorCode = NodeExists for /home/curi/.zookeeper
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Got user-level KeeperException when processing sessionid:<.*> type:create cxid:<.*> zxid:<.*> txntype:<.*> reqpath:<.*> Error Path:<.*> Error:KeeperErrorCode = NodeExists for <.*>`
**Match times**: 1

```text
Match example 1:
2015-07-29 19:37:27,222 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@627] - Got user-level KeeperException when processing sessionid:0x34ed93485090001 type:create cxid:0x55b8bb0f zxid:0x100000010 txntype:-1 reqpath:n/a Error Path:/home/curi/.zookeeper Error:KeeperErrorCode = NodeExists for /home/curi/.zookeeper
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Starting quorum peer`
**Match times**: 1

```text
Match example 1:
2015-07-30 23:46:27,304 - INFO [main:QuorumPeerMain@127] - Starting quorum peer
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Snapshotting: <.*> to <.*>`
**Match times**: 2

```text
Match example 1:
2015-07-30 23:46:31,590 - INFO [QuorumPeer[myid=2]/0:0:0:0:0:0:0:0:2181:FileTxnSnapLog@240] - Snapshotting: 0x300000dcd to /var/lib/zookeeper/version-2/snapshot.300000dcd
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-31 15:36:21,074 - INFO [QuorumPeer[myid=2]/0:0:0:0:0:0:0:0:2181:FileTxnSnapLog@240] - Snapshotting: 0x50000062e to /var/lib/zookeeper/version-2/snapshot.50000062e
────────────────────────────────────────────────────────────────────────────────
```

### pattern `autopurge.purgeInterval set to <.*>`
**Match times**: 3

```text
Match example 1:
2015-07-31 15:31:15,575 - INFO [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 0
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-10 18:25:25,206 - INFO [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 0
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-08-25 11:14:51,514 - INFO [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 0
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Follower sid: <.*> : info : <.*>`
**Match times**: 1

```text
Match example 1:
2015-07-31 15:36:24,570 - INFO [LearnerHandler-/10.10.34.13:59348:LearnerHandler@263] - Follower sid: 3 : info : org.apache.zookeeper.server.quorum.QuorumPeer$QuorumServer@33557fe4
────────────────────────────────────────────────────────────────────────────────
```

### pattern `maxSessionTimeout set to <.*>`
**Match times**: 2

```text
Match example 1:
2015-08-10 18:25:25,239 - INFO [main:QuorumPeer@944] - maxSessionTimeout set to -1
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-08-10 18:25:25,239 - INFO [main:QuorumPeer@944] - maxSessionTimeout set to -1
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Have quorum of supporters; starting up and setting last processed zxid: <.*>`
**Match times**: 1

```text
Match example 1:
2015-08-18 16:09:18,900 - INFO [LearnerHandler-/10.10.34.11:49928:Leader@598] - Have quorum of supporters; starting up and setting last processed zxid: 0xb00000000
────────────────────────────────────────────────────────────────────────────────
```

### pattern `shutdown of request processor complete`
**Match times**: 1

```text
Match example 1:
2015-08-20 17:12:29,085 - INFO [QuorumPeer[myid=2]/0:0:0:0:0:0:0:0:2181:FinalRequestProcessor@415] - shutdown of request processor complete
────────────────────────────────────────────────────────────────────────────────
```

### pattern `First is <.*>`
**Match times**: 1

```text
Match example 1:
2015-08-20 17:14:13,880 - WARN [LearnerHandler-/10.10.34.13:42241:Leader@576] - First is 0x0
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Reading snapshot <.*>`
**Match times**: 1

```text
Match example 1:
2015-08-25 11:14:51,662 - INFO [main:FileSnap@83] - Reading snapshot /var/lib/zookeeper/version-2/snapshot.b00000084
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Sending DIFF`
**Match times**: 1

```text
Match example 1:
2015-08-25 11:14:53,074 - INFO [LearnerHandler-/10.10.34.11:32976:LearnerHandler@395] - Sending DIFF
────────────────────────────────────────────────────────────────────────────────
```

### pattern `Getting a snapshot from leader`
**Match times**: 2

```text
Match example 1:
2015-08-25 11:26:28,145 - INFO [QuorumPeer[myid=2]/0:0:0:0:0:0:0:0:2181:Learner@325] - Getting a snapshot from leader
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-31 15:36:23,884 - INFO [QuorumPeer[myid=3]/0:0:0:0:0:0:0:0:2181:Learner@325] - Getting a snapshot from leader
────────────────────────────────────────────────────────────────────────────────
```

### pattern `minSessionTimeout set to <.*>`
**Match times**: 4

```text
Match example 1:
2015-07-30 23:52:53,800 - INFO [main:QuorumPeer@933] - minSessionTimeout set to -1
────────────────────────────────────────────────────────────────────────────────
Match example 2:
2015-07-30 23:52:53,800 - INFO [main:QuorumPeer@933] - minSessionTimeout set to -1
────────────────────────────────────────────────────────────────────────────────
Match example 3:
2015-07-31 15:36:23,686 - INFO [main:QuorumPeer@933] - minSessionTimeout set to -1
────────────────────────────────────────────────────────────────────────────────
```


## Unmatched Log Details
Total 96 unmatched logs

```text
Unmatched log 1:
2015-07-29 19:52:04,792 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.18:42772 which had sessionid 0x14ed93111f20005
════════════════════════════════════════════════════════════════════════════════
Unmatched log 2:
2015-07-29 19:52:09,519 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:45542 which had sessionid 0x14ed93111f20002
════════════════════════════════════════════════════════════════════════════════
Unmatched log 3:
2015-07-29 19:54:45,337 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.13:37106 which had sessionid 0x14ed93111f20010
════════════════════════════════════════════════════════════════════════════════
Unmatched log 4:
2015-07-29 23:44:21,576 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:49557 which had sessionid 0x14ed93111f20048
════════════════════════════════════════════════════════════════════════════════
Unmatched log 5:
2015-07-29 23:44:28,903 - ERROR [CommitProcessor:1:NIOServerCnxn@180] - Unexpected Exception:
════════════════════════════════════════════════════════════════════════════════
Unmatched log 6:
2015-07-30 14:52:21,906 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.29:39382 which had sessionid 0x14ed93111f2005d
════════════════════════════════════════════════════════════════════════════════
Unmatched log 7:
2015-07-30 15:41:40,669 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:50940 which had sessionid 0x14ed93111f20099
════════════════════════════════════════════════════════════════════════════════
Unmatched log 8:
2015-07-30 16:09:17,019 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:52893 which had sessionid 0x14ed93111f2009b
════════════════════════════════════════════════════════════════════════════════
Unmatched log 9:
2015-07-30 16:44:26,593 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:45682 which had sessionid 0x14ed93111f200cd
════════════════════════════════════════════════════════════════════════════════
Unmatched log 10:
2015-07-30 17:06:34,257 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:45697 which had sessionid 0x14ed93111f200d6
════════════════════════════════════════════════════════════════════════════════
Unmatched log 11:
2015-07-30 17:36:31,976 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:54983 which had sessionid 0x14ed93111f200f0
════════════════════════════════════════════════════════════════════════════════
Unmatched log 12:
2015-07-30 18:18:02,003 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ede63a5a70002
════════════════════════════════════════════════════════════════════════════════
Unmatched log 13:
2015-07-30 18:18:30,005 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ede65503f0010
════════════════════════════════════════════════════════════════════════════════
Unmatched log 14:
2015-07-30 19:50:32,001 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ede63a5a70023
════════════════════════════════════════════════════════════════════════════════
Unmatched log 15:
2015-07-30 19:59:08,004 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ede65503f002b
════════════════════════════════════════════════════════════════════════════════
Unmatched log 16:
2015-07-30 20:06:34,003 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ede63a01b003b
════════════════════════════════════════════════════════════════════════════════
Unmatched log 17:
2015-07-30 20:13:46,004 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ede65503f0039
════════════════════════════════════════════════════════════════════════════════
Unmatched log 18:
2015-07-30 20:34:58,003 - INFO [ProcessThread(sid:1 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ede63a5a7003a
════════════════════════════════════════════════════════════════════════════════
Unmatched log 19:
2015-07-30 21:03:35,468 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.13:38088 which had sessionid 0x14ede63a5a70048
════════════════════════════════════════════════════════════════════════════════
Unmatched log 20:
2015-07-30 23:03:42,133 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.17:51214 which had sessionid 0x14ede63a5a70053
════════════════════════════════════════════════════════════════════════════════
Unmatched log 21:
2015-07-31 11:01:40,975 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.13:54485 which had sessionid 0x14edfaa86f60021
════════════════════════════════════════════════════════════════════════════════
Unmatched log 22:
2015-07-31 21:44:41,270 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:59661 which had sessionid 0x14ee3e057ed0027
════════════════════════════════════════════════════════════════════════════════
Unmatched log 23:
2015-08-10 18:12:23,970 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.19:57338 which had sessionid 0x14f05578bd8000d
════════════════════════════════════════════════════════════════════════════════
Unmatched log 24:
2015-08-10 18:27:49,007 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:46331 which had sessionid 0x14f1724a6e80004
════════════════════════════════════════════════════════════════════════════════
Unmatched log 25:
2015-08-20 17:12:29,467 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:56471 (no session established for client)
════════════════════════════════════════════════════════════════════════════════
Unmatched log 26:
2015-08-20 19:32:55,963 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.35:48997 which had sessionid 0x14f4a6318b80024
════════════════════════════════════════════════════════════════════════════════
Unmatched log 27:
2015-08-20 19:33:02,860 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.12:58917 which had sessionid 0x14f4a6318b80018
════════════════════════════════════════════════════════════════════════════════
Unmatched log 28:
2015-07-29 19:52:16,002 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f20005
════════════════════════════════════════════════════════════════════════════════
Unmatched log 29:
2015-07-29 19:52:16,002 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ed93119420008
════════════════════════════════════════════════════════════════════════════════
Unmatched log 30:
2015-07-29 19:52:20,004 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f20000
════════════════════════════════════════════════════════════════════════════════
Unmatched log 31:
2015-07-29 20:39:58,002 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ed9311942000c
════════════════════════════════════════════════════════════════════════════════
Unmatched log 32:
2015-07-29 21:34:48,003 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ed93119420021
════════════════════════════════════════════════════════════════════════════════
Unmatched log 33:
2015-07-29 21:41:34,002 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f2003f
════════════════════════════════════════════════════════════════════════════════
Unmatched log 34:
2015-07-29 23:05:07,344 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.28:37304 which had sessionid 0x24ed9311942004f
════════════════════════════════════════════════════════════════════════════════
Unmatched log 35:
2015-07-29 23:05:16,002 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0021
════════════════════════════════════════════════════════════════════════════════
Unmatched log 36:
2015-07-29 23:43:04,001 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f20046
════════════════════════════════════════════════════════════════════════════════
Unmatched log 37:
2015-07-29 23:44:24,329 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0030
════════════════════════════════════════════════════════════════════════════════
Unmatched log 38:
2015-07-29 23:44:25,695 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f2004f
════════════════════════════════════════════════════════════════════════════════
Unmatched log 39:
2015-07-29 23:50:50,001 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x14ed93111f20050
════════════════════════════════════════════════════════════════════════════════
Unmatched log 40:
2015-07-30 14:38:08,000 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ed93119420073
════════════════════════════════════════════════════════════════════════════════
Unmatched log 41:
2015-07-30 14:52:23,211 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.13:37335 which had sessionid 0x24ed93119420065
════════════════════════════════════════════════════════════════════════════════
Unmatched log 42:
2015-07-30 14:52:27,546 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:53520 which had sessionid 0x24ed9311942005f
════════════════════════════════════════════════════════════════════════════════
Unmatched log 43:
2015-07-30 15:13:13,987 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e005e
════════════════════════════════════════════════════════════════════════════════
Unmatched log 44:
2015-07-30 15:24:39,217 - INFO [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@1001] - Closed socket connection for client /10.10.34.11:53857 which had sessionid 0x24ed93119420082
════════════════════════════════════════════════════════════════════════════════
Unmatched log 45:
2015-07-30 15:38:12,001 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x24ed93119420094
════════════════════════════════════════════════════════════════════════════════
Unmatched log 46:
2015-07-30 16:00:22,001 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0081
════════════════════════════════════════════════════════════════════════════════
Unmatched log 47:
2015-07-30 16:00:30,000 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0080
════════════════════════════════════════════════════════════════════════════════
Unmatched log 48:
2015-07-30 16:11:48,004 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e007a
════════════════════════════════════════════════════════════════════════════════
Unmatched log 49:
2015-07-30 16:11:48,004 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0078
════════════════════════════════════════════════════════════════════════════════
Unmatched log 50:
2015-07-30 16:12:14,000 - INFO [ProcessThread(sid:2 cport:-1)::PrepRequestProcessor@476] - Processed session termination for sessionid: 0x34ed9ac1c1e0085
════════════════════════════════════════════════════════════════════════════════
```
