import React, { useState } from 'react';
import { Calendar, TrendingDown, Activity } from 'lucide-react';

const ReportScreen: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'exercise' | 'body' | 'visit'>('exercise');

  return (
    <div className="min-h-screen bg-ios-gray pb-20">
      {/* iOS Status Bar Spacer */}
      <div className="h-11 bg-white"></div>

      {/* Header */}
      <header className="bg-white px-4 py-4 border-b border-ios-separator sticky top-0 z-10">
        <h1 className="text-xl font-semibold text-ios-text text-center">レポート</h1>
      </header>

      {/* Tabs */}
      <div className="bg-white border-b border-ios-separator sticky top-16 z-10">
        <div className="flex">
          <button
            onClick={() => setActiveTab('exercise')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'exercise'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            運動記録
          </button>
          <button
            onClick={() => setActiveTab('body')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'body'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            体組成
          </button>
          <button
            onClick={() => setActiveTab('visit')}
            className={`flex-1 py-3 text-sm font-semibold transition-colors ${
              activeTab === 'visit'
                ? 'text-furdi-pink border-b-2 border-furdi-pink'
                : 'text-ios-text-secondary'
            }`}
          >
            来館履歴
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="px-4 pt-4 space-y-3">
        {/* Period Filter */}
        <div className="flex gap-2">
          <button className="px-3 py-1.5 bg-furdi-pink text-white text-xs font-semibold rounded-full">
            週
          </button>
          <button className="px-3 py-1.5 bg-white border border-ios-separator text-ios-text text-xs font-medium rounded-full">
            月
          </button>
          <button className="px-3 py-1.5 bg-white border border-ios-separator text-ios-text text-xs font-medium rounded-full">
            年
          </button>
        </div>

        {activeTab === 'exercise' && (
          <>
            {/* Chart */}
            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">トレーニング時間（週）</h3>
              <div className="h-48 flex items-end justify-between gap-2">
                {[30, 45, 20, 50, 35, 40, 25].map((height, i) => (
                  <div key={i} className="flex-1 flex flex-col items-center gap-1">
                    <div
                      className="w-full bg-furdi-pink rounded-t"
                      style={{ height: `${height}%` }}
                    ></div>
                    <span className="text-[10px] text-ios-text-secondary">
                      {['月', '火', '水', '木', '金', '土', '日'][i]}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Summary */}
            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">今週のサマリー</h3>
              <div className="grid grid-cols-2 gap-3">
                <div className="bg-ios-gray rounded-lg p-3">
                  <div className="flex items-center gap-2 mb-1">
                    <Activity className="w-4 h-4 text-furdi-pink" />
                    <p className="text-xs text-ios-text-secondary">総時間</p>
                  </div>
                  <p className="text-2xl font-bold text-ios-text">245<span className="text-sm">分</span></p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <div className="flex items-center gap-2 mb-1">
                    <Activity className="w-4 h-4 text-furdi-pink" />
                    <p className="text-xs text-ios-text-secondary">消費カロリー</p>
                  </div>
                  <p className="text-2xl font-bold text-ios-text">1,250<span className="text-sm">kcal</span></p>
                </div>
              </div>
            </div>

            {/* Exercise List */}
            <div className="ios-card divide-y divide-ios-separator">
              {[
                { date: '今日 18:30', type: 'AIマシン', duration: '45分', intensity: '中' },
                { date: '昨日 19:00', type: '動画トレーニング', duration: '30分', intensity: '低' },
                { date: '一昨日 18:00', type: 'AIマシン', duration: '50分', intensity: '高' },
              ].map((item, i) => (
                <div key={i} className="p-4">
                  <div className="flex items-center justify-between mb-1">
                    <p className="text-sm font-medium text-ios-text">{item.type}</p>
                    <span className="text-xs text-ios-text-secondary">{item.date}</span>
                  </div>
                  <div className="flex items-center gap-3 text-xs text-ios-text-secondary">
                    <span>⏱ {item.duration}</span>
                    <span>💪 {item.intensity}</span>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}

        {activeTab === 'body' && (
          <>
            {/* Weight Chart */}
            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">体重推移（週）</h3>
              <div className="h-48 relative">
                <svg className="w-full h-full" viewBox="0 0 300 150">
                  <polyline
                    points="0,80 50,70 100,65 150,60 200,55 250,52 300,50"
                    fill="none"
                    stroke="#FF69B4"
                    strokeWidth="3"
                  />
                  {[0, 50, 100, 150, 200, 250, 300].map((x, i) => (
                    <circle key={i} cx={x} cy={[80, 70, 65, 60, 55, 52, 50][i]} r="4" fill="#FF69B4" />
                  ))}
                </svg>
                <div className="absolute bottom-0 left-0 right-0 flex justify-between px-1">
                  {['月', '火', '水', '木', '金', '土', '日'].map((day, i) => (
                    <span key={i} className="text-[10px] text-ios-text-secondary">{day}</span>
                  ))}
                </div>
              </div>
            </div>

            {/* Current Stats */}
            <div className="ios-card p-4">
              <div className="flex items-center justify-between mb-4">
                <div>
                  <p className="text-xs text-ios-text-secondary">現在の体重</p>
                  <p className="text-3xl font-bold text-ios-text">54.2<span className="text-lg">kg</span></p>
                </div>
                <div className="flex items-center gap-1 text-green-500">
                  <TrendingDown className="w-5 h-5" />
                  <span className="text-lg font-semibold">-0.3kg</span>
                </div>
              </div>
              <div className="grid grid-cols-3 gap-3">
                <div className="text-center">
                  <p className="text-xs text-ios-text-secondary">BMI</p>
                  <p className="text-lg font-semibold text-ios-text">21.2</p>
                </div>
                <div className="text-center">
                  <p className="text-xs text-ios-text-secondary">体脂肪率</p>
                  <p className="text-lg font-semibold text-ios-text">24.5%</p>
                </div>
                <div className="text-center">
                  <p className="text-xs text-ios-text-secondary">筋肉量</p>
                  <p className="text-lg font-semibold text-ios-text">38.2kg</p>
                </div>
              </div>
            </div>
          </>
        )}

        {activeTab === 'visit' && (
          <>
            {/* Calendar View */}
            <div className="ios-card p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-sm font-semibold text-ios-text">2024年1月</h3>
                <Calendar className="w-5 h-5 text-ios-text-secondary" />
              </div>
              <div className="grid grid-cols-7 gap-1">
                {['日', '月', '火', '水', '木', '金', '土'].map((day) => (
                  <div key={day} className="text-center text-xs text-ios-text-secondary py-1">
                    {day}
                  </div>
                ))}
                {Array.from({ length: 31 }, (_, i) => i + 1).map((day) => {
                  const isVisited = [1, 3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29].includes(day);
                  return (
                    <div
                      key={day}
                      className={`aspect-square flex items-center justify-center text-sm rounded-lg ${
                        isVisited
                          ? 'bg-furdi-pink text-white font-semibold'
                          : 'text-ios-text'
                      }`}
                    >
                      {day}
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Visit Stats */}
            <div className="ios-card p-4">
              <h3 className="text-sm font-semibold text-ios-text mb-3">来館統計</h3>
              <div className="grid grid-cols-2 gap-3">
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">今月の来館</p>
                  <p className="text-2xl font-bold text-ios-text">13<span className="text-sm">回</span></p>
                </div>
                <div className="bg-ios-gray rounded-lg p-3">
                  <p className="text-xs text-ios-text-secondary mb-1">週平均</p>
                  <p className="text-2xl font-bold text-ios-text">3.2<span className="text-sm">回</span></p>
                </div>
              </div>
            </div>

            {/* Visit History */}
            <div className="ios-card divide-y divide-ios-separator">
              <div className="px-4 py-3">
                <h3 className="text-sm font-semibold text-ios-text">最近の来館履歴</h3>
              </div>
              {[
                { date: '今日', time: '18:30 - 19:45', duration: '1時間15分', store: '渋谷店' },
                { date: '昨日', time: '19:00 - 20:00', duration: '1時間', store: '渋谷店' },
                { date: '1/27', time: '18:00 - 19:20', duration: '1時間20分', store: '渋谷店' },
              ].map((item, i) => (
                <div key={i} className="p-4">
                  <div className="flex items-center justify-between mb-1">
                    <p className="text-sm font-medium text-ios-text">{item.date}</p>
                    <span className="text-xs text-ios-text-secondary">{item.store}</span>
                  </div>
                  <div className="flex items-center gap-3 text-xs text-ios-text-secondary">
                    <span>🕐 {item.time}</span>
                    <span>⏱ {item.duration}</span>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default ReportScreen;
