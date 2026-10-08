> この比較は改善着手前の調査スナップショットです。[現在の成果物](../starter-status.md)を参照してください。競合の未確認は機能欠如を意味しません。

# 公開スキル比較と差別化案

調査日: 2026-10-09 JST。調査開始時刻: 08:07:32 +09:00。公開GitHub・WHATWG・W3C WAI・Google Search Centralのみを参照した。公開リポジトリの `main` コミットをGitHub APIで取得し、代表スキルとREADMEを固定コミットURLから再読した。競合の導入・スクリプト・ブラウザー操作は実行していない。スター数、利用者数、性能、生成品質の優劣は測定していない。

## 結論

「ネイティブHTMLを優先する」「アクセシビリティを確認する」「実行証拠と推測を分ける」だけでは、確認した公開スキルとの差別化が弱い。最も近い `frontend-a11y` は `details`、`dialog`、リンク・ボタンの使い分けやフレームワークへの適用を既に具体化している。Addy Osmaniのスキルは実測、ソース仮説、アクセシビリティツリー、手動確認を区別している。

このプロジェクトでは、**コンテンツの意味をカンプ段階から記録し、その判断をHTML・操作・実際の証拠までつなげる**経路を、使える小さな参照例として示すのが有望である。これは調査範囲からの設計上の推論であり、世界初・競合唯一という主張ではない。

現在の `semantic-html` はsemantic blueprint、要素選択の判断順序、FAQ・引用・カード・表・フォーム、標準の要求と推奨とプロジェクト慣習の区別を既に草案に含む。まずこの資産を初回利用者が実践できる経路にする。未実装のルールエンジンやスキーマを実装済みとして紹介しない。

## 比較の読み方

- **観察**: 下記の代表スキル・README・明示した補足資料に書かれている事項。
- **推論**: 観察から提案した改善方向。生成品質や導入成功の実測ではない。
- **未確認**: 今回読んだ範囲に明示を確認できなかった、または実行を伴う確認をしていない事項。「機能がない」という意味ではない。
- 比較対象は近い公開スキル7リポジトリ。リポジトリ全体の能力を代表ファイルだけから断定しない。
- 以下の導入経路は各READMEの記載の観察であり、この環境での互換性保証ではない。

## 参照版と一次資料

固定コミットは調査時の `main` 先端であり、そのスキル単体の最終変更コミットを表すものではない。

