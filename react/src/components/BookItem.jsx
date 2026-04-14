import React, { useState } from 'react';
import CONFIG from '../config';

const BookItem = ({ llibre }) => {
    const [showDetails, setShowDetails] = useState(false);
    
    const toggleDetails = () => setShowDetails(!showDetails);
    const getFullUrl = (path) => {
        if (!path) return null;
        if (path.startsWith('http')) return path;
        const domain = CONFIG.API_BASE_URL.replace('/api', '');
        return `${domain}${path}`;
    };

    return (
        <div style={{
            border: '1px solid #ddd',
            borderRadius: '10px',
            padding: '20px',
            marginBottom: '20px',
            backgroundColor: '#fff',
            boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
        }}>
            <h3 style={{ margin: '0' }}>{llibre.titol}</h3>
            <p><strong>Autor:</strong> {llibre.autor}</p>
            
            <button 
                onClick={toggleDetails}
                style={{
                    backgroundColor: '#3498db',
                    color: 'white',
                    border: 'none',
                    padding: '8px 15px',
                    borderRadius: '5px',
                    cursor: 'pointer',
                    marginTop: '10px'
                }}
            >
                {showDetails ? 'Ocultar detalles' : 'Ver descripción y fotos'}
            </button>

            {showDetails && (
                <div style={{ marginTop: '20px', borderTop: '1px solid #eee', paddingTop: '15px' }}>
                    <p><strong>Fecha edición:</strong> {llibre.data_edicio}</p>
                    <p><strong>Resumen:</strong> {llibre.resum || 'Sin descripción.'}</p>
                    {llibre.imatge && (
                        <div style={{ marginBottom: '20px' }}>
                            <h4>Portada:</h4>
                            <img 
                                src={getFullUrl(llibre.imatge)} 
                                alt={llibre.titol} 
                                style={{ maxWidth: '250px', borderRadius: '8px', boxShadow: '0 4px 10px rgba(0,0,0,0.2)' }} 
                            />
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default BookItem;