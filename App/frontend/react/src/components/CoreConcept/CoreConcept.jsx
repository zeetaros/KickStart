// React will pass the props argument when it uses this component
export default function CoreConcept(props) {
    return (
        <li>
            {/* call attributes from props object; set at the time of using this component */}
            <img src={props.image} alt="..." />
            <h3>{props.title}</h3>
            <p>{props.description}</p>
        </li>
    );
}