---
title: 'MATLAB 配色与常用绘图'
summary: 'A practical palette and reusable snippets for MATLAB figures — clean bar, line, and 3D plots.'
date: '2025-11-15'
authors:
  - sky-huang
tags:
  - Tools
  - Visualization
  - MATLAB
categories:
  - tools
---

# 1. 三维柱状图

常用配色（hex）：

```text
#8ECFC9  #FFBE7A  #FA7F6F  #82B0D2  #BEB8DC  #E7DAD2
```

```matlab
% 颜色转换
colorHex = {'8ECFC9','FFBE7A','FA7F6F','82B0D2','BEB8DC','E7DAD2'};
colorRGB = zeros(length(colorHex), 3);
for k = 1:length(colorHex)
    colorRGB(k, :) = sscanf(colorHex{k}, '%2x%2x%2x') / 255;
end

% 生成数据
data = 10 * rand(5, 6) + 5;

% 创建图形
figure('Color', [1 1 1], 'Position', [200 200 800 500])
h = bar3(data);
```

更多内容见原文（含平面化样式设置、图例设置等）。本笔记整理自个人绘图经验，**所有代码片段仅作教学示例，使用请结合具体场景做适配**。
