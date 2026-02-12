
import React, { useState, useEffect } from 'react';
import { Bell, Search, User } from 'lucide-react';
import Sidebar from './components/Sidebar';
import Dashboard from './components/Dashboard';
import TransactionList from './components/TransactionList';
import ExplainableAI from './components/ExplainableAI';
import UPIVerification from './components/UPIVerification';
import { AppTab } from './types';

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<AppTab>('dashboard');
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard': return <Dashboard />;
      case 'transactions': return <TransactionList />;
      case 'xai': return <ExplainableAI />;
      case 'verification': return <UPIVerification />;
      case 'settings': return (
        <div className="p-12 text-center text-slate-400">
          <h2 className="text-3xl font-bold text-slate-800 dark:text-white mb-4">Settings</h2>
          <p>Security preferences and account configurations are coming soon.</p>
        </div>
      );
      default: return <Dashboard />;
    }
  };

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-900 transition-colors duration-300">
      <Sidebar 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        isDark={isDark} 
        toggleTheme={() => setIsDark(!isDark)} 
      />

      <main className="flex-1 flex flex-col h-screen overflow-hidden">
        {/* Header */}
        <header className="h-20 bg-white/80 dark:bg-slate-800/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-700 px-8 flex items-center justify-between z-10">
          <div className="flex items-center space-x-2 text-slate-400">
            <span className="text-sm font-medium">Pages</span>
            <span className="text-slate-300 dark:text-slate-600">/</span>
            <span className="text-sm font-semibold text-slate-800 dark:text-white capitalize">{activeTab}</span>
          </div>

          <div className="flex items-center space-x-6">
            <div className="hidden md:flex relative items-center">
              <Search className="absolute left-3 text-slate-400" size={16} />
              <input 
                type="text" 
                placeholder="Search..." 
                className="pl-10 pr-4 py-2 bg-slate-100 dark:bg-slate-700/50 rounded-xl border-none text-sm focus:ring-2 focus:ring-indigo-500 outline-none dark:text-white"
              />
            </div>
            
            <div className="flex items-center space-x-4">
              <button className="relative p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-xl transition-colors">
                <Bell size={20} />
                <span className="absolute top-2 right-2 w-2 h-2 bg-rose-500 rounded-full border-2 border-white dark:border-slate-800" />
              </button>
              
              <div className="h-8 w-px bg-slate-200 dark:bg-slate-700" />
              
              <button className="flex items-center space-x-3 p-1 pr-3 rounded-full hover:bg-slate-100 dark:hover:bg-slate-700 transition-all">
                <div className="w-8 h-8 rounded-full bg-indigo-100 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-600 dark:text-indigo-400">
                  <User size={18} />
                </div>
                <div className="hidden sm:block text-left">
                  <p className="text-xs font-bold text-slate-800 dark:text-white">Admin User</p>
                  <p className="text-[10px] text-slate-400 font-medium">Security Officer</p>
                </div>
              </button>
            </div>
          </div>
        </header>

        {/* Dynamic Content Area */}
        <div className="flex-1 overflow-y-auto p-8 bg-slate-50 dark:bg-slate-900 scroll-smooth">
          <div className="max-w-7xl mx-auto">
            {renderContent()}
          </div>
          
          <footer className="mt-20 py-8 border-t border-slate-200 dark:border-slate-800 flex flex-col md:flex-row justify-between items-center gap-4 text-slate-400 text-xs font-medium">
            <p>© 2023 Secure AI Fraud Systems. All rights reserved.</p>
            <div className="flex space-x-6 uppercase tracking-widest">
              <a href="#" className="hover:text-indigo-500 transition-colors">Privacy Policy</a>
              <a href="#" className="hover:text-indigo-500 transition-colors">Terms of Service</a>
              <a href="#" className="hover:text-indigo-500 transition-colors">Compliance</a>
            </div>
          </footer>
        </div>
      </main>
    </div>
  );
};

export default App;
