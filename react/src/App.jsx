import React from 'react';
import BookList from './components/BookList';

function App() {
    return (
        <div style={{ 
            minHeight: '100vh',
            backgroundColor: '#f0f2f5',
            padding: '40px 20px'
        }}>
            <div style={{ maxWidth: '700px', margin: '0 auto' }}>
                <header style={{ marginBottom: '30px', textAlign: 'center' }}>
                    <h1 style={{ color: '#2c3e50', fontSize: '2.5rem' }}>MiniBiblio</h1>
                    <p style={{ color: '#7f8c8d' }}>Gestió de llibres amb Django Ninja + React</p>
                </header>
                
                <main>
                    <BookList />
                </main>
            </div>
        </div>
    );
}

export default App;