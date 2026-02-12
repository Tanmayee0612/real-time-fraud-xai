
export interface Transaction {
  id: string;
  merchant: string;
  amount: number;
  date: string;
  location: string;
  category: string;
  riskScore: number;
  status: 'SAFE' | 'SUSPICIOUS' | 'FRAUD';
  description: string;
}

export type AppTab = 'dashboard' | 'transactions' | 'xai' | 'verification' | 'settings';

export interface AIExplanation {
  explanation: string;
  factors: {
    name: string;
    impact: number;
    description: string;
  }[];
}
