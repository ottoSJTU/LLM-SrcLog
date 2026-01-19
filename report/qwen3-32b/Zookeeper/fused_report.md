# Log Analysis Report

## Log matched templates
| Metric | Value |
|------|-----|
| Precision | 0.8235 (42/51) |
| Recall    | 0.9545 (42/44) |
| F1-Score  | 0.8842 |

## Statistical Overview
- Total log count: `2000`
- Matched log count: `2000`
- Log match rate: `100.00%`
- Number of matched templates: `52`

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
| `Closed socket connection for client <.*> which had sessionid <.*>` | 44 |
| `Unexpected Exception:` | 1 |
| `Processed session termination for sessionid: <.*>` | 47 |
| `Closed socket connection for client <.*> (no session established for client)` | 4 |

## Matched Content Details

## Unmatched Log Details
**All logs were successfully matched**
