function fetchRecipes() {
    return fetch("http://localhost:8000/recipes").then(res => res.json())
}

export default function Home() {
    let recipes = []

    fetchRecipes().then((results) => {
        recipes = results
    })

    return (
        <div>
            <h1>Recifree</h1>
            <div>List of all recipes:</div>
            <ul>
                { recipes.forEach(r => {
                    return <li>{r.title}</li>
                })}
            </ul>
        </div>
    )
}
