(function () {
  'use strict';
  const $ = id => document.getElementById(id);

  /* ===== STEP 1 ===== */
  const POSTS = [
    { who: '@haru_2026・3分前', t: '今日から沖縄！　家族全員で1週間の旅行〜✈️　留守番は誰もいませ〜ん', bad: true,
      why: '<strong>留守を知らせてしまっています。</strong>空き巣などの被害につながる可能性があります。旅行の投稿は帰ってからにしましょう。' },
    { who: '@kaede_info・12分前', t: '文化祭の準備、みんなでがんばりました！　＃文化祭　＃うちの高校', bad: false,
      why: '特に問題はありません。ただし、写真に他の人が写っている場合は<strong>本人の許可</strong>を取りましょう。' },
    { who: '@sora_pic・20分前', t: '推しのアニメキャラをアイコンにしてみた！　かわいい〜', bad: true,
      why: '<strong>著作権の侵害</strong>にあたります。アニメのキャラクター画像を許可なくプロフィール画像に使うことはできません。' },
    { who: '@ren_news・35分前', t: '【拡散希望】○○地方で大きな地震が来るらしい！　友だちから回ってきた情報です', bad: true,
      why: '<strong>出所の分からない情報を拡散しています。</strong>「友だちから回ってきた」は根拠になりません。デマの拡散は大きな混乱を招きます。' },
    { who: '@mio_stage・1時間前', t: 'コンサートで撮った○○さんの写真、勝手にグッズにして売ってます！', bad: true,
      why: '<strong>肖像権・パブリシティ権の侵害</strong>にあたります。また会場での撮影自体が禁止されていることも多いです。' }
  ];
  let pAns = {};
  function drawPosts() {
    $('postBox').innerHTML = POSTS.map((p, i) =>
      '<div class="post' + (pAns[i] ? (p.bad ? ' ng' : ' ok') : '') + '" data-i="' + i + '">' +
      '<div class="who">' + p.who + '</div><div class="t">' + p.t + '</div></div>').join('');
    $('postBox').querySelectorAll('.post').forEach(el => el.addEventListener('click', () => {
      const i = +el.dataset.i; pAns[i] = true; drawPosts();
      const n = $('postNote');
      n.className = 'note ' + (POSTS[i].bad ? 'ng' : 'ok');
      const c = Object.keys(pAns).length;
      n.innerHTML = (POSTS[i].bad ? '<strong>問題があります。</strong>' : '<strong>大きな問題はありません。</strong>') + POSTS[i].why +
        '<br>' + c + ' / ' + POSTS.length + ' 件を確認' +
        (c === POSTS.length ? '<br>5件のうち<strong>4件に問題</strong>がありました。投稿する前に「誰が見るか」「何が分かってしまうか」を考える習慣をつけましょう。' : '');
    }));
    $('postNote').className = 'note info';
    $('postNote').textContent = '投稿をクリックして確かめましょう。';
  }

  /* ===== STEP 3 ===== */
  const TASTE = ['スポーツ', '音楽', '料理', 'ゲーム'];
  let taste = null;
  const FEED = {
    'スポーツ': ['サッカー日本代表の速報', '高校野球ハイライト', '走るのが速くなる方法', 'スポーツ用品セール情報', 'バスケの名場面まとめ'],
    '音楽': ['新曲リリース情報', 'ライブ映像まとめ', 'ギター初心者講座', '人気アーティストの対談', '音楽フェス最新情報'],
    '料理': ['5分でできる朝ごはん', '人気のパスタレシピ', '包丁の研ぎ方', 'コンビニ食材アレンジ', '調理器具レビュー'],
    'ゲーム': ['新作ゲーム紹介', '攻略のコツ10選', 'eスポーツ大会結果', 'ゲーム実況ランキング', '次世代機のうわさ']
  };
  const MIX = ['地域の防災情報', '選挙の争点まとめ', '別の分野のニュース', '海外の文化紹介', '科学の新発見'];
  function drawFeed() {
    $('tasteBtns').innerHTML = TASTE.map(t =>
      '<button class="btn' + (taste === t ? ' primary' : '') + '" data-t="' + t + '">' + t + 'をよく見る</button>').join('') +
      '<button class="btn" data-t="reset">リセット</button>';
    $('tasteBtns').querySelectorAll('button').forEach(b => b.addEventListener('click', () => {
      taste = b.dataset.t === 'reset' ? null : b.dataset.t; drawFeed();
    }));
    const items = taste ? FEED[taste].map(t => ({ t: t, same: true })) : MIX.map(t => ({ t: t, same: false }));
    $('feedBox').innerHTML = items.map(i => '<div class="it' + (i.same ? ' same' : '') + '">' + i.t + '</div>').join('');
    const n = $('feedNote');
    n.className = 'note ' + (taste ? 'ng' : 'info');
    n.innerHTML = taste
      ? '<strong>' + taste + '</strong>の話題ばかりになりました。便利な反面、<strong>ほかの分野の情報が目に入らなくなります</strong>。' +
        'これを<strong>フィルターバブル</strong>といいます。自分と違う意見に触れにくくなることにも注意が必要です。'
      : '履歴がない状態では、いろいろな分野の情報が表示されています。ボタンを押してみましょう。';
  }

  function init() {
    drawPosts(); drawFeed();
    Quiz.judge('jBox', 'jNote', [
      { k: '⓪', t: '相手からのメッセージにはどんなときでも早く返信しなければいけない。', ok: false,
        why: 'すぐに返す義務はありません。急かされること自体がストレスや<strong>トラブルの原因</strong>になります。' },
      { k: '①', t: '信頼関係のある相手とSNSやメールでやり取りする際も、悪意を持った者がなりすましている可能性を頭に入れておくべきである。', ok: true,
        why: 'アカウントの乗っ取りによる<strong>なりすまし</strong>は実際に起きています。お金や個人情報の話が出たら、別の手段で本人に確認しましょう。' },
      { k: '②', t: 'Webページに匿名で投稿した場合は、本人が特定されることはない。', ok: false,
        why: '通信記録から<strong>発信者を特定できます</strong>（発信者情報開示制度）。匿名でも責任は生じます。' },
      { k: '③', t: 'SNSの非公開グループでは、どんなグループであっても、個人情報を書き込んでも問題はない。', ok: false,
        why: '非公開でも、<strong>メンバーがスクリーンショットを外部に出す</strong>ことがあります。' },
      { k: '④', t: '一般によく知られているアニメのキャラクターの画像をSNSのプロフィール画像に許可なく掲載することは、著作権の侵害に当たる。', ok: true,
        why: '有名かどうかは関係ありません。<strong>著作権の侵害</strong>にあたります。' },
      { k: '⑤', t: '芸能人は多くの人に知られていることから肖像権の対象外となるため、芸能人の写真をSNSに掲載してもよい。', ok: false,
        why: '芸能人にも<strong>肖像権</strong>があり、さらに<strong>パブリシティ権</strong>もあります。' }
    ], '適当なのは <strong>①と④</strong> の2つなので、本文の答えは【ア】・【イ】＝<strong>①・④</strong>（順不同）です。');
    Quiz.choice('q2Box', 'q2Note', [
      { k: 'ウ', q: 'インターネット上の情報の信ぴょう性を確かめる方法として最も適当なものは',
        ch: ['検索エンジンの検索結果で、上位に表示されているかどうかで判断する', 'Q&Aサイトの回答は、多くの人に支持されているベストアンサーに選ばれているかどうかで判断する', 'SNSに投稿された情報は、共有や「いいね」の数が多いかどうかで判断する', '特定のWebサイトだけでなく、書籍や複数のWebサイトなどを確認し、比較・検証してから判断する'],
        a: 3, why: '検索順位・ベストアンサー・いいね数は、いずれも<strong>正しさの証明にはなりません</strong>。複数の情報源で確かめるのが基本です。' }
    ], '本文の答えは【ウ】③ です。');
    Quiz.choice('q3Box', 'q3Note', [
      { k: 'エ', q: 'インターネット上のサービスの利用に関する記述として<strong>適切でない</strong>ものは',
        ch: ['SNSなどで見知らぬ人とやりとりを行う際には、公開されているプロフィールやアイコン画像を確認することで、相手が信用できるかどうかを判断するとよい', 'SNSへの不適切な投稿により炎上が起こってしまった場合、その投稿を速やかに削除したとしても、生涯にわたって深刻な影響を受ける可能性がある', 'インターネット上の情報は、自分自身の検索履歴やSNSの閲覧履歴などに基づいて表示されており、偏った情報だけになってしまう可能性がある', '企業がインフルエンサーや芸能人などの影響力のある人に、広告であることを消費者に隠して自社の商品やサービスを宣伝してもらう行為は、法律により制限されている', '自宅周辺で自分を撮った写真をSNSに投稿する場合、瞳に映り込んだ意図しない情報がないかを確認するとよい'],
        a: 0, why: 'プロフィールやアイコンは<strong>いくらでも偽装できます</strong>。信用の判断材料にはなりません。①はデジタルタトゥー、②はフィルターバブル（STEP 3）、③はステルスマーケティング規制、④は個人情報の特定の話で、いずれも正しい記述です。' }
    ], '本文の答えは【エ】⓪ です。');
    window.Terms.glossary($('glossBox'), ['情報モラル', 'なりすまし', 'フィルターバブル', 'デジタルタトゥー', '肖像権', 'パブリシティ権', '著作権', 'ファクトチェック']);
    Worksheet.make('wsBox', {
      name: 'info-morals',
      fields: [
        { id: 'r1', label: '① 起きて困ること', hint: '実際に起こりうる具体的な場面。', rows: 3,
          ph: '例：部活の写真に写り込んだ人が、知らないうちにSNSに載る' },
        { id: 'r2', label: '② だれが困るか', hint: '本人・家族・学校・写り込んだ人。', rows: 2, ph: '例：写り込んだ後輩と、その保護者' },
        { id: 'r3', label: '③ ルール案', hint: '「〜しない」より「〜する」の形にすると守りやすい。', rows: 3,
          ph: '例：人が写っている写真は、写っている全員に見せてから投稿する' },
        { id: 'r4', label: '④ 例外と、そのときの手順', hint: '例外を決めておくと形骸化しにくい。', rows: 2,
          ph: '例：大会の集合写真は顧問の確認を取れば可' },
        { id: 'r5', label: '⑤ 守られているかの確かめ方', hint: '見直す時期も決める。', rows: 2, ph: '例：学期末にアンケートで確認し、必要なら書きかえる' }
      ],
      build: function (v, e) {
        return '<h4>利用ルールシート</h4><dl>' +
          '<dt>① 起きて困ること</dt><dd>' + e(v.r1) + '</dd>' +
          '<dt>② 困る人</dt><dd>' + e(v.r2) + '</dd>' +
          '<dt>③ ルール案</dt><dd>' + e(v.r3) + '</dd>' +
          '<dt>④ 例外と手順</dt><dd>' + e(v.r4) + '</dd>' +
          '<dt>⑤ 確かめ方・見直し</dt><dd>' + e(v.r5) + '</dd></dl>';
      },
      note: '守れないルールは、ないのと同じです。④と⑤があるかどうかで実効性が変わります。'
    });

    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
