import request from './req';


export const apiGetRecipes = () => {
    return {data: [
        {id: 1, title: 'Brownies', description: 'Brownie recipe', create_time: '2024-09-14 18:32:43', username: 'young.lixx'}, 
        {id: 2, title: 'Rose tteokbokki', description: 'Teokkbokki with roses', create_time: '2025-01-06 23:26:19', username: 'theo'}
    ]};
};