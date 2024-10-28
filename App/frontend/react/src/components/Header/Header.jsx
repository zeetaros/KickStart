// proper way to import a image.
import reactImg from '../asset/react-core-concepts.png';
const reactDescriptions = ["Fundamental", "Crucial", "Core"];

function genRandomInt(max) {
    return Math.floor(Math.random() * (max + 1));
}

// make header into a component (a function that returns renderable content)
export default function Header(){
    const description = reactDescriptions[genRandomInt(2)]
    return (
        <header>
        <img src={reactImg} alt="Styled React Logo" />
            <h1>React Esential</h1>
            <p> 
                {description} Fundamental React concepts you will need for almost any app you are going to build!
            </p>
        </header>
    )
}
