import CONFIG from '../config';

export const getLlibres = async () => {
    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/llibres`);
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error al servei API:", error);
        throw error;
    }
};