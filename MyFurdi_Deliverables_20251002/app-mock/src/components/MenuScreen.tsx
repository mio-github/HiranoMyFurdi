import React from 'react';
import { User, BookOpen, Video, Bell, Settings, HelpCircle, FileText, Lock, LogOut, ChevronRight, Dna } from 'lucide-react';

interface MenuScreenProps {
  onNavigate?: (screen: string) => void;
}

const MenuScreen: React.FC<MenuScreenProps> = ({ onNavigate }) => {
  const menuSections = [
    {
      title: 'ユーザー情報',
      items: [
        { icon: User, label: 'プロフィール編集', badge: null },
      ],
    },
    {
      title: '利用ガイド',
      items: [
        { icon: BookOpen, label: 'はじめての方へ', badge: null },
        { icon: Video, label: 'アプリの使い方', badge: null },
        { icon: FileText, label: 'AIマシンの使い方', badge: null },
        { icon: FileText, label: '測定機器の使い方', badge: null },
      ],
    },
    {
      title: 'コンテンツ',
      items: [
        { icon: Video, label: '動画トレーニング一覧', badge: null },
        { icon: Bell, label: 'お知らせ一覧', badge: '3' },
        { icon: HelpCircle, label: 'FAQ・よくある質問', badge: null },
        { icon: FileText, label: 'コラム・読み物', badge: null },
      ],
    },
    {
      title: 'データ・連携',
      items: [
        { icon: Dna, label: '遺伝子テスト結果を見る', badge: 'NEW' },
        { icon: Settings, label: 'データ連携設定', badge: null },
      ],
    },
    {
      title: '設定',
      items: [
        { icon: Settings, label: 'アプリ設定', badge: null },
        { icon: Bell, label: '通知設定', badge: null },
      ],
    },
    {
      title: '契約・サポート',
      items: [
        { icon: FileText, label: '契約内容確認', badge: null },
        { icon: HelpCircle, label: 'お問い合わせ', badge: null },
        { icon: Lock, label: '利用規約', badge: null },
        { icon: Lock, label: 'プライバシーポリシー', badge: null },
      ],
    },
  ];

  return (
    <div className="min-h-screen bg-ios-gray pb-20">
      {/* iOS Status Bar Spacer */}
      <div className="h-11 bg-white"></div>

      {/* Header */}
      <header className="bg-white px-4 py-4 border-b border-ios-separator">
        <h1 className="text-xl font-semibold text-ios-text text-center">メニュー</h1>
      </header>

      {/* User Profile Card */}
      <div className="bg-gradient-to-br from-furdi-pink to-furdi-pink-dark p-4 m-4 rounded-2xl text-white">
        <div className="flex items-center gap-4 mb-4">
          <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center">
            <User className="w-8 h-8 text-furdi-pink" />
          </div>
          <div className="flex-1">
            <p className="text-lg font-semibold">さくら様</p>
            <p className="text-sm opacity-90">会員ID: FUR-2024-0123</p>
          </div>
        </div>
        <div className="grid grid-cols-3 gap-2">
          <div className="bg-white bg-opacity-20 rounded-lg p-2 text-center">
            <p className="text-xs opacity-90">会員歴</p>
            <p className="text-lg font-semibold">3ヶ月</p>
          </div>
          <div className="bg-white bg-opacity-20 rounded-lg p-2 text-center">
            <p className="text-xs opacity-90">来店回数</p>
            <p className="text-lg font-semibold">52回</p>
          </div>
          <div className="bg-white bg-opacity-20 rounded-lg p-2 text-center">
            <p className="text-xs opacity-90">バッジ</p>
            <p className="text-lg font-semibold">15個</p>
          </div>
        </div>
      </div>

      {/* Menu Sections */}
      <div className="px-4 space-y-4">
        {menuSections.map((section, sectionIndex) => (
          <div key={sectionIndex} className="ios-card overflow-hidden">
            <div className="px-4 py-2 bg-ios-gray border-b border-ios-separator">
              <p className="text-xs font-semibold text-ios-text-secondary uppercase">{section.title}</p>
            </div>
            <div className="divide-y divide-ios-separator">
              {section.items.map((item, itemIndex) => {
                const Icon = item.icon;
                const handleClick = () => {
                  if (item.label === '遺伝子テスト結果を見る' && onNavigate) {
                    onNavigate('dna');
                  }
                };
                return (
                  <button
                    key={itemIndex}
                    onClick={handleClick}
                    className="w-full flex items-center gap-3 p-4 active:bg-ios-gray transition-colors"
                  >
                    <div className="w-8 h-8 bg-furdi-pink-light rounded-lg flex items-center justify-center flex-shrink-0">
                      <Icon className="w-5 h-5 text-furdi-pink" />
                    </div>
                    <span className="flex-1 text-left text-sm text-ios-text">{item.label}</span>
                    {item.badge && (
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-semibold ${
                        item.badge === 'NEW'
                          ? 'bg-furdi-pink text-white'
                          : 'bg-red-500 text-white'
                      }`}>
                        {item.badge}
                      </span>
                    )}
                    <ChevronRight className="w-5 h-5 text-ios-text-secondary" />
                  </button>
                );
              })}
            </div>
          </div>
        ))}

        {/* Logout Button */}
        <div className="ios-card overflow-hidden">
          <button className="w-full flex items-center justify-center gap-2 p-4 text-red-500 active:bg-ios-gray transition-colors">
            <LogOut className="w-5 h-5" />
            <span className="text-sm font-semibold">ログアウト</span>
          </button>
        </div>

        {/* App Version */}
        <div className="text-center py-4">
          <p className="text-xs text-ios-text-secondary">MyFurdi v1.0.0</p>
          <p className="text-[10px] text-ios-text-secondary mt-1">© 2024 FURDI. All rights reserved.</p>
        </div>
      </div>
    </div>
  );
};

export default MenuScreen;
