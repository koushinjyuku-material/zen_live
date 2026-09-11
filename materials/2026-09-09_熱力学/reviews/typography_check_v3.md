# 第3版 文字サイズ・PDF仕様の検証

2026-09-11、主担当による最終PDFの実測。

## 結果

- PowerPoint標準ワイドと同じ960 × 540 PDFポイント（16:9）。
- 本文欄420 bp、本文28 bpのため全角約15文字幅。
- 日本語本文・見出し・図ラベルは実測28.00ポイント。英数字・数式の主文字も28ポイント。添字・指数・インライン分数等の数学上必要な部分のみ通常の縮小。
- 図のresizeboxを廃止し、図形の寸法と文字サイズを独立に設定。
- 全23ページの文字はページ内。フォントはすべて埋め込み。
- 最終LaTeXビルドは意図どおり問題9ページ、解答14ページ。Overfull、Underfull、Missing characterの警告なし。

| ファイル | ページ | 日本語サイズ | 最小左端 | 最大右端 | 最上端 | 最下端 |
| --- | --- | --- | --- | --- | --- | --- |
| 熱力学_問題.pdf | 1 | 28.00 | 42.00 | 918.00 | 29.22 | 422.05 |
| 熱力学_問題.pdf | 2 | 28.00 | 42.00 | 918.01 | 29.22 | 433.72 |
| 熱力学_問題.pdf | 3 | 28.00 | 42.00 | 918.00 | 29.22 | 458.25 |
| 熱力学_問題.pdf | 4 | 28.00 | 42.00 | 918.00 | 29.22 | 369.96 |
| 熱力学_問題.pdf | 5 | 28.00 | 42.00 | 918.01 | 29.22 | 373.63 |
| 熱力学_問題.pdf | 6 | 28.00 | 42.00 | 918.01 | 29.22 | 390.19 |
| 熱力学_問題.pdf | 7 | 28.00 | 42.00 | 918.00 | 29.22 | 433.10 |
| 熱力学_問題.pdf | 8 | 28.00 | 42.00 | 918.00 | 29.24 | 474.42 |
| 熱力学_問題.pdf | 9 | 28.00 | 42.00 | 934.23 | 29.24 | 391.17 |
| 熱力学_解答.pdf | 1 | 28.00 | 42.00 | 918.00 | 29.22 | 422.02 |
| 熱力学_解答.pdf | 2 | 28.00 | 42.00 | 918.00 | 29.22 | 431.84 |
| 熱力学_解答.pdf | 3 | 28.00 | 42.00 | 918.00 | 29.22 | 438.25 |
| 熱力学_解答.pdf | 4 | 28.00 | 42.00 | 918.00 | 29.22 | 371.31 |
| 熱力学_解答.pdf | 5 | 28.00 | 42.00 | 918.00 | 29.22 | 458.20 |
| 熱力学_解答.pdf | 6 | 28.00 | 42.00 | 918.00 | 29.22 | 401.94 |
| 熱力学_解答.pdf | 7 | 28.00 | 42.00 | 918.00 | 29.22 | 453.37 |
| 熱力学_解答.pdf | 8 | 28.00 | 42.00 | 918.00 | 29.22 | 435.61 |
| 熱力学_解答.pdf | 9 | 28.00 | 42.00 | 918.00 | 29.22 | 382.80 |
| 熱力学_解答.pdf | 10 | 28.00 | 42.00 | 918.00 | 29.22 | 349.60 |
| 熱力学_解答.pdf | 11 | 28.00 | 42.00 | 918.00 | 29.22 | 473.47 |
| 熱力学_解答.pdf | 12 | 28.00 | 42.00 | 918.00 | 29.24 | 320.59 |
| 熱力学_解答.pdf | 13 | 28.00 | 42.00 | 918.00 | 29.24 | 438.45 |
| 熱力学_解答.pdf | 14 | 28.00 | 42.00 | 918.00 | 29.24 | 442.74 |

## 熱力学_問題.pdf のフォント埋め込み

```text
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
EFJKTG+HaranoAjiMincho-Bold-Identity-H CID Type 0C       Identity-H       yes yes no       5  0
ALIYYK+LMRoman10-Bold-Identity-H     CID Type 0C       Identity-H       yes yes yes      7  0
QMVOIH+LMRoman10-Regular-Identity-H  CID Type 0C       Identity-H       yes yes yes      9  0
NUBVTA+LatinModernMath-Regular-Identity-H CID Type 0C       Identity-H       yes yes yes     11  0
MBIZBR+HaranoAjiMincho-Regular-Identity-H CID Type 0C       Identity-H       yes yes no      13  0
```

SHA-256: `6e7e94c86d06b6ac53ce588f06f25922bd0c817312884672d108b5dd3eeb81e4`

## 熱力学_解答.pdf のフォント埋め込み

```text
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
AXBZPV+HaranoAjiMincho-Bold-Identity-H CID Type 0C       Identity-H       yes yes no       5  0
PIXSFX+LMRoman10-Bold-Identity-H     CID Type 0C       Identity-H       yes yes yes      7  0
KOMCAF+LMRoman10-Regular-Identity-H  CID Type 0C       Identity-H       yes yes yes      9  0
GAOPPG+HaranoAjiMincho-Regular-Identity-H CID Type 0C       Identity-H       yes yes no      11  0
JGWKHA+LatinModernMath-Regular-Identity-H CID Type 0C       Identity-H       yes yes yes     13  0
```

SHA-256: `9df7ceb340b4af99848cba82154cb97acd4c255db2c001643fda96ddb8c2571d`
