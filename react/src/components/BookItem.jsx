import React, { useState } from 'react';

const BookItem = ({ llibre }) => {
    const [showDetails, setShowDetails] = useState(false);
    
    // URL base de tu servidor Django
    const API_BASE_URL = 'http://localhost:8000';

    const toggleDetails = () => setShowDetails(!showDetails);

    // Función para limpiar las URLs que vienen de Django
    const getFullUrl = (path) => {
        if (!path) return null;
        if (path.startsWith('http')) return path;
        return `${API_BASE_URL}${path}`;
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
                    cursor: 'pointer'
                }}
            >
                {showDetails ? 'Ocultar detalles' : 'Ver descripción y fotos'}
            </button>

            {showDetails && (
                <div style={{ marginTop: '20px', borderTop: '1px solid #eee', paddingTop: '15px' }}>
                    <p><strong>Fecha edición:</strong> {llibre.data_edicio}</p>
                    <p><strong>Resumen:</strong> {llibre.resum || 'Sin descripción.'}</p>

                    {/* IMAGEN PRINCIPAL (Campo 'imatge' en tu modelo) */}
                    {llibre.imatge && (
                        <div style={{ marginBottom: '20px' }}>
                            <h4>Portada:</h4>
                            <img 
                                src={getFullUrl(llibre.imatge)} 
                                alt="Portada" 
                                style={{ maxWidth: '200px', borderRadius: '8px' }} 
                            />
                        </div>
                    )}

                    {/* GALERÍA (Si tu API devuelve el related_name 'galeria') */}
                    {llibre.galeria && llibre.galeria.length > 0 && (
                        <div>
                            <h4>Galería de fotos:</h4>
                            <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                                {llibre.galeria.map((imgObj, index) => (
                                    <img 
                                        key={index}
                                        src={getFullUrl(imgObj.imatge)} 
                                        alt={imgObj.descripcio || 'Imagen galería'}
                                        style={{ width: '100px', height: '100px', objectFit: 'cover', borderRadius: '5px' }}
                                    />
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default BookItem;