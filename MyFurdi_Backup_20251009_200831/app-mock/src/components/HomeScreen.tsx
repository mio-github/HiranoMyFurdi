import React from 'react';
import { Bell, ChevronRight, Flame, Target, MapPin, Activity, TrendingDown, Video, FileText, HelpCircle, Dna } from 'lucide-react';

const HomeScreen: React.FC = () => {
  const currentHour = new Date().getHours();
  const greeting = currentHour < 12 ? 'おはようございます' : currentHour < 18 ? 'こんにちは' : 'こんばんは';

  return (
    <div className="min-h-screen bg-ios-gray pb-20">
      {/* iOS Status Bar Spacer */}
      <div className="h-11 bg-white"></div>

      {/* Header */}
      <header className="bg-white px-4 py-4 border-b border-ios-separator sticky top-0 z-10">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold text-ios-text">
            {greeting}、さくらさん！
          </h1>
          <button className="relative p-2">
            <Bell className="w-6 h-6 text-ios-text" />
            <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
          </button>
        </div>
      </header>

      {/* Content */}
      <div className="px-4 pt-4 space-y-3">
        {/* Today's Challenge Card */}
        <div className="ios-card p-4">
          <div className="flex items-center gap-2 mb-3">
            <Target className="w-5 h-5 text-furdi-pink" />
            <h2 className="text-base font-semibold text-ios-text">今日のチャレンジ</h2>
          </div>

          <div className="bg-furdi-pink-light rounded-lg p-4 mb-3">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-ios-text">体重を記録する</span>
              <span className="text-xs text-furdi-pink font-medium">報酬: デイリーバッジ 🏅</span>
            </div>
            <button className="w-full bg-furdi-pink text-white rounded-full py-2.5 font-semibold text-sm active:scale-95 transition-transform">
              1タップで記録する
            </button>
          </div>

          <div className="flex items-center gap-2 text-xs text-ios-text-secondary">
            <div className="flex-1 bg-ios-gray rounded-full h-1.5 overflow-hidden">
              <div className="bg-furdi-pink h-full rounded-full" style={{ width: '60%' }}></div>
            </div>
            <span className="font-medium">3/5 達成</span>
          </div>
        </div>

        {/* Visit Summary Card */}
        <div className="ios-card p-4">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <Flame className="w-5 h-5 text-orange-500" />
              <span className="text-2xl font-bold text-ios-text">5日連続来店中！</span>
            </div>
          </div>

          <div className="space-y-3">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-sm text-ios-text-secondary">今週の来店</span>
                <span className="text-sm font-semibold text-ios-text">3/4回</span>
              </div>
              <div className="progress-bar bg-ios-gray">
                <div className="progress-bar-fill bg-furdi-pink" style={{ width: '75%' }}></div>
              </div>
              <p className="text-xs text-furdi-pink font-medium mt-1">あと1回で目標達成です！</p>
            </div>

            <div className="grid grid-cols-2 gap-3 pt-2 border-t border-ios-separator">
              <div>
                <p className="text-xs text-ios-text-secondary">前回来店</p>
                <p className="text-sm font-medium text-ios-text">昨日 18:30</p>
              </div>
              <div>
                <p className="text-xs text-ios-text-secondary">次回おすすめ</p>
                <p className="text-sm font-medium text-furdi-pink">明日 18:00頃</p>
              </div>
            </div>
          </div>
        </div>

        {/* Congestion Quick View */}
        <div className="ios-card p-4">
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-2">
                <MapPin className="w-4 h-4 text-ios-text-secondary" />
                <span className="text-sm text-ios-text-secondary">渋谷店（お気に入り）</span>
              </div>
              <div className="flex items-center gap-2 mb-1">
                <div className="w-3 h-3 bg-green-500 rounded-full"></div>
                <span className="text-lg font-semibold text-ios-text">かなり空いています</span>
              </div>
              <p className="text-xs text-ios-text-secondary">現在の利用率: 25%</p>
            </div>
            <ChevronRight className="w-5 h-5 text-ios-text-secondary" />
          </div>

          <div className="flex gap-2 mt-3">
            <button className="flex-1 bg-furdi-pink text-white rounded-full py-2 text-sm font-semibold active:scale-95 transition-transform">
              詳しく見る
            </button>
            <button className="flex-1 bg-white border-2 border-furdi-pink text-furdi-pink rounded-full py-2 text-sm font-semibold active:scale-95 transition-transform">
              今から行く
            </button>
          </div>
        </div>

        {/* Health Data Summary - Tabs */}
        <div className="ios-card overflow-hidden">
          <div className="flex border-b border-ios-separator">
            <button className="flex-1 py-3 text-sm font-semibold text-furdi-pink border-b-2 border-furdi-pink">
              体重
            </button>
            <button className="flex-1 py-3 text-sm font-medium text-ios-text-secondary">
              体脂肪
            </button>
            <button className="flex-1 py-3 text-sm font-medium text-ios-text-secondary">
              歩数
            </button>
          </div>

          <div className="p-4">
            <div className="flex items-end justify-between mb-3">
              <div>
                <p className="text-3xl font-bold text-ios-text">54.2 <span className="text-lg font-normal text-ios-text-secondary">kg</span></p>
                <div className="flex items-center gap-1 mt-1">
                  <TrendingDown className="w-4 h-4 text-green-500" />
                  <span className="text-sm font-medium text-green-500">-0.3kg</span>
                  <span className="text-xs text-ios-text-secondary">（前回比）</span>
                </div>
              </div>
              <div className="text-right">
                <div className="flex items-center gap-1 text-2xl">
                  {['▂', '▃', '▅', '▃', '▄', '▅', '▆'].map((bar, i) => (
                    <span key={i} className="text-furdi-pink">{bar}</span>
                  ))}
                </div>
                <p className="text-xs text-ios-text-secondary mt-1">7日間</p>
              </div>
            </div>

            <p className="text-sm text-green-500 font-medium mb-3">順調に減っています✨</p>

            <button className="w-full bg-furdi-pink text-white rounded-full py-2.5 text-sm font-semibold active:scale-95 transition-transform">
              記録する
            </button>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="ios-card p-4">
          <h3 className="text-sm font-semibold text-ios-text mb-3">クイックアクション</h3>
          <div className="grid grid-cols-3 gap-3">
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <Video className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">動画</span>
            </button>
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <FileText className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">記録</span>
            </button>
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <Activity className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">データ</span>
            </button>
          </div>
          <div className="grid grid-cols-3 gap-3 mt-2">
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <Bell className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">お知らせ</span>
            </button>
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <HelpCircle className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">FAQ</span>
            </button>
            <button className="flex flex-col items-center gap-2 p-3 rounded-lg active:bg-ios-gray transition-colors">
              <div className="w-12 h-12 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <Dna className="w-6 h-6 text-furdi-pink" />
              </div>
              <span className="text-xs font-medium text-ios-text">遺伝子</span>
            </button>
          </div>
        </div>

        {/* Weekly Summary - Collapsible */}
        <div className="ios-card p-4">
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-sm font-semibold text-ios-text">📈 今週の成果</h3>
            <ChevronRight className="w-5 h-5 text-ios-text-secondary" />
          </div>
          <div className="grid grid-cols-3 gap-3">
            <div>
              <p className="text-xs text-ios-text-secondary">時間</p>
              <p className="text-lg font-semibold text-ios-text">120分</p>
              <p className="text-xs text-green-500">+20分 ⬆️</p>
            </div>
            <div>
              <p className="text-xs text-ios-text-secondary">カロリー</p>
              <p className="text-lg font-semibold text-ios-text">850 kcal</p>
            </div>
            <div>
              <p className="text-xs text-ios-text-secondary">来店</p>
              <p className="text-lg font-semibold text-ios-text">3回</p>
            </div>
          </div>
        </div>

        {/* Notice Banner */}
        <div className="bg-gradient-to-r from-furdi-pink to-furdi-pink-dark rounded-lg p-4 text-white">
          <p className="text-xs font-medium opacity-90">重要なお知らせ</p>
          <p className="text-sm font-semibold mt-1">新しいトレーニング動画が追加されました！</p>
        </div>
      </div>
    </div>
  );
};

export default HomeScreen;