| ID | リポジトリ・固定コミット | 実際に読んだ代表ファイル | README |
|---|---|---|---|
| A | `anthropics/skills` / `683bc88e56f3e09ba94f7055977f3d3aa499f202` | [frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design/SKILL.md) | [README](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/README.md) |
| B | `vercel-labs/agent-skills` / `063bee94c3f4df8453406c830b0a7df0f2860278` | [web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md)、参照先[command.md](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) | [README](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md) |
| C | `google-labs-code/stitch-skills` / `0337446dadde6f8c94210444e2aa9d546126480f` | [design-md/SKILL.md](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/plugins/stitch-utilities/skills/design-md/SKILL.md) | [README](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/README.md) |
| D | `mgifford/accessibility-skills` / `ada839399f053c55e1a776a98c02f8904d70dd32` | [ACCESSIBILITY-general/SKILL.md](https://github.com/mgifford/accessibility-skills/blob/ada839399f053c55e1a776a98c02f8904d70dd32/skills/ACCESSIBILITY-general/SKILL.md)、[forms](https://github.com/mgifford/accessibility-skills/blob/ada839399f053c55e1a776a98c02f8904d70dd32/skills/forms/SKILL.md)、[tables](https://github.com/mgifford/accessibility-skills/blob/ada839399f053c55e1a776a98c02f8904d70dd32/skills/tables/SKILL.md) | [README](https://github.com/mgifford/accessibility-skills/blob/ada839399f053c55e1a776a98c02f8904d70dd32/README.md) |
| E | `addyosmani/web-quality-skills` / `afa8da942115f2961fdbfa80807ea0b232ff6c00` | [web-quality-audit/SKILL.md](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/skills/web-quality-audit/SKILL.md)、[accessibility](https://github.com/addyosmani/web-quality-skills/blob/main/skills/accessibility/SKILL.md) | [README](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/README.md) |
| F | `pbakaus/impeccable` / `30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f` | [生成済みSKILL.md](https://github.com/pbakaus/impeccable/blob/30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f/plugin/skills/impeccable/SKILL.md)、[SKILL.src.md](https://github.com/pbakaus/impeccable/blob/30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f/skill/SKILL.src.md)、[craft-floor](https://github.com/pbakaus/impeccable/blob/30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f/skill/reference/craft-floor.md)、[audit](https://github.com/pbakaus/impeccable/blob/30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f/skill/reference/audit.md) | [README](https://github.com/pbakaus/impeccable/blob/30cdd375d1acd5dc3d3e31e1eeb3e83ec518002f/README.md) |
| G | `mikemai2awesome/agent-skills` / `b225980138789535683bf4cf17b6871f10c188ce` | [frontend-a11y/SKILL.md](https://github.com/mikemai2awesome/agent-skills/blob/b225980138789535683bf4cf17b6871f10c188ce/skills/frontend-a11y/SKILL.md) | [README](https://github.com/mikemai2awesome/agent-skills/blob/b225980138789535683bf4cf17b6871f10c188ce/README.md) |

Fは生成元 `SKILL.src.md` とプラグイン向け生成済み `SKILL.md` を両方読んだ。生成済み配布物の全ホスト検証はしていない。Bの外部 `command.md` とEの補足 `accessibility` は調査日取得の `main` を読んだ補足で、上表の固定版に内包されると見なしていない。

## 観察: ワークフロー・証拠・導入

| 対象 | 中心となる仕事 | カンプ前の意味構造・blueprint | ネイティブ操作 | 実際の証拠の扱い | 導入記載 |
|---|---|---|---|---|---|
| A | 美的方向・文字・レイアウト・文章をブリーフから作る | 内容に基づく視覚構造とデザイン計画。HTML要素選択のblueprint形式は代表ファイルでは未確認 | フォーカス・動きの配慮はある。個別HTMLパターンは未確認 | 利用可能ならスクリーンショットで自己確認。標準適合判定手順は未確認 | Claude向けプラグインとAPI等。教育・デモ用途の制限を明記 |
| B | 指定ソースを最新Web Interface Guidelinesでレビュー | レビュー入口。制作前blueprintは代表ファイルでは未確認 | actionはbutton、navigationはlink、semantic HTML優先を外部ガイドに明示 | `file:line`の指摘。ブラウザー実測を必須とする記載は代表ファイルでは未確認 | `npx skills add vercel-labs/agent-skills` |
| C | Stitch画面の視覚言語をDESIGN.mdへ抽出 | 色の役割・形・文字・余白の意味。HTML content modelのblueprintと同じ意味ではない | 代表design-mdは主に見た目の抽出。個別操作パターンは未確認 | HTML・画像・メタデータをStitch MCPから取得。取得と適合確認は別 | プラグイン、選択導入、手動導入。Stitch MCPと依存スキルが必要 |
| D | ACCESSIBILITY.mdの要求、分野別パターン、検査・報告 | 表では構造を先に選ぶ。全制作経路共通のblueprintは確認範囲では未確認 | ネイティブ優先。フォーム・表に詳細ガイド | 手動検査・自動検査・既知の不足・完了条件を扱う | `npx skills add`、手動参照等。記載経路の実動作は未確認 |
| E | 実行可能なサイトの性能・a11y・SEO・品質監査 | 主に実行サイトからの診断。カンプ制作前blueprintは確認範囲では未確認 | native優先、名前・役割・状態、キーボードを扱う | 実測とソース仮説、labとfield、手動と自動を区別。a11y treeも読む | `npx skills add`、ホスト別導入。DevTools MCPは任意で代替あり |
| F | デザイン・UX・制作・改善、ローカル検出器 | shape・コンテンツ・PRODUCT.md・DESIGN.md、comp-first経路をREADMEに記載 | auditで意味HTML・操作・フォーカスを扱う | 表示確認と検出器。READMEはclean scanを証明と扱わず、auditは評価点も使う | 専用installer、手動配布、ホスト別パッケージ。導入結果は未確認 |
| G | 少ないHTML/CSS/JSでアクセシブルなUIを作る | native-firstと意味要素、既存スタックへの変換。コンテンツ関係のblueprint契約は代表ファイルでは未確認 | button、details/summary、dialog/showModal、開閉navigationに具体例 | 標準参照と手動上の注意。実行結果を6状態で記録する契約は代表ファイルでは未確認 | `npx skills add ... --skill frontend-a11y`、同梱references |
| 本件 | カンプ→HTML、ブリーフ→カンプ、既存サイトレビュー | 内容関係・順序・要素・根拠・未解決事項をblueprint草案に記録 | 開閉navigationの状態判断は草案。動作する参照例は未実装 | 6状態、根拠種別、実施・未実施を区別する草案 | リポジトリ全体の参照。単体切出しの相対参照とホスト対応は未検証 |

A–Gの各行は上記の当該SKILL・README・補足への参照で裏付ける。特徴が重なることを確認した表であり、性能順位表ではない。

## 観察: コンテンツ・言語・検索・アクセシビリティ

| 対象 | HTML content model・内容関係 | 表・フォーム | 言語・l10n | SEO | a11y |
|---|---|---|---|---|
| A | 視覚構造は情報を表すとの指針。要素の許可関係の表は代表ファイルでは未確認 | 代表ファイルでは詳細未確認 | 文章と対象者の語彙。l10n詳細は未確認 | 代表ファイルでは詳細未確認 | focus、reduced motion、見た目のa11yを品質下限として記載 |
| B | semantic HTML優先、link/action、見出し階層 | label、入力型、エラー、tableの使用を外部ガイドに記載 | Intlの日付・数値を扱う | 代表範囲では包括的SEO経路は未確認 | 名前、代替、focus、keyboard等のチェック |
| C | 色・コンポーネントの機能的役割と視覚語彙 | input/formのスタイルを抽出 | 自然言語で記述。HTMLのlang・l10n詳細は未確認 | design-md代表では未確認 | design-md代表では詳細未確認 |
| D | semantic-first、表のデータ関係と適切な構造 | forms・tables専門スキルを実読。label、error summary、th/scope等 | フォームのlocale考慮、plain languageルート | 代表範囲では検索専用経路は未確認 | WCAG・AT・検査・深い分野別ガイド |
| E | native要素、正しいネスト、見出し・名前・役割・状態 | labels、フォームエラー。包括的表の意味選択は代表範囲で未確認 | lang、言語変更の例 | crawl、canonical、metadata、JSON-LD、ランキング保証を分離 | 自動＋a11y tree＋キーボード＋手動 |
| F | auditで見出し・landmark・div vs buttonを扱う | forms、エラー状態、内容overflow等 | hardenはi18n・edge caseを扱う | 読んだ代表範囲で専用SEO経路は未確認 | audit、意味HTML、focus、contrast、表示確認 |
| G | meaning elements、region命名、native vs ARIA | labels、form errors、field操作。表の詳細は代表範囲で未確認 | CSS logical propertiesとRTL。フレームワーク別referencesを持つ | frontend-a11y代表では未確認 | native widget、名前、role/state、WCAG参照を具体化 |
| 本件 | content modelの要求・推奨・記述と、慣習・判断を草案で区別 | 内容に応じた表/list選択、label・入力型・未確定値を草案で扱う | 英日README、language/locale/marketを区別する方針。RTL等の実証は未確認 | provider一次資料、metadata、検索・AI引用を分ける草案 | manual checksは短い草案。AT・端末・ブラウザーを未検証と明示 |

## 公式資料が示す故障の種類

以下はAIで生成する場合にも防ぎたい**故障の分類**である。AI生成サイトでの発生率、既存サイトより多いという比較、特定モデルの弱さを測った資料ではない。AI固有の問題と一般的なWeb実装の問題を同一視しない。

| 故障の種類 | 一次資料から確認できること | 本件で示す具体的な予防・証拠 |
|---|---|---|
| 情報の関係が見た目にしかない | [WCAG 1.3.1の解説](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)は、表示が伝える構造・関係をプログラムが判断できるか文章で提供する要件を説明する | 順序list/peer list/name-value/tableを内容から選び、blueprintとDOMを対応させる |
| divを置換しただけ、section/articleを過剰使用 | [WHATWG grouping content](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element)はdivの意味と最後の候補という著者向け推奨を記す。単純なdiv個数で適合失敗は判定できない | スタイルだけのdivを許容し、semantic elementの判断根拠を残す。HTML要求・推奨・慣習を分ける |
| 表の列・行の関係をカード表示で失う | [WAI tables](https://www.w3.org/WAI/tutorials/tables/)はheader/dataの関係を示すmarkupと複雑表の関連付けを説明する | 比較matrixとpeer cardの選択理由、th/scope、狭幅時の確認を参照例にする |
| ラベル・入力説明がplaceholderだけ | [WAI form labels](https://www.w3.org/WAI/tutorials/forms/labels/)はラベル関連付けとplaceholderの限界を説明する | visible label、関連付け、errorの結び付けをカンプ段階で見せる |
| クリックだけで使え、キーボードで仕事が完了しない | [WCAG 2.1.1の解説](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)はkeyboard interfaceでの機能操作と例外を説明する | link/buttonを行為から選び、Tab/Enter/Space、開閉・Escape・focus returnを実際に記録する |
| 見出しや領域が視覚再現だけ | [WAI page structure](https://www.w3.org/WAI/tutorials/page-structure/)は適切な要素・見出し・領域によるnavigationを説明する | カンプの文字サイズとheading levelを分け、DOM/a11y treeで確認する |
| ARIA属性を付ければ操作も完成したと見なす | [WAI APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)はARIAの誤用を避け、ネイティブHTMLと実際の動作・支援技術確認を重視する | まずnative要素。ARIAだけで合格にせず、役割・状態・操作を確認する |
| 言語が宣言されていない | [WCAG 3.1.1の解説](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)はページの主言語をプログラムが判断できることを説明する | html langの設定、ページ内言語変更の必要性を扱う。言語から法域を推測しない |
| metadataやsemantic HTMLをSEO成功の証明にする | [Google Search Essentials](https://developers.google.com/search/docs/essentials)は要件・推奨を満たしてもcrawl/index/表示を保証しないとする | emitted metadataとvisible contentを確認し、検索掲載・順位・AI引用の実績を別にする |

WAI Tutorials、Understanding、APGは説明・実装ガイダンスであり、HTML規範本文やWCAG適合要件そのものと同列に扱わない。WHATWGでも要求と推奨を区別する。

## 現在の本件の不足

調査時に読んだローカル資料: `README.ja.md`、`docs/starter-status.md`、`docs/compatibility.md`、入口・semantic-html・native-interactions・accessibility・search-contentのSKILL、content-models/content-patterns/navigation/manual-checks、`examples/semantic-comparison/README.md`。他担当の並行編集があるため、この一覧は調査時の観察範囲である。

1. **使い方を読めるが、初回の成果を手元で確かめる例がない。** semantic-comparisonはplannedと明示。READMEも runnable demo、runner、CI、installer等を未実装とする。
2. **blueprintが良い判断契約になっている一方、完成例まで連続して追えない。** FAQ・引用・カード・表・フォームのsketchはあり、さらに同じ入力からblueprint→HTML→実行証拠を見せる余地がある。
3. **native-interactionsとaccessibilityの専門入口・参照が短い。** navigationには状態区別があるが、具体的な実装と再現手順がない。frontend-a11y等のパターンを参照し、一般論の追加より操作可能な例を優先する。
4. **配布の依存関係が初回導入を阻む。** repository-relative linksを単一SKILLとして切り出すと壊れ得る。どのホストも動作確認されていないという制限は維持する。
5. **SEO・地域対応を広く掲げると目的の説明が長くなる。** 入口はsemantic sourceの具体的な改善に置き、検索・地域は関係する作業で専門草案を読む構成が適切と推論する。

## 優先改善案

| 順位 | 改善案 | 初回利用者に見せる成果 | 完了を確かめる条件 |
|---|---|---|---|
| 1 | 実行できる小さな意味HTML参照例を1件作る | ナビゲーション、FAQ、引用または比較表、フォームを含むHTMLとblueprint。表示を整えた実例からソースに入れる | 記録した条件でHTML確認、DOM、keyboardの結果を実際に残す。未実施AT・実機はuntested |
| 2 | READMEから1回の試行へつなぐ短いquickstart | 入力例、コピーできる依頼文、読むファイル、出力先、レビュー箇所 | 既存の未検証表示を維持しつつ、手順の参照先が全て存在する。スキル実行・ホスト成功と文書検査を分ける |
| 3 | semantic blueprintの判断例を完成例で見せる | 同じcard外観でもlist/table/articleが違う例、FAQのdl/details選択、標準・慣習・判断の違い | 意味判断と規範要求に一次資料があり、視覚入力だけの推測はneeds_review、過剰semantic化の反例もある |
| 4 | native操作の状態とfocusを参照例へ具体化 | disclosureとmodalの違い、閉じた状態・リンク選択・Escape・戻るfocus・resize | 閉じた領域のフォーカス到達、開閉状態、focusの実動作を手順別に記録。native要素使用だけで適合を宣言しない |
| 5 | 依存を同梱したportable bundleを設計し、1ホストで確認する | entrypointと必要referencesを壊れず渡せる配布物、任意の専門ガイド、削除方法 | パッケージ内リンク、host/version、実際の呼出し、参照読込み、生成物、除去を記録。manifest/schemaが存在するだけでsupportとは呼ばない |

参照例の内容と作る順序は提案であり、この調査担当は製品コードを変更していない。1と3は同じ参照例で同時に示せる。portable bundleは有力な導入改善だが、今回の作業時点では実装・対応ホストを未確認として扱う。

## 広めるための導線案

「適切なHTMLを使いましょう」という一般的な説明から始めるより、1つの具体例と意味の判断をすぐ見せる導線を推奨する。

1. READMEの冒頭に目的と現在の実装段階を短く示す。
2. 参照例の画面を開き、同じ例のHTMLとblueprintを隣のリンクで読めるようにする。
3. すぐ下に、同じ例を変更して試すコピー可能な依頼文を置く。
4. 最初はリポジトリ全体を参照する試行を案内する。検証していない `npx skills add` や全エージェント対応を保証しない。
5. ポータブル配布物の参照整合と1ホストでの実行を確認できた時点で、そのホスト・版・呼出しだけをcompatibilityに記録する。
6. 貢献者には「出典のあるcontent判断」「動作する小さな例」「誤検出・境界例」「試した環境と失敗」を受け付ける。スターの増加やSEO成果を保証しない。

コピー可能な依頼文の案:

> このリポジトリの入口スキルと関係する専門資料を、現在の実装状況に従って使ってください。添付したカンプと本文から、情報のまとまり、見出し、list・table・引用、link・button・フォーム、画像の役割をsemantic blueprintとして整理し、その判断に沿ったHTML/CSSを作ってください。画像から分からない事実は推測と未解決事項を明記してください。標準の要求、推奨、プロジェクト慣習を区別してください。実際に行ったHTML・DOM・keyboard確認だけを証拠として報告し、未実施の検査はuntestedにしてください。

配布前のこの依頼文は設計ガイダンスの試行例であり、品質保証または対応エージェントの宣言ではない。

## 未確認と作業境界

- 競合のhost/version別導入、実際の生成品質、検出器精度、AT/browser/device動作は未確認。
- AI生成サイトの欠陥発生率や比較研究はこの調査で確認していない。故障分類を頻度の実証として使わない。
- 全競合の全ファイルを読んでいない。比較表の未確認セルを機能欠如と読み替えない。
- 本件のrule engine、JSON schema、runner、CI、installer、地域パックは、調査時のstatus文書に従い未実装または未検証。
- この担当の変更は本ファイルだけ。インストール、アプリ作成、公開、支払い、外部への私的データ送信、Git変更操作はしていない。
- desktop/SaaSの構想はこのスキル改善調査の成果・実装には含めていない。
