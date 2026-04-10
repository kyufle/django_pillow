import React, { useState } from 'react';

const BookItem = ({ llibre }) => {
    const [showDetails, setShowDetails] = useState(false);
    const toggleDetails = () => {
        setShowDetails(!showDetails);
    };

    return (
        <div style={{
            border: '1px solid #ddd',
            borderRadius: '10px',
            padding: '20px',
            marginBottom: '15px',
            backgroundColor: '#fff',
            boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
        }}>
            <h3 style={{ margin: '0 0 10px 0' }}>{llibre.titol}</h3>
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
                {showDetails ? 'Ocultar info' : 'Ver descripción y fotos'}
            </button>

            {showDetails && (
                <div style={{ 
                    marginTop: '20px', 
                    paddingTop: '15px', 
                    borderTop: '1px dashed #ccc',
                    animation: 'fadeIn 0.5s'
                }}>
                    <h4>Detalles del libro:</h4>
                    <p><strong>Fecha de edición:</strong> {llibre.data_edicio}</p>
                    
                    {llibre.resum ? (
                        <p><strong>Descripción:</strong> {llibre.resum}</p>
                    ) : (
                        <p><em>No hay descripción disponible.</em></p>
                    )}

                    {llibre.portada_url && (
                        <div style={{ marginTop: '15px' }}>
                            <img 
                                src={llibre.portada_url} 
                                alt={`Portada de ${llibre.titol}`} 
                                style={{ maxWidth: '200px', borderRadius: '5px' }}
                            />
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default BookItem;