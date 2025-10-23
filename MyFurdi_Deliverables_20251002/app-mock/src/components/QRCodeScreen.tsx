import React from 'react';
import { ChevronDown, Info } from 'lucide-react';

const QRCodeScreen: React.FC = () => {
  return (
    <div className="min-h-screen bg-white flex flex-col">
      {/* iOS Status Bar Spacer */}
      <div className="h-11 bg-white"></div>

      {/* Header */}
      <header className="px-4 py-4 border-b border-ios-separator">
        <h1 className="text-xl font-semibold text-ios-text text-center">入館証</h1>
      </header>

      {/* Content */}
      <div className="flex-1 flex flex-col items-center justify-center px-6 pb-24">
        {/* QR Code */}
        <div className="bg-white p-6 rounded-2xl shadow-lg mb-6">
          <div className="w-64 h-64 bg-white border-4 border-ios-gray rounded-xl flex items-center justify-center">
            {/* QR Code placeholder - in real app, this would be actual QR */}
            <svg viewBox="0 0 200 200" className="w-full h-full">
              <rect width="200" height="200" fill="white"/>
              {/* QR Code pattern simulation */}
              <g fill="black">
                <rect x="10" y="10" width="60" height="60"/>
                <rect x="130" y="10" width="60" height="60"/>
                <rect x="10" y="130" width="60" height="60"/>
                <rect x="30" y="30" width="20" height="20" fill="white"/>
                <rect x="150" y="30" width="20" height="20" fill="white"/>
                <rect x="30" y="150" width="20" height="20" fill="white"/>
                {/* Random pattern */}
                <rect x="80" y="20" width="10" height="10"/>
                <rect x="100" y="20" width="10" height="10"/>
                <rect x="80" y="40" width="10" height="10"/>
                <rect x="110" y="40" width="10" height="10"/>
                <rect x="90" y="60" width="10" height="10"/>
                <rect x="80" y="80" width="10" height="10"/>
                <rect x="110" y="80" width="10" height="10"/>
                <rect x="80" y="100" width="10" height="10"/>
                <rect x="100" y="100" width="10" height="10"/>
                <rect x="130" y="80" width="10" height="10"/>
                <rect x="150" y="90" width="10" height="10"/>
                <rect x="170" y="100" width="10" height="10"/>
                <rect x="20" y="80" width="10" height="10"/>
                <rect x="40" y="90" width="10" height="10"/>
                <rect x="50" y="110" width="10" height="10"/>
                <rect x="80" y="130" width="10" height="10"/>
                <rect x="100" y="140" width="10" height="10"/>
                <rect x="120" y="150" width="10" height="10"/>
                <rect x="140" y="160" width="10" height="10"/>
                <rect x="160" y="170" width="10" height="10"/>
                <rect x="130" y="130" width="10" height="10"/>
                <rect x="150" y="140" width="10" height="10"/>
                <rect x="170" y="150" width="10" height="10"/>
              </g>
            </svg>
          </div>
        </div>

        {/* User Info */}
        <div className="w-full max-w-sm space-y-2 mb-6">
          <div className="flex justify-between items-center p-3 bg-ios-gray rounded-lg">
            <span className="text-sm text-ios-text-secondary">会員ID</span>
            <span className="text-sm font-semibold text-ios-text">FUR-2024-0123</span>
          </div>
          <div className="flex justify-between items-center p-3 bg-ios-gray rounded-lg">
            <span className="text-sm text-ios-text-secondary">お名前</span>
            <span className="text-sm font-semibold text-ios-text">さくら様</span>
          </div>
          <div className="flex justify-between items-center p-3 bg-ios-gray rounded-lg">
            <span className="text-sm text-ios-text-secondary">有効期限</span>
            <span className="text-sm font-semibold text-ios-text">2025年12月31日</span>
          </div>
        </div>

        {/* Store Selection */}
        <button className="w-full max-w-sm ios-card p-4 mb-4 active:scale-95 transition-transform">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-furdi-pink-light rounded-full flex items-center justify-center">
                <span className="text-lg">🏪</span>
              </div>
              <div className="text-left">
                <p className="text-xs text-ios-text-secondary">利用店舗</p>
                <p className="text-sm font-semibold text-ios-text">渋谷店</p>
              </div>
            </div>
            <ChevronDown className="w-5 h-5 text-ios-text-secondary" />
          </div>
        </button>

        {/* Usage Instructions */}
        <button className="w-full max-w-sm flex items-center justify-center gap-2 text-furdi-pink text-sm font-medium py-3">
          <Info className="w-4 h-4" />
          <span>入館方法を見る</span>
        </button>

        {/* Auto-update notice */}
        <div className="mt-6 text-center">
          <p className="text-xs text-ios-text-secondary">QRコードは30秒ごとに自動更新されます</p>
          <div className="flex items-center justify-center gap-1 mt-2">
            <div className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-xs text-green-500">有効</span>
          </div>
        </div>
      </div>

      {/* Tips */}
      <div className="px-6 pb-6">
        <div className="bg-furdi-pink-light rounded-lg p-4">
          <p className="text-xs font-semibold text-furdi-pink mb-1">💡 初めての方へ</p>
          <p className="text-xs text-ios-text">
            入館時にこのQRコードをリーダーにかざしてください。店内のマシンでも同じQRコードが使えます。
          </p>
        </div>
      </div>
    </div>
  );
};

export default QRCodeScreen;
