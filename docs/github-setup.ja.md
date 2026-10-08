# GitHub公開の手動手順

この文書は手順書です。ここに書いたコマンドは実行していません（リポジトリは別途 `gh repo create nyattoh/semantic-web-skill --public --source . --remote origin` で作成・接続済みで、未pushです。節4はこの場合 `--push` を省き、`git push -u origin main` に読み替えます）。GitHubの所有者候補は `nyattoh`、リポジトリ名候補は `semantic-web-skill`、公開範囲は `public` です。名前の空きは未確認です。

## 1. 展開と前提確認

ZIPの最上位は `semantic-web-skill` です。Windowsで `D:\develop\works` に展開すると `D:\develop\works\semantic-web-skill` になります。既存フォルダーがあれば上書きせず、別の退避先へ展開して比較してください。

以下はPowerShellで一段ずつ実行し、結果を確認する例です。自動実行用スクリプトではありません。GitとGitHub CLIが利用でき、GitHubへ認証済みであることを前提とします。未導入・未認証ならここで止め、公式案内に従って本人が設定してください。認証情報をファイルへ書き込まないでください。

```powershell
Set-Location 'D:\develop\works\semantic-web-skill'
git --version
gh --version
gh auth status --hostname github.com
gh api --hostname github.com user --jq .login
```

ログイン名が厳密に `nyattoh` であることを確認します。異なるアカウント、認証エラー、権限不足、接続エラーの場合は進めません。トークンを表示・コピーするコマンドは不要です。

```powershell
gh repo view nyattoh/semantic-web-skill --json nameWithOwner,visibility,url
```

既存リポジトリが見つかったら停止してください。既存先へのpushや内容の置換はこの手順の対象外です。コマンド失敗だけで「名前が空いている」と判断しないでください。認証と通信が正常な状態で、本人のGitHub新規作成画面でも同名が利用可能か確認します。この時点ではブラウザで作成せず、確認だけにします。不明なら停止します。

## 2. 公開内容とライセンスを確認

publicではファイルとコミット情報が一般公開されます。仕様を含む全ファイルの公開可否を確認してください。[LICENSE](../LICENSE)（MIT）と[LICENSE-DOCS.txt](../LICENSE-DOCS.txt)（CC BY 4.0）の適用範囲を確認します。旧プロンプト `web_spec.original.md` は権利未確認のため公開せず、`.gitignore` で除外しています。

Gitのコミット名・メールも公開対象です。既存設定を確認し、必要なら本人がGitHubの非公開メール設定などを選びます。この手順ではグローバル設定を変更しません。

```powershell
git config --get user.name
git config --get user.email
```

## 3. ローカルの新規mainを作る

すでに `.git` がある、または親ディレクトリのGit管理下なら、既存の履歴へ混ぜず停止してください。エクスプローラーで隠しファイルも確認します。以下の確認で `git rev-parse` が既存リポジトリのパスを表示した場合も停止します。新規フォルダーでは「not a git repository」が想定されます。

```powershell
Test-Path .git
git rev-parse --show-toplevel
```

`.git` がなく親もGit管理外であると確認してから続けます。

```powershell
git init -b main
git status --short --untracked-files=all
git add --all
git diff --cached --name-status
git diff --cached --stat
git diff --cached --check
git diff --cached
```

ステージ済みの一覧と全文を読み、秘密情報、個人情報、不要な成果物がないことを確認します。.gitignoreは秘密情報検査の代わりにはなりません。`git diff --cached --check` に問題があれば修正して再確認します。公開するファイルが確定してからコミットします。

```powershell
git commit -m "docs: add semantic-web skill documentation starter"
git status --short
git branch --show-current
git log -1 --format=fuller
```

作業ツリーがクリーンで、ブランチが `main`、コミット情報が公開してよい内容であることを確認します。

## 4. 新規公開リポジトリ作成とpush

この次のコマンドが外部公開を行います。本人アカウント、名前の空き、公開内容、public設定、ライセンス状態に納得している場合だけ実行します。

```powershell
gh repo create nyattoh/semantic-web-skill --public --source=. --remote=origin --push
```

名前の衝突や権限エラーが出たら停止します。リポジトリ作成だけ成功してpushが失敗する場合もあるため、同じ作成コマンドを繰り返さず、次節で実在する状態を確認してください。強制push、既存originの上書き、削除によるやり直しはしません。

## 5. 成功確認

```powershell
gh repo view nyattoh/semantic-web-skill --json nameWithOwner,visibility,url,defaultBranchRef
git remote -v
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

所有者と名前が `nyattoh/semantic-web-skill`、可視性が `PUBLIC`、既定ブランチが `main` であることを確認します。originの所有者・名前が意図したものと一致し、ローカルHEADとリモートmainのコミットIDが一致することを確認します。CLIが返したURLを開き、READMEと仕様書が読めることも確認してください。

不一致や空の結果があれば、完了とは扱いません。確認できた状態とエラーを保存して原因を調べます。検証していないスキルを動作済み・公開準備完了と書かないでください。

## コマンドの一次資料

2026年10月8日UTCにコマンド仕様を参照。実機での実行確認は未実施です。

- [GitHub CLI: gh repo create](https://cli.github.com/manual/gh_repo_create)
- [GitHub CLI: gh repo view](https://cli.github.com/manual/gh_repo_view)
- [GitHub CLI: gh auth status](https://cli.github.com/manual/gh_auth_status)
- [Git: git init](https://git-scm.com/docs/git-init)
