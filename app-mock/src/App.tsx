import React, { useState } from 'react';
import HomeScreen from './components/HomeScreen';
import ReportScreen from './components/ReportScreen';
import QRCodeScreen from './components/QRCodeScreen';
import RewardScreen from './components/RewardScreen';
import MenuScreen from './components/MenuScreen';
import DNAResultScreen from './components/DNAResultScreen';
import TabBar from './components/TabBar';

function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [currentScreen, setCurrentScreen] = useState<string | null>(null);

  // iPhone frame styles - fixed height to match iPhone 14 Pro
  const iPhoneFrameStyle = {
    width: '393px',
    height: '852px',
    margin: '0 auto',
    position: 'relative' as const,
    boxShadow: '0 0 0 12px #1d1d1f, 0 0 0 13px #2d2d2d, 0 20px 60px rgba(0,0,0,0.5)',
    borderRadius: '40px',
    overflow: 'hidden',
    background: '#000',
  };

  const handleNavigate = (screen: string) => {
    setCurrentScreen(screen);
  };

  const handleBack = () => {
    setCurrentScreen(null);
  };

  const renderScreen = () => {
    // Show DNA screen if navigated to it
    if (currentScreen === 'dna') {
      return <DNAResultScreen onBack={handleBack} />;
    }

    // Show tab screens
    switch (activeTab) {
      case 'home':
        return <HomeScreen />;
      case 'report':
        return <ReportScreen />;
      case 'qrcode':
        return <QRCodeScreen />;
      case 'reward':
        return <RewardScreen />;
      case 'menu':
        return <MenuScreen onNavigate={handleNavigate} />;
      default:
        return <HomeScreen />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div style={iPhoneFrameStyle}>
        {/* Notch */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-40 h-7 bg-black rounded-b-3xl z-50"></div>

        {/* Screen Content */}
        <div className="relative bg-white h-full flex flex-col">
          <div className="flex-1 overflow-y-auto pb-[60px]">
            {renderScreen()}
          </div>
          <TabBar activeTab={activeTab} onTabChange={setActiveTab} />
        </div>
      </div>

      {/* Instructions */}
      <div className="max-w-md mx-auto mt-8 px-4">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-lg font-bold text-gray-800 mb-2">MyFurdi モックアプリ</h2>
          <p className="text-sm text-gray-600 mb-4">
            iOSネイティブアプリの見た目を再現したモックアプリです。
          </p>
          <ul className="text-xs text-gray-500 space-y-1">
            <li>• 下部のタブバーで画面を切り替えられます</li>
            <li>• すべての画面がFURDIブランド（ピンク基調）でデザインされています</li>
            <li>• iOS HIG準拠のネイティブな見た目を実現</li>
            <li>• レスポンシブデザイン（iPhone 14 Pro サイズ: 393px）</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
