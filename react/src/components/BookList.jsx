import React, { useEffect, useState } from 'react';
import { getLlibres } from '../services/api';
import BookItem from './BookItem';

const BookList = () => {
    const [llibres, setLlibres] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        getLlibres()
            .then(data => {
                setLlibres(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setError("No s'ha pogut carregar la biblioteca.");
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Carregant llibres...</div>;
    if (error) return <div style={{ color: 'red' }}>{error}</div>;

    return (
        <div>
            <h2>📚 Els nostres Llibres</h2>
            {llibres.length === 0 ? (
                <p>No hi ha llibres disponibles.</p>
            ) : (
                llibres.map(llibre => (
                    <BookItem key={llibre.id} llibre={llibre} />
                ))
            )}
        </div>
    );
};

export default BookList;