---
title: 'MATLAB 配色与常用绘图'
summary: '一份 MATLAB 学术绘图小抄:6 个常用图型(3D 柱、热图、曲面、等高线、多子图、出图)+ 配色方案 + 出版质量导出参数 + 平替 python 写法。'
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

> 适用于:实验报告、毕设 paper、组会 slide。
> 配色:用 [小川由明雄 Yumi Ochiai]/[科学人 COLORMAPS] 风格的中等亮度饱和调色,打印不脏,投影不瞎。

## 共享: 6 套调色板(hex)

```text
# 经典清爽
#2E5A87  #4F94CD  #82B0D2  #B6D7E8  #E8F0F8

# 暖 — 经典 Nature 风格
#E07B43  #E6B566  #E2CB88  #C4A77D  #94724F

# 冷 — 论文常用
#3B528B  #21908D  #5DC863  #FDE725  #440154

# 复古高饱和
#8ECFC9  #FFBE7A  #FA7F6F  #82B0D2  #BEB8DC  #E7DAD2

# 李代数体
#C1A875  #A49374  #826644  #615041

# 灰阶
#222831  #393E46  #666B70  #9DA1A7  #C6CACF
```

---

## 1. 三维柱状图(bar3)

常用配色(hex 复现) —— `8ECFC9, FFBE7A, FA7F6F, 82B0D2, BEB8DC, E7DAD2`:

```matlab
% 颜色转换
colorHex = {'8ECFC9','FFBE7A','FA7F6F','82B0D2','BEB8DC','E7DAD2'};
colorRGB = zeros(length(colorHex),3);
for k = 1:length(colorHex)
    colorRGB(k, :) = sscanf(colorHex{k},'%2x%2x%2x') / 255;
end

% 模拟数据
data = 10 * rand(5, 6) + 5;

% 创建图形
figure('Color',[1 1 1], 'Position',[200 200 800 500])
h = bar3(data);

% 平面化样式 (无边框、扁平上色)
for k = 1:length(h)
    h(k).FaceColor = colorRGB(k, :);
    h(k).EdgeColor = 'none';
end

% 标签与视角
xlabel('X axis'); ylabel('Y axis'); zlabel('Z axis');
title('3D bar example');
view(-37.5, 30);

set(gca, 'FontName', 'Arial', 'FontSize', 10);
set(gcf, 'PaperPositionMode', 'auto');
```

---

## 2. Heatmap(热图)

single-cell / GRN / correlation matrix 必备。

```matlab
% 数据:基因 × 样本
genes   = 50;
samples = 30;
mtx = randn(genes, samples);
mtx = smoothdata(mtx, 1, 'movmean', 3);  % 行方向平滑

% 配色:用 cbrewer / crameri 系(避免 jet 的色觉不友好)
figure('Color',[1 1 1], 'Position',[300 300 800 600])
imagesc(mtx);
% colormap 用 parula 替代 jet,或者从 cmocean 加载
colormap(cmocean('balance'));  % diverge 配色,适合 correlation
% colormap(parula);            % 序列配色,适合单方向的值
clim([-2 2]);                  % 对称色阶

% 颜色条 + 标签
cb = colorbar; ylabel(cb, 'value');
xlabel('Sample'); ylabel('Gene');
title('Heatmap');

% 轴标签替代数字
set(gca, 'XTick', 1:samples, 'XTickLabel', compose('S%d', 1:samples), ...
         'YTick', 1:genes,   'YTickLabel', compose('g%d', 1:genes));
set(gca, 'TickLabelInterpreter', 'none', 'FontSize', 8);
```

**配色陷阱**:`jet` 是色觉不友好(红绿色盲看不出),能不用就不用。`viridis` / `cmocean('balance')` / `cmocean('curl')` 更合适。

---

## 3. 曲面图(surf)

密度曲面、流形可视化。

```matlab
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3);
Z = peaks(X, Y);   % MATLAB 自带样例曲面

figure('Color',[1 1 1], 'Position',[200 200 800 600])
surf(X, Y, Z, 'EdgeColor','none', 'FaceAlpha',0.95);
colormap(cmocean('thermal'));   % 序列色映射
clim([min(Z(:)) max(Z(:))]);

shading interp;       % 平滑插值
lighting gouraud;     % 漫反射光照
camlight right;       % 加一个右光源
axis tight; grid off;

title('3D surface');
xlabel('X'); ylabel('Y'); zlabel('Z');
view(-45, 35);
```

---

## 4. 等高线 + 填充(contourf)

适合 loss landscape / 误差等高线 / 决策边界。

```matlab
[X, Y] = meshgrid(-3:0.05:3, -3:0.05:3);
Z = peaks(X, Y);

figure('Color',[1 1 1], 'Position',[200 200 800 600])
contourf(X, Y, Z, 20, 'LineColor','none');
colormap(cmocean('haline'));     % 任意喜欢的顺序色
cb = colorbar; ylabel(cb, 'level');

hold on
contour(X, Y, Z, 10, 'LineColor',[.2 .2 .2 .4], 'LineWidth', 0.5);  % 半透明叠加线条
hold off

title('Filled contour');
xlabel('X'); ylabel('Y');
axis tight; axis square;
```

---

## 5. 多子图(multi-panel figure)

论文 figure 一般 2-4 个子图(A/B/C/D)。

