## 概要
Web APIによる書籍貸し出しサンプルアプリです．
最小限の実装のため，セキュリティをはじめ本番運用は考慮していません．


## 使用方法
1. リポジトリをクローン
2. [docker-compose.yml](docker-compose.yml)の管理者名・パスワードを編集する：
``` yaml
environment:
      - BM_ADMIN_NAME=admin
      - BM_ADMIN_PASSWORD=password
```
3. `docker-compose up`

## URL仕様
- `/` : ブラウザ向けインターフェース（アプリ）
- `/api/` : Web API エンドポイント
- `/swagger-ui/` : API仕様書


## システムの構成要素
### サーバサイド
- Python Flask，Flask-Restful ほか
- SQLite
- Nginx（リバースプロキシ）

### クライアントサイド
- Vue.js 2

## License

[MIT](https://github.com/mrcdr/book_manager/blob/master/LICENSE)
