import { useState } from 'react';
// CORE_CONCEPTS is a named export in data.js not default export; Hence, import it explicitly with {}
import { CORE_CONCEPTS, CORE_CONCEPTS_V2 } from './data.js';
import Header from './components/Header/Header.jsx';  // this imports the default export function in Header.jsx and named the module "Header"
import CoreConcept from './components/CoreConcept/CoreConcept.jsx';
import TabButton from './components/TabButton/TabButton.jsx';


function App() {
    const [selectedTopic, setSelectedTopic] = useState("Please click a button");

    let tabContent = "Please click a button"
    function selectHandler(selectedButton) {
        // selectedButton => 'components', 'jsx', 'props', 'state'
        setSelectedTopic(selectedButton);
        console.log(tabContent);
    }

    return (
        <div>
            {/* use the Header component */}
            <Header />
            <main>
                <section id="core-concepts">
                <h2>Quick Start</h2>
                <ul>
                    {/* insert resusable React component */}
                    <CoreConcept 
                        // set attributes for the props object
                        title={CORE_CONCEPTS[0].title}
                        description={CORE_CONCEPTS[0].description}
                        image={CORE_CONCEPTS[0].image}
                    />
                    <CoreConcept 
                        title={CORE_CONCEPTS_V2[1].title}
                        description={CORE_CONCEPTS_V2[1].descr}
                        image={CORE_CONCEPTS_V2[1].img}
                    />
                    {/* short form if and only if attributes in CORE_CONCEPTS named the same as how it's called in component CoreConcept */}
                    <CoreConcept {...CORE_CONCEPTS[2]}/>
                    <CoreConcept {...CORE_CONCEPTS[3]}/>
                    
                </ul>
                </section>
                <section id="examples">
                    <h2>Examples</h2>
                    <menu>
                        {/* this way of using component is component composition by using children props */}
                        <TabButton onSelect={() => selectHandler('component')}>Component</TabButton>
                        <TabButton onSelect={() => selectHandler('jsx')}>JSX</TabButton>
                        <TabButton onSelect={() => selectHandler('props')}>Props</TabButton>
                        <TabButton onSelect={() => selectHandler('state')}>State</TabButton>
                    </menu>
                   {selectedTopic}
                </section>
            </main>
        </div>
    )
}

export default App;