```matlab
figure('Color',[1 1 1], 'Position',[200 200 1200 400])

% 子图 A: 折线
subplot(1, 3, 1);
plot(0:0.01:1, sin(0:0.01:1)*0.5 + randn(1,101)*0.05, 'LineWidth', 1.5, 'Color', colorRGB(1, :));
title('(A) line'); xlabel('time'); ylabel('y');
axis tight; box off;

% 子图 B: 散点
subplot(1, 3, 2);
scatter(randn(200,1), randn(200,1), 20, rand(200,1), 'filled');
colormap(gca, cmocean('thermal'));
cb = colorbar; ylabel(cb, 'value');
title('(B) scatter'); xlabel('x'); ylabel('y');
axis tight; box off;

% 子图 C: 直方图
subplot(1, 3, 3);
histogram(randn(1000,1), 30, 'FaceColor', colorRGB(3, :), 'EdgeColor','none');
title('(C) histogram'); xlabel('value'); ylabel('count');
axis tight; box off;

% 统一字体
set(findall(gcf, '-property', 'FontName'), 'FontName', 'Arial', 'FontSize', 10);
```

---

## 6. 出图(出版质量)

paper / 投稿必备参数:

```matlab
f = gcf;
f.Units = 'inches';
f.Position = [1 1 7 5];      % 横向 7×5 inch(Nature 单栏常用)
f.PaperPositionMode = 'auto';

% 导出 600 DPI PDF(矢量)
print(f, 'figure_name', '-dpdf', '-r600', '-vector');
% 备用:导出 600 DPI PNG
print(f, 'figure_name', '-dpng', '-r600');

% 让所有文字统一为 Arial,大小匹配模板
set(findall(f, '-property', 'FontName'), 'FontName', 'Arial');
set(findall(f, '-property', 'FontSize'), 'FontSize', 8);
```

**实用建议**:
- 期刊要求**矢量 PDF** 优先(`-dpdf -vector`)
- 双栏宽度**单栏 ~3.15 in**,**双栏 ~6.5 in**
- 字号 6-8 pt 在 Nature / Science 都不算小,正文 8-9 pt
- 颜色一次性选定,**灰度打印不出**(色觉无障碍公式:色 + 形状)

---

## 7. 平替 Python(matplotlib)

如果因为协作 / AI 集成需要切到 Python:

```python
import matplotlib.pyplot as plt
import numpy as np

# 配色与 MATLAB 完全一致(传 hex 字符串即可)
color_hex = ['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2']

X = np.random.randn(5, 6) * 2 + 8
fig, ax = plt.subplots(figsize=(8, 5))
for k, c in enumerate(color_hex):
    ax.bar(np.arange(6) + k * 0.13, X[k], width=0.13, color=c)

ax.set_xlabel('group'); ax.set_ylabel('value')
ax.spines[['top','right']].set_visible(False)
plt.tight_layout()
plt.savefig('out.pdf', dpi=600, bbox_inches='tight')
```

```python
import seaborn as sns
sns.set_theme(style="white", font="Arial")
sns.heatmap(corr, cmap="RdBu_r", center=0, annot=True, fmt=".2f")
```

---

## 一些容易出的细节

1. **图中字号 vs 论文字号**——图内 8 pt = Nature 排印后 ~6-7 pt readable。
2. **颜色顺序与图例一致**——别让读者来回跳。
3. **colorbar 别和图形重叠**——`colorbar('Position',[.9 .1 .02 .8])` 手动放。
4. **X 轴用科学记数法**——`set(gca, 'XTick', [1e3 1e4 1e5], 'XTickLabel', {'1k' '10k' '100k'})`。
5. **P 值的星号**——直接写在图上,不要让读者到正文里找(`'p < 0.001'`, `'**'` 等)。

---

## 完整脚本: 一张可提交的论文 figure

```matlab
% 创建数据
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3);
Z = peaks(X, Y) + randn(size(X)) * 0.5;

% 配色
colors = sscanf('8ECFC9FFBE7AFA7F6F82B0D2BEB8DCE7DAD2', ...
                '%2x%2x%2x', [3 6])' / 255;

% 图形
figure('Color', [1 1 1], 'Position', [200 200 800 600]);
set(gcf, 'DefaultAxesFontSize', 8, ...
         'DefaultAxesFontName', 'Arial');

% 左图:曲面
ax1 = subplot(1, 2, 1);
surf(X, Y, Z, 'EdgeColor', 'none', 'FaceAlpha', 0.95);
colormap(ax1, cmocean('thermal'));
shading interp; camlight right; lighting gouraud;
axis tight; grid off;
title('(A) density surface');
xlabel('x'); ylabel('y'); zlabel('density');

% 右图:等高线
ax2 = subplot(1, 2, 2);
contourf(X, Y, Z, 20, 'LineColor','none');
colormap(ax2, cmocean('haline'));
cb = colorbar; ylabel(cb, 'level');
axis tight; axis square;
title('(B) filled contour');
xlabel('x'); ylabel('y');

% 导出
set(gcf, 'PaperPositionMode', 'auto');
print(gcf, 'figure1', '-dpdf', '-r600', '-vector');
```

---

## 推荐资源

- MATLAB `cmocean` 配色包:GitHub `chadagregg/cmocean`(我也搬了核心函数到 `D:\study\matlab\cmocean\`)
- ColorBrewer:科学 / 色觉无障碍配色(cmocean / viridis / cividis 都参考它)
- MATLAB 官方 docs:`docs/charts.html` 的例子很多可以直接拿来改
- python 平替:matplotlib + seaborn,接口几乎是 MATLAB 一对一

放一条经验:**你以后 90% 的图都是同一份模板的微调**。把一份"已经调好字体 / 颜色 / 出图"的 figure script 存起来,每篇论文配一次新的,效率最高。
