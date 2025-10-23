import React from 'react';
import { Home, BarChart3, CreditCard, Trophy, Menu } from 'lucide-react';

interface TabBarProps {
  activeTab: string;
  onTabChange: (tab: string) => void;
}

const TabBar: React.FC<TabBarProps> = ({ activeTab, onTabChange }) => {
  const tabs = [
    { id: 'home', label: 'ホーム', icon: Home },
    { id: 'report', label: 'レポート', icon: BarChart3 },
    { id: 'qrcode', label: '入館証', icon: CreditCard },
    { id: 'reward', label: 'リワード', icon: Trophy },
    { id: 'menu', label: 'メニュー', icon: Menu },
  ];

  return (
    <div className="ios-tab-bar">
      <div className="flex items-center justify-around h-full">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;

          return (
            <button
              key={tab.id}
              onClick={() => onTabChange(tab.id)}
              className={`flex flex-col items-center justify-center gap-0.5 flex-1 h-full transition-all duration-200 active:scale-95`}
            >
              <Icon
                className={`w-[22px] h-[22px] transition-all duration-200 ${
                  isActive ? 'text-furdi-pink' : 'text-gray-400'
                }`}
                strokeWidth={isActive ? 2.5 : 2}
              />
              <span
                className={`text-[9px] mt-0.5 transition-all duration-200 ${
                  isActive ? 'text-furdi-pink font-semibold' : 'text-gray-400'
                }`}
              >
                {tab.label}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};

export default TabBar;
