import React, { useState } from 'react';
import { Trophy, CheckCircle2, Circle, Lock } from 'lucide-react';

const RewardScreen: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'daily' | 'weekly' | 'badges' | 'stats'>('daily');

  return (
    <div className="min-h-screen bg-ios-gray pb-20">
      {/* iOS Status Bar Spacer */}
      <div className="h-11 bg-white"></div>

      {/* Header */}
      <header className="bg-white px-4 py-4 border-b border-ios-separator sticky top-0 z-10">
        <h1 className="text-xl font-semibold text-ios-text text-center">リワード</h1>
      </header>

      {/* Tabs */}
      <div className="bg-white border-b border-ios-separator sticky top-16 z-10">
        <div className="flex">
          <button
            onClick={() => setActiveTab('daily')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'daily'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            今日
          </button>
          <button
            onClick={() => setActiveTab('weekly')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'weekly'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            週間
          </button>
          <button
            onClick={() => setActiveTab('badges')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'badges'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            バッジ
          </button>
          <button
            onClick={() => setActiveTab('stats')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'stats'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            実績
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="px-4 pt-4 space-y-3">
        {/* Daily Challenges */}
        {activeTab === 'daily' && (
          <>
            <div className="ios-card p-4">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-base font-semibold text-ios-text">🎯 今日のチャレンジ</h2>
                <div className="flex items-center gap-2">
                  <div className="flex-1 bg-ios-gray rounded-full h-1.5 w-16 overflow-hidden">
                    <div className="bg-furdi-pink h-full rounded-full" style={{ width: '60%' }}></div>
                  </div>
                  <span className="text-xs font-medium text-ios-text-secondary">3/5</span>
                </div>
              </div>

              <div className="space-y-3">
                {/* Completed Task */}
                <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                  <div className="flex items-center gap-3">
                    <CheckCircle2 className="w-5 h-5 text-green-500 flex-shrink-0" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-ios-text">アプリを開く</p>
                      <p className="text-xs text-ios-text-secondary">報酬: デイリースタンプ 🎫</p>
                    </div>
                  </div>
                </div>

                {/* Completed Task */}
                <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                  <div className="flex items-center gap-3">
                    <CheckCircle2 className="w-5 h-5 text-green-500 flex-shrink-0" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-ios-text">体重を記録する</p>
                      <p className="text-xs text-ios-text-secondary">報酬: ヘルスバッジ 🏅</p>
                    </div>
                  </div>
                </div>

                {/* Completed Task */}
                <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                  <div className="flex items-center gap-3">
                    <CheckCircle2 className="w-5 h-5 text-green-500 flex-shrink-0" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-ios-text">混雑状況を確認する</p>
                      <p className="text-xs text-ios-text-secondary">報酬: スマートバッジ 🔍</p>
                    </div>
                  </div>
                </div>

                {/* Pending Task */}
                <div className="border border-ios-separator rounded-lg p-3">
                  <div className="flex items-center gap-3">
                    <Circle className="w-5 h-5 text-ios-text-secondary flex-shrink-0" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-ios-text">動画を1本視聴する</p>
                      <p className="text-xs text-ios-text-secondary">報酬: トレーナーバッジ 🎬</p>
                    </div>
                    <button className="px-3 py-1 bg-furdi-pink text-white text-xs font-semibold rounded-full active:scale-95 transition-transform">
                      視聴
                    </button>
                  </div>
                </div>

                {/* Pending Task */}
                <div className="border border-ios-separator rounded-lg p-3">
                  <div className="flex items-center gap-3">
                    <Circle className="w-5 h-5 text-ios-text-secondary flex-shrink-0" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-ios-text">来店する</p>
                      <p className="text-xs text-ios-text-secondary">報酬: フィットネスバッジ 💪</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Bonus */}
            <div className="bg-gradient-to-r from-furdi-pink to-furdi-pink-dark rounded-lg p-4 text-white">
              <p className="text-sm font-semibold mb-1">🎁 全達成ボーナス</p>
              <p className="text-xs opacity-90">5つすべて達成で特別バッジ獲得！</p>
            </div>
          </>
        )}

        {/* Weekly Challenges */}
        {activeTab === 'weekly' && (
          <>
            <div className="ios-card p-4">
              <h2 className="text-base font-semibold text-ios-text mb-3">📅 週間チャレンジ</h2>

              <div className="space-y-3">
                <div className="border border-ios-separator rounded-lg p-3">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-lg">🏃</span>
                    <p className="text-sm font-medium text-ios-text flex-1">週3回来店チャレンジ</p>
                  </div>
                  <div className="mb-2">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs text-ios-text-secondary">進捗</span>
                      <span className="text-xs font-medium text-ios-text">2/3 回</span>
                    </div>
                    <div className="progress-bar bg-ios-gray">
                      <div className="progress-bar-fill bg-furdi-pink" style={{ width: '67%' }}></div>
                    </div>
                  </div>
                  <p className="text-xs text-ios-text-secondary mb-2">報酬: ウィークリーチャンピオン 🏆</p>
                  <p className="text-xs text-orange-500">残り期間: あと3日</p>
                </div>

                <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-lg">🎬</span>
                    <p className="text-sm font-medium text-ios-text flex-1">動画3本視聴チャレンジ</p>
                    <CheckCircle2 className="w-5 h-5 text-green-500" />
                  </div>
                  <div className="mb-2">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs text-ios-text-secondary">進捗</span>
                      <span className="text-xs font-medium text-green-600">3/3 本 ✅</span>
                    </div>
                    <div className="progress-bar bg-green-200">
                      <div className="progress-bar-fill bg-green-500" style={{ width: '100%' }}></div>
                    </div>
                  </div>
                  <p className="text-xs text-ios-text-secondary mb-2">報酬: ビデオマスター 📺</p>
                  <button className="w-full bg-green-500 text-white rounded-full py-2 text-xs font-semibold active:scale-95 transition-transform">
                    報酬を受け取る
                  </button>
                </div>
              </div>
            </div>

            <div className="ios-card p-4">
              <h2 className="text-base font-semibold text-ios-text mb-3">📆 月間チャレンジ</h2>

              <div className="space-y-3">
                <div className="border border-ios-separator rounded-lg p-3">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-lg">💪</span>
                    <p className="text-sm font-medium text-ios-text flex-1">累計10時間トレーニング</p>
                  </div>
                  <div className="mb-2">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs text-ios-text-secondary">進捗</span>
                      <span className="text-xs font-medium text-ios-text">8.5/10 時間</span>
                    </div>
                    <div className="progress-bar bg-ios-gray">
                      <div className="progress-bar-fill bg-furdi-pink" style={{ width: '85%' }}></div>
                    </div>
                  </div>
                  <p className="text-xs text-ios-text-secondary mb-1">報酬: マンスリーアスリート 🥇</p>
                  <p className="text-xs text-furdi-pink">あと1.5時間で達成！</p>
                </div>
              </div>
            </div>
          </>
        )}

        {/* Badges */}
        {activeTab === 'badges' && (
          <>
            <div className="ios-card p-4">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-base font-semibold text-ios-text">🏅 マイバッジコレクション</h2>
                <span className="text-sm text-ios-text-secondary">15/50</span>
              </div>

              <div className="flex gap-2 mb-4">
                <button className="px-3 py-1 bg-furdi-pink text-white text-xs font-semibold rounded-full">
                  すべて
                </button>
                <button className="px-3 py-1 bg-ios-gray text-ios-text text-xs font-medium rounded-full">
                  獲得済み
                </button>
                <button className="px-3 py-1 bg-ios-gray text-ios-text text-xs font-medium rounded-full">
                  未獲得
                </button>
              </div>

              <div className="grid grid-cols-4 gap-3">
                {/* Earned Badges */}
                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center text-2xl shadow-md">
                    🏅
                  </div>
                  <span className="text-xs font-medium text-ios-text text-center">初来店</span>
                  <span className="text-[10px] text-ios-text-secondary">1/1</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-gradient-to-br from-red-500 to-orange-600 rounded-full flex items-center justify-center text-2xl shadow-md">
                    🔥
                  </div>
                  <span className="text-xs font-medium text-ios-text text-center">7連続</span>
                  <span className="text-[10px] text-ios-text-secondary">1/7</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-2xl shadow-md">
                    💪
                  </div>
                  <span className="text-xs font-medium text-ios-text text-center">10時間</span>
                  <span className="text-[10px] text-ios-text-secondary">1/14</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-gradient-to-br from-green-500 to-teal-600 rounded-full flex items-center justify-center text-2xl shadow-md">
                    📉
                  </div>
                  <span className="text-xs font-medium text-ios-text text-center">-1kg</span>
                  <span className="text-[10px] text-ios-text-secondary">1/20</span>
                </button>

                {/* Locked Badges */}
                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-ios-gray rounded-full flex items-center justify-center shadow-md">
                    <Lock className="w-6 h-6 text-ios-text-secondary" />
                  </div>
                  <span className="text-xs font-medium text-ios-text-secondary text-center">14連続</span>
                  <span className="text-[10px] text-ios-text-secondary">あと9日</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-ios-gray rounded-full flex items-center justify-center shadow-md">
                    <Lock className="w-6 h-6 text-ios-text-secondary" />
                  </div>
                  <span className="text-xs font-medium text-ios-text-secondary text-center">50時間</span>
                  <span className="text-[10px] text-ios-text-secondary">あと42h</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-ios-gray rounded-full flex items-center justify-center shadow-md">
                    <Lock className="w-6 h-6 text-ios-text-secondary" />
                  </div>
                  <span className="text-xs font-medium text-ios-text-secondary text-center">-3kg</span>
                  <span className="text-[10px] text-ios-text-secondary">あと2.6kg</span>
                </button>

                <button className="flex flex-col items-center gap-1 p-2 rounded-lg active:bg-ios-gray transition-colors">
                  <div className="w-14 h-14 bg-gradient-to-br from-gray-400 to-gray-600 rounded-full flex items-center justify-center text-2xl shadow-md">
                    ？
                  </div>
                  <span className="text-xs font-medium text-ios-text-secondary text-center">???</span>
                  <span className="text-[10px] text-ios-text-secondary">シークレット</span>
                </button>
              </div>
            </div>
          </>
        )}

        {/* Stats */}
        {activeTab === 'stats' && (
          <>
            <div className="ios-card p-4">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-16 h-16 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center">
                  <Trophy className="w-8 h-8 text-white" />
                </div>
                <div className="flex-1">
                  <p className="text-xs text-ios-text-secondary">現在のランク</p>
                  <p className="text-xl font-bold text-ios-text">シルバー</p>
                </div>
              </div>
              <div className="mb-2">
                <div className="flex items-center justify-between mb-1">
                  <span className="text-xs text-ios-text-secondary">次のランクまで</span>
                  <span className="text-xs font-medium text-ios-text">60/100 pt</span>
                </div>
                <div className="progress-bar bg-ios-gray">
                  <div className="progress-bar-fill bg-gradient-to-r from-yellow-400 to-orange-500" style={{ width: '60%' }}></div>
                </div>
              </div>
              <p className="text-xs text-furdi-pink">あと40ptでゴールドランク！</p>
            </div>

            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">📈 累計データ</h3>
              <div className="grid grid-cols-2 gap-3">
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">総来店回数</p>
                  <p className="text-2xl font-bold text-ios-text">52<span className="text-sm font-normal">回</span></p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">総トレーニング</p>
                  <p className="text-2xl font-bold text-ios-text">78<span className="text-sm font-normal">時間</span></p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">総カロリー</p>
                  <p className="text-2xl font-bold text-ios-text">12.5<span className="text-sm font-normal">k</span></p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">会員歴</p>
                  <p className="text-2xl font-bold text-ios-text">3<span className="text-sm font-normal">ヶ月</span></p>
                </div>
              </div>
            </div>

            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">🎯 目標達成状況</h3>
              <div className="space-y-3">
                <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">体重変化</p>
                  <p className="text-sm text-ios-text mb-1">開始時: <span className="font-semibold">58.0 kg</span> → 現在: <span className="font-semibold">54.2 kg</span></p>
                  <p className="text-lg font-bold text-green-600">-3.8 kg 達成！ 🎉</p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">来店頻度</p>
                  <p className="text-sm text-ios-text mb-1">週平均: <span className="font-semibold">3.2回</span></p>
                  <p className="text-sm text-green-600">✅ 目標: 週3回 達成中</p>
                </div>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default RewardScreen;
