import matplotlib.pyplot as plt
import numpy as np

# 数据（单位：亿元）
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
total = [385.33, 385.42, 391.49, 380.03, 383.45, 383.12, 383.95]
grassland = [360.72, 358.19, 361.55, 351.76, 352.07, 353.95, 350.71]
water = [16.38, 18.58, 21.53, 18.97, 21.87, 20.08, 22.54]
forest = [0.50, 0.68, 0.80, 0.98, 1.20, 1.10, 2.43]
unused = [7.18, 7.30, 7.09, 7.71, 7.65, 7.59, 7.70]          # 未利用地
cropland = [0.55, 0.67, 0.52, 0.61, 0.66, 0.40, 0.56]       # 耕地
construction = [0.0003, 0.0003, 0.0004, 0.0013, 0.0025, 0.0040, 0.0062]  # 建设用地

# 设置全局字体和字号
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 8
plt.rcParams['axes.linewidth'] = 0.6
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['lines.markersize'] = 2.0

# 创建图形，宽度7.5cm，高度11cm（加长）
fig = plt.figure(figsize=(7.5/2.54, 11.0/2.54))
gs = fig.add_gridspec(2, 1, height_ratios=[1.8, 1.2], hspace=0.08)

ax1 = fig.add_subplot(gs[0])   # 上部：总量+草地
ax2 = fig.add_subplot(gs[1])   # 下部：水域、林地、未利用地、耕地、建设用地

# Y轴范围
ax1.set_ylim(340, 400)
ax2.set_ylim(0, 25)

# 隐藏上部X轴刻度
ax1.tick_params(labelbottom=False, bottom=True, direction='in', length=3, width=0.6)
ax2.tick_params(direction='in', length=3, width=0.6)

# 设置Y轴刻度间隔
ax1.set_yticks(np.arange(340, 401, 10))
ax2.set_yticks(np.arange(0, 26, 5))

# 添加细网格线（仅纵向）
ax1.grid(True, axis='y', linestyle='--', linewidth=0.4, color='#cccccc', alpha=0.6)
ax2.grid(True, axis='y', linestyle='--', linewidth=0.4, color='#cccccc', alpha=0.6)

# 上部：总量和草地
ax1.plot(years, total, marker='o', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#4d4d4d', markerfacecolor='white',
         markeredgewidth=0.6, label='Total ESV')
ax1.plot(years, grassland, marker='s', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#2b8c4a', markerfacecolor='white',
         markeredgewidth=0.6, label='Grassland')
ax1.axhline(y=385.33, linestyle='--', linewidth=0.6, color='#999999', alpha=0.8)
ax1.text(1990.5, 385.6, '1990 baseline', fontsize=7, color='#666666', ha='left', va='bottom')

# 下部：水域、林地、未利用地、耕地、建设用地
ax2.plot(years, water, marker='^', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#1f78b4', markerfacecolor='white',
         markeredgewidth=0.6, label='Water area')
ax2.plot(years, forest, marker='d', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#e31a23', markerfacecolor='white',
         markeredgewidth=0.6, label='Forest land')
ax2.plot(years, unused, marker='v', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#ff7f00', markerfacecolor='white',
         markeredgewidth=0.6, label='Unused land')
ax2.plot(years, cropland, marker='p', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#6a3d9a', markerfacecolor='white',
         markeredgewidth=0.6, label='Cropland')
ax2.plot(years, construction, marker='*', linestyle='-', linewidth=1.0,
         markersize=2.0, color='#a6cee3', markerfacecolor='white',
         markeredgewidth=0.6, label='Construction land')

# 可选：参考线
ax2.axhline(y=16.38, linestyle=':', linewidth=0.5, color='#1f78b4', alpha=0.5)

# 轴标签
ax1.set_ylabel('ESV (10⁸ yuan)', fontsize=8, labelpad=2)
ax2.set_ylabel('ESV (10⁸ yuan)', fontsize=8, labelpad=2)
ax2.set_xlabel('Year', fontsize=8, labelpad=2)

# X轴刻度
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=0)

# 图例：上部图例左下，下部图例放在upper left，双列
ax1.legend(loc='lower left', frameon=False, fontsize=7, handlelength=1.5, borderaxespad=0.2)
ax2.legend(loc='upper left', frameon=False, fontsize=7, handlelength=1.5, borderaxespad=0.2, ncol=2)

# 折断标记
d = 0.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=6,
              linestyle='none', color='k', mec='k', mew=0.7, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# 内侧刻度
ax1.tick_params(axis='y', which='both', direction='in')
ax2.tick_params(axis='y', which='both', direction='in')

plt.tight_layout(pad=0.5)

# 同时保存PDF和PNG
plt.savefig('ESV_all_broken.pdf', dpi=300, bbox_inches='tight')
plt.savefig('ESV_all_broken.png', dpi=300, bbox_inches='tight')
plt.show()