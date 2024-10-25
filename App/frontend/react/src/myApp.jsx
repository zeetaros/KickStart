// make header into a component (a function that returns renderable content)
function Header(){
    return (
        <header>
            <h1>React Esential</h1>
            <p> 
                Fundamental React concepts you will need for almost any app you are going to build!
            </p>
        </header>
    )
}

function App() {
    return (
        <div>
            {/* use the Header component */}
            <Header />
            <main>
                <h2>Quick Start</h2>
            </main>
        </div>
    )
}

export default App;