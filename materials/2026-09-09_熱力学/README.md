# 熱力学 基本演習4題（改訂第3版・28ポイント）

2026-09-09 制作、2026-09-11 文字サイズ改訂。問題文・図は本教材用に独自作成。初版はGitの履歴に保存。

## ファイル

- [問題PDF（9ページ）](output/pdf/熱力学_問題.pdf)
- [解答PDF（14ページ）](output/pdf/熱力学_解答.pdf)
- [問題のLaTeX](source/problems.tex)、[解答のLaTeX](source/answers.tex)、[共通設定・TikZ図](source/style.tex)
- [レビュー記録](reviews/)

全ページ960 bp × 540 bp（338.67 mm × 190.5 mm）、16:9。本文・解答・見出し・図版ラベルは28 bp。PowerPointの標準ワイドスライドにページ全体を配置すると28ポイント相当になる。本文欄は420 bp幅（全角約15文字）。数式の添字・指数は通常のLaTeX組版に従う。日本語はHaranoAjiMincho、英数字はLatin Modern Roman、数式はLatin Modern Math。全フォントを埋め込み、文字・数式・図をベクトルで出力する。PowerPointではページ全体を16:9のスライドに合わせて配置する。PPTXそのものは今回の出力対象ではない。

## 問題構成

| 題 | 内容 | 問題PDF | 解答PDF |
| --- | --- | --- | --- |
| 1 | 負の傾きの斜辺を持つ三角形のサイクル、仕事、熱量、熱効率 | p.1〜2 | p.1〜4 |
| 2 | 鉛直ピストンのつり合い、定圧膨張・定積加熱・断熱圧縮 | p.3〜6 | p.5〜8 |
| 3 | 状態方程式、内部エネルギーの計算 | p.7 | p.9〜10 |
| 4 | 熱気球の密度、浮力、浮上する温度条件 | p.8〜9 | p.11〜14 |

気体が外部にした仕事を正、気体が吸収した熱量を正とする。第2問(4)の「された仕事」は周囲からの仕事の総量であり、別記号を使う。第4問は下部が開いた気球なので、内部の空気の質量は一定ではない。

## 再生成

TeX Live（XeLaTeX、extarticle、xeCJK、unicode-math、TikZ、HaranoAji・Latin Modernフォント）、Poppler、Python 3を使用。

```sh
python3 materials/2026-09-09_熱力学/build.py
```

各ファイルを2回コンパイルし、はみ出し・欠落文字の警告とページ数を検査して `output/pdf/` に保存する。変更後はPDFをPNGにレンダリングして目視確認する。中間出力は `tmp/pdfs/thermodynamics_v3/`。

## 参考と確認

- [利用者指定の参考資料](../../references/参考資料一覧.md)。元資料の文章や図の転載はしていない。
- 第2版の物理内容は4役でレビュー済み： [問題・数式チェック](reviews/problem_math_check_v2.md)、[解答原稿](reviews/answer_draft_v2.md)、[解答チェック](reviews/answer_check_v2.md)、[図版チェック](reviews/figure_check_v2.md)。末尾に `_v2` のない記録は初版のレビュー。
- 第3版では文字サイズとページ構成を改訂。[解答の再配置](reviews/answer_layout_v3.md)、[内容継承のチェック](reviews/content_check_v3.md)、[図版・表示チェック](reviews/figure_check_v3.md)、[サイズ・埋め込みの検証](reviews/typography_check_v3.md)を実施。
- [制作依頼と作業記録](../../records/2026-09-09.md)。

最新の追加指定と保存記録：[2026-09-11](../../records/2026-09-11.md)。
