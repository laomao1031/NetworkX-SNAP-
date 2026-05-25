# NetworkX-SNAP-
Nodes |V|: 4039
Edges |E|: 88234
Average Degree: 43.69
BFS Average Time: 0.017427 seconds
DFS Average Time: 0.021382 seconds
Time Difference (DFS - BFS): 0.003955 seconds

心得與瓶頸分析
本實驗對 Facebook 社交網路進行走訪。該圖具備高密度、短直徑的小世界網路特性。數據顯示 BFS 執行效率優於 DFS。

兩者的效能瓶頸在於記憶體存取模式。BFS 採用佇列結構，能對鄰接節點進行連續性的記憶體存取，具備更好的快取局部性。

相反地，DFS 的瓶頸在於其深度優先的遞迴機制。在高度稠密網絡中，DFS 會在記憶體中維護極深的調用棧，頻繁進行入棧與出棧。這種行為伴隨大量隨機記憶體尋址與指針跳轉，容易導致快取缺失，因此執行速度較慢。
