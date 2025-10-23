import React, { useState } from 'react';
import { ChevronLeft, Info, Download } from 'lucide-react';

interface DNAResultScreenProps {
  onBack?: () => void;
}

const DNAResultScreen: React.FC<DNAResultScreenProps> = ({ onBack }) => {
  const [activeTab, setActiveTab] = useState('overall');

  const tabs = [
    { id: 'overall', label: '総合' },
    { id: 'muscle', label: '筋肉' },
    { id: 'metabolism', label: '代謝' },
    { id: 'risk', label: 'リスク' },
    { id: 'detail', label: '詳細' },
  ];

  // Radar chart data (percentage out of 100)
  const radarData = [
    { label: '筋力', value: 70 },
    { label: '持久力', value: 85 },
    { label: '代謝', value: 75 },
    { label: '回復', value: 80 },
    { label: '柔軟性', value: 65 },
    { label: '総合', value: 75 },
  ];

  // Convert radar data to polygon points
  const getRadarPolygonPoints = () => {
    const center = { x: 100, y: 100 };
    const maxRadius = 80;
    const angleStep = (Math.PI * 2) / radarData.length;

    return radarData
      .map((item, index) => {
        const angle = angleStep * index - Math.PI / 2;
        const radius = (item.value / 100) * maxRadius;
        const x = center.x + radius * Math.cos(angle);
        const y = center.y + radius * Math.sin(angle);
        return `${x},${y}`;
      })
      .join(' ');
  };

  return (
    <div className="bg-ios-gray min-h-screen">
      {/* Status Bar */}
      <div className="h-11 bg-white flex items-center justify-between px-5">
        <span className="text-sm">9:41</span>
      </div>

      {/* Header */}
      <div className="h-15 bg-white flex items-center px-4 border-b border-ios-separator">
        <button onClick={onBack} className="p-1 -ml-1">
          <ChevronLeft className="w-5 h-5 text-gray-600" />
        </button>
        <h1 className="flex-1 text-center text-lg font-semibold text-ios-text -ml-5">
          DNA検査結果
        </h1>
      </div>

      {/* Test Info Card */}
      <div className="mx-4 mt-4 mb-4 p-4 rounded-xl bg-blue-50 border border-blue-200 relative overflow-hidden">
        <div className="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-blue-200 bg-opacity-40 rounded-full flex items-center justify-center">
          <span className="text-2xl">🧬</span>
        </div>
        <p className="text-xs text-gray-700 mb-1">検査日: 2024年8月15日</p>
        <p className="text-sm font-semibold text-blue-600">検査機関: GeneQuest</p>
      </div>

      {/* Tabs */}
      <div className="bg-white border-b border-ios-separator">
        <div className="flex px-4 py-2">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-3 py-2 text-sm relative ${
                activeTab === tab.id
                  ? 'text-blue-500 font-semibold'
                  : 'text-gray-500'
              }`}
            >
              {tab.label}
              {activeTab === tab.id && (
                <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-blue-500"></div>
              )}
            </button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="px-4 pb-20">
        {activeTab === 'overall' && (
          <>
            {/* Radar Chart Card */}
            <div className="bg-white rounded-xl p-4 mt-4 border border-ios-separator">
              <h3 className="text-sm font-semibold text-ios-text mb-4">体質スコア</h3>

              <div className="flex justify-center">
                <svg width="200" height="200" viewBox="0 0 200 200" className="overflow-visible">
                  {/* Background circles */}
                  <circle cx="100" cy="100" r="80" fill="none" stroke="#f5f5f5" strokeWidth="1" />
                  <circle cx="100" cy="100" r="60" fill="none" stroke="#f5f5f5" strokeWidth="1" />
                  <circle cx="100" cy="100" r="40" fill="none" stroke="#f5f5f5" strokeWidth="1" />
                  <circle cx="100" cy="100" r="20" fill="none" stroke="#f5f5f5" strokeWidth="1" />

                  {/* Axes */}
                  {radarData.map((_, index) => {
                    const angle = ((Math.PI * 2) / radarData.length) * index - Math.PI / 2;
                    const x = 100 + 80 * Math.cos(angle);
                    const y = 100 + 80 * Math.sin(angle);
                    return (
                      <line
                        key={index}
                        x1="100"
                        y1="100"
                        x2={x}
                        y2={y}
                        stroke="#e5e5e7"
                        strokeWidth="1"
                      />
                    );
                  })}

                  {/* Data polygon */}
                  <polygon
                    points={getRadarPolygonPoints()}
                    fill="#2196F3"
                    fillOpacity="0.3"
                    stroke="#2196F3"
                    strokeWidth="2"
                  />

                  {/* Labels */}
                  {radarData.map((item, index) => {
                    const angle = ((Math.PI * 2) / radarData.length) * index - Math.PI / 2;
                    const x = 100 + 95 * Math.cos(angle);
                    const y = 100 + 95 * Math.sin(angle);
                    return (
                      <text
                        key={index}
                        x={x}
                        y={y}
                        textAnchor="middle"
                        dominantBaseline="middle"
                        className="text-[10px] fill-gray-600"
                      >
                        {item.label}
                      </text>
                    );
                  })}
                </svg>
              </div>
            </div>

            {/* Body Type Card */}
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 mt-4">
              <div className="flex items-start gap-3">
                <div className="w-10 h-10 bg-blue-200 bg-opacity-50 rounded-full flex items-center justify-center flex-shrink-0">
                  <span className="text-xl">💪</span>
                </div>
                <div className="flex-1">
                  <p className="text-xs text-gray-600 mb-1">あなたの体質タイプ</p>
                  <h3 className="text-base font-bold text-blue-600 mb-1">持久力優位型</h3>
                  <p className="text-xs text-gray-600">遺伝的に長時間の運動に向いています</p>
                </div>
                <div className="text-2xl text-blue-500">
                  ★★★★☆
                </div>
              </div>
            </div>

            {/* Gene Cards */}
            <div className="grid grid-cols-2 gap-3 mt-4">
              <div className="bg-white rounded-lg p-3 border border-ios-separator">
                <h4 className="text-xs font-semibold text-ios-text mb-0.5">ACTN3遺伝子</h4>
                <p className="text-[9px] text-gray-500 mb-2">(筋肉タイプ)</p>
                <div className="inline-block px-3 py-1 bg-green-50 rounded-full mb-2">
                  <span className="text-xs font-semibold text-green-600">XX型</span>
                </div>
                <p className="text-[10px] text-gray-600">持久力に優れる</p>
              </div>

              <div className="bg-white rounded-lg p-3 border border-ios-separator">
                <h4 className="text-xs font-semibold text-ios-text mb-0.5">ACE遺伝子</h4>
                <p className="text-[9px] text-gray-500 mb-2">(持久力)</p>
                <div className="inline-block px-3 py-1 bg-blue-50 rounded-full mb-2">
                  <span className="text-xs font-semibold text-blue-600">II型</span>
                </div>
                <p className="text-[10px] text-gray-600">持久力が高い</p>
              </div>
            </div>

            {/* Recommendation Card */}
            <div className="bg-orange-50 rounded-xl p-4 mt-4 mb-4">
              <div className="flex items-start gap-2 mb-2">
                <Info className="w-4 h-4 text-orange-500 flex-shrink-0 mt-0.5" />
                <h3 className="text-xs font-semibold text-orange-600">あなたにおすすめ</h3>
              </div>
              <ul className="space-y-1.5">
                <li className="text-xs text-gray-700 flex items-start">
                  <span className="mr-1.5">•</span>
                  <span>有酸素運動を中心に</span>
                </li>
                <li className="text-xs text-gray-700 flex items-start">
                  <span className="mr-1.5">•</span>
                  <span>長時間の低〜中強度トレーニング</span>
                </li>
                <li className="text-xs text-gray-700 flex items-start">
                  <span className="mr-1.5">•</span>
                  <span>マラソン・サイクリング・水泳</span>
                </li>
              </ul>
            </div>
          </>
        )}

        {activeTab === 'muscle' && (
          <div className="mt-4">
            <div className="bg-white rounded-xl p-4 border border-ios-separator">
              <h3 className="text-sm font-semibold mb-3">筋肉タイプ分析</h3>

              <div className="space-y-4">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs text-gray-600">速筋繊維</span>
                    <span className="text-xs font-semibold">30%</span>
                  </div>
                  <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full bg-orange-500 rounded-full" style={{ width: '30%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs text-gray-600">遅筋繊維</span>
                    <span className="text-xs font-semibold">70%</span>
                  </div>
                  <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div className="h-full bg-blue-500 rounded-full" style={{ width: '70%' }}></div>
                  </div>
                </div>
              </div>

              <div className="mt-4 p-3 bg-blue-50 rounded-lg">
                <p className="text-xs text-gray-700">
                  遅筋繊維が多いため、長時間の有酸素運動に適しています。
                  瞬発的なパワーよりも、持続的な運動能力に優れています。
                </p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'metabolism' && (
          <div className="mt-4 space-y-3">
            <div className="bg-white rounded-lg p-4 border border-ios-separator">
              <h4 className="text-sm font-semibold mb-3">基礎代謝</h4>
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs text-gray-600">遺伝的傾向</span>
                <span className="text-sm font-semibold">標準</span>
              </div>
              <div className="text-2xl font-bold text-ios-text mb-1">1,350 kcal</div>
              <p className="text-xs text-gray-500">1日の推定基礎代謝</p>
            </div>

            <div className="grid grid-cols-3 gap-2">
              <div className="bg-white rounded-lg p-3 border border-ios-separator text-center">
                <div className="text-lg mb-1">🍚</div>
                <p className="text-[10px] text-gray-600 mb-1">糖質代謝</p>
                <p className="text-xs font-semibold">標準</p>
              </div>
              <div className="bg-white rounded-lg p-3 border border-ios-separator text-center">
                <div className="text-lg mb-1">🥑</div>
                <p className="text-[10px] text-gray-600 mb-1">脂質代謝</p>
                <p className="text-xs font-semibold">やや低</p>
              </div>
              <div className="bg-white rounded-lg p-3 border border-ios-separator text-center">
                <div className="text-lg mb-1">🥩</div>
                <p className="text-[10px] text-gray-600 mb-1">タンパク質</p>
                <p className="text-xs font-semibold">高い</p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'risk' && (
          <div className="mt-4">
            <div className="bg-yellow-50 border border-yellow-200 rounded-xl p-4">
              <h3 className="text-sm font-semibold text-gray-800 mb-3">怪我リスク評価</h3>

              <div className="mb-4">
                <div className="flex items-center gap-2 mb-2">
                  <div className="w-3 h-3 bg-yellow-500 rounded-full"></div>
                  <span className="text-sm font-semibold">総合リスク: 中程度</span>
                </div>
              </div>

              <div className="space-y-3">
                <div className="bg-white rounded-lg p-3">
                  <h4 className="text-xs font-semibold mb-1">関節・腱</h4>
                  <p className="text-[10px] text-gray-600 mb-1">COL1A1遺伝子: GT型</p>
                  <p className="text-xs text-orange-600">リスク: やや高い</p>
                </div>

                <div className="bg-white rounded-lg p-3">
                  <h4 className="text-xs font-semibold mb-1">柔軟性</h4>
                  <p className="text-[10px] text-gray-600 mb-1">COL5A1遺伝子: CC型</p>
                  <p className="text-xs text-green-600">リスク: 標準</p>
                </div>
              </div>

              <div className="mt-4 p-3 bg-orange-50 rounded-lg">
                <h4 className="text-xs font-semibold text-orange-700 mb-2">予防策</h4>
                <ul className="space-y-1">
                  <li className="text-xs text-gray-700">• ウォームアップを十分に</li>
                  <li className="text-xs text-gray-700">• ストレッチを重点的に</li>
                  <li className="text-xs text-gray-700">• 急な負荷増加を避ける</li>
                </ul>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'detail' && (
          <div className="mt-4">
            <div className="bg-white rounded-xl p-4 border border-ios-separator mb-4">
              <h3 className="text-sm font-semibold mb-3">全21項目の検査結果</h3>

              <div className="space-y-3">
                <div>
                  <h4 className="text-xs font-semibold text-gray-600 mb-2">筋肉・運動能力</h4>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-xs">ACTN3 - 筋肉タイプ</span>
                      <span className="text-sm">★★★★☆</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-xs">ACE - 持久力</span>
                      <span className="text-sm">★★★★★</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-xs">PPARGC1A - 運動効果</span>
                      <span className="text-sm">★★★☆☆</span>
                    </div>
                  </div>
                </div>

                <div className="border-t border-gray-100 pt-3">
                  <h4 className="text-xs font-semibold text-gray-600 mb-2">代謝</h4>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-xs">FTO - 肥満傾向</span>
                      <span className="text-sm">★★★☆☆</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-xs">PPARG - 脂肪燃焼</span>
                      <span className="text-sm">★★★★☆</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <button className="w-full bg-blue-500 text-white py-3 rounded-full font-semibold flex items-center justify-center gap-2">
              <Download className="w-5 h-5" />
              詳細PDFをダウンロード
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default DNAResultScreen;
