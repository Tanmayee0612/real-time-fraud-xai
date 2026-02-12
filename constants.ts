
import { Transaction } from './types';

export const MOCK_TRANSACTIONS: Transaction[] = [
  {
    id: 'TXN-001',
    merchant: 'Amazon India',
    amount: 12500.50,
    date: '2023-10-25 14:30',
    location: 'Banjara Hills, Hyderabad',
    category: 'Shopping',
    riskScore: 12,
    status: 'SAFE',
    description: 'Standard monthly shopping routine.'
  },
  {
    id: 'TXN-002',
    merchant: 'Digital Tech Solutions',
    amount: 85999.00,
    date: '2023-10-25 03:15',
    location: 'Secunderabad, Hyderabad',
    category: 'Electronics',
    riskScore: 88,
    status: 'FRAUD',
    description: 'High value transaction at an unusual hour from a location not previously visited.'
  },
  {
    id: 'TXN-003',
    merchant: 'Swiggy',
    amount: 845.20,
    date: '2023-10-24 19:45',
    location: 'Jubilee Hills, Hyderabad',
    category: 'Dining',
    riskScore: 5,
    status: 'SAFE',
    description: 'Food delivery within residential zone.'
  },
  {
    id: 'TXN-004',
    merchant: 'Crypto Exchange India',
    amount: 55000.00,
    date: '2023-10-24 12:10',
    location: 'HITEC City, Hyderabad',
    category: 'Finance',
    riskScore: 65,
    status: 'SUSPICIOUS',
    description: 'Rapid withdrawal to a newly linked wallet address.'
  },
  {
    id: 'TXN-005',
    merchant: 'Ratnadeep Supermarket',
    amount: 3200.00,
    date: '2023-10-23 10:20',
    location: 'Gachibowli, Hyderabad',
    category: 'Grocery',
    riskScore: 8,
    status: 'SAFE',
    description: 'Regular grocery purchase.'
  }
];

export const CORRECT_PIN = '1234';
