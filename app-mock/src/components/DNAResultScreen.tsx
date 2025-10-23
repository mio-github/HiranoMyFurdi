import React, { useState } from 'react';
import { ChevronLeft, Download, ExternalLink, AlertCircle } from 'lucide-react';

interface DNAResultScreenProps {
  onBack?: () => void;
}

const DNAResultScreen: React.FC<DNAResultScreenProps> = ({ onBack }) => {
  const [showToast, setShowToast] = useState(false);

  const handleLineConsultation = () => {
    setShowToast(true);
    setTimeout(() => setShowToast(false), 3000);
    // In real app, this would open LINE app
    window.open('https://line.me/R/', '_blank');
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
          遺伝子テスト結果
        </h1>
      </div>

      {/* Content */}
      <div className="px-4 pb-20">
        {/* Test Info Card */}
        <div className="mt-4 p-4 rounded-xl bg-blue-50 border border-blue-200 relative overflow-hidden">
          <div className="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-blue-200 bg-opacity-40 rounded-full flex items-center justify-center">
            <span className="text-2xl">🧬</span>
          </div>
          <p className="text-xs text-gray-700 mb-1">検査日: 2024年8月15日</p>
          <p className="text-sm font-semibold text-blue-600">検査機関: GeneQuest</p>
        </div>

        {/* PDF Viewer Section - Gene Test Results */}
        <div className="mt-4 bg-white rounded-xl border border-ios-separator overflow-hidden">
          <div className="p-4 border-b border-ios-separator">
            <h3 className="text-sm font-semibold text-ios-text mb-1">遺伝子検査結果レポート</h3>
            <p className="text-xs text-gray-500">21項目の詳細な検査結果</p>
          </div>

          {/* PDF Preview */}
          <div className="bg-gray-50 p-8 min-h-[300px] flex flex-col items-center justify-center">
            <div className="w-full max-w-sm bg-white rounded-lg shadow-md p-6 border-2 border-gray-200">
              <div className="text-center mb-4">
                <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-3xl">📄</span>
                </div>
                <h4 className="text-sm font-semibold mb-2">遺伝子検査結果レポート</h4>
                <p className="text-xs text-gray-600">全21ページ (2.4MB)</p>
              </div>

              {/* Simulated PDF Content Preview */}
              <div className="border-t border-gray-200 pt-3 space-y-2">
                <div className="flex justify-between text-xs">
                  <span className="text-gray-600">筋肉タイプ</span>
                  <span className="font-semibold">持久力優位型</span>
                </div>
                <div className="flex justify-between text-xs">
                  <span className="text-gray-600">代謝傾向</span>
                  <span className="font-semibold">標準</span>
                </div>
                <div className="flex justify-between text-xs">
                  <span className="text-gray-600">怪我リスク</span>
                  <span className="font-semibold text-orange-600">やや高</span>
                </div>
              </div>
            </div>

            <div className="mt-4 flex gap-2">
              <button className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-full text-sm font-semibold hover:bg-blue-600 transition-colors">
                <Download className="w-4 h-4" />
                ダウンロード
              </button>
              <button className="flex items-center gap-2 px-4 py-2 bg-white border-2 border-blue-500 text-blue-500 rounded-full text-sm font-semibold hover:bg-blue-50 transition-colors">
                <ExternalLink className="w-4 h-4" />
                全画面で開く
              </button>
            </div>
          </div>
        </div>

        {/* PDF Viewer Section - Training Menu */}
        <div className="mt-4 bg-white rounded-xl border border-ios-separator overflow-hidden">
          <div className="p-4 border-b border-ios-separator">
            <h3 className="text-sm font-semibold text-ios-text mb-1">おすすめトレーニングメニュー</h3>
            <p className="text-xs text-gray-500">あなたの遺伝子型に最適化されたプラン</p>
          </div>

          {/* PDF Preview */}
          <div className="bg-gray-50 p-8 min-h-[300px] flex flex-col items-center justify-center">
            <div className="w-full max-w-sm bg-white rounded-lg shadow-md p-6 border-2 border-gray-200">
              <div className="text-center mb-4">
                <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-3xl">💪</span>
                </div>
                <h4 className="text-sm font-semibold mb-2">パーソナライズドメニュー</h4>
                <p className="text-xs text-gray-600">12週間プログラム (1.8MB)</p>
              </div>

              {/* Simulated Training Menu Preview */}
              <div className="border-t border-gray-200 pt-3 space-y-2">
                <div className="text-xs">
                  <div className="font-semibold mb-1">推奨トレーニング</div>
                  <ul className="space-y-1 text-gray-600">
                    <li>• 有酸素運動中心</li>
                    <li>• 長時間低～中強度</li>
                    <li>• ストレッチ重視</li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="mt-4 flex gap-2">
              <button className="flex items-center gap-2 px-4 py-2 bg-green-500 text-white rounded-full text-sm font-semibold hover:bg-green-600 transition-colors">
                <Download className="w-4 h-4" />
                ダウンロード
              </button>
              <button className="flex items-center gap-2 px-4 py-2 bg-white border-2 border-green-500 text-green-500 rounded-full text-sm font-semibold hover:bg-green-50 transition-colors">
                <ExternalLink className="w-4 h-4" />
                全画面で開く
              </button>
            </div>
          </div>
        </div>

        {/* LINE Consultation Button */}
        <div className="mt-6">
          <button
            onClick={handleLineConsultation}
            className="w-full bg-[#00B900] text-white py-4 rounded-xl font-semibold flex items-center justify-center gap-3 shadow-lg hover:bg-[#00A000] transition-colors active:scale-98"
          >
            <svg className="w-6 h-6" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63h2.386c.346 0 .627.285.627.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.495.254l2.462 3.33V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63.346 0 .628.285.628.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.348 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.282.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314"/>
            </svg>
            <span>LINEで専門家に相談する</span>
          </button>

          {/* Info Text */}
          <div className="mt-3 flex items-start gap-2 px-4">
            <AlertCircle className="w-4 h-4 text-gray-400 flex-shrink-0 mt-0.5" />
            <p className="text-xs text-gray-500">
              遺伝子結果について専門家にご相談いただけます。LINEアプリが開きます。
            </p>
          </div>
        </div>

        {/* Additional Info Card */}
        <div className="mt-6 mb-4 bg-orange-50 border border-orange-200 rounded-xl p-4">
          <h4 className="text-xs font-semibold text-orange-700 mb-2 flex items-center gap-1">
            <span>💡</span>
            結果の見方
          </h4>
          <ul className="space-y-1.5 text-xs text-gray-700">
            <li>• PDFには21項目の詳細な遺伝子情報が含まれています</li>
            <li>• おすすめメニューはあなた専用にカスタマイズされています</li>
            <li>• わからないことがあればLINEでお気軽にご相談ください</li>
          </ul>
        </div>
      </div>

      {/* iOS Toast Message */}
      {showToast && (
        <div className="fixed inset-x-0 top-20 px-4 z-50 animate-fadeIn">
          <div className="bg-gray-900 bg-opacity-90 text-white text-sm px-4 py-3 rounded-xl shadow-lg max-w-sm mx-auto text-center">
            LINEアプリに移動します。アプリに戻るには再度開いてください。
          </div>
        </div>
      )}
    </div>
  );
};

export default DNAResultScreen;
