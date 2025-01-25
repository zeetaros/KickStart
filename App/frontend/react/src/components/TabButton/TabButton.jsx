// Create a component called "TabButton"
export default function TabButton({children, onSelect}) {
    // "children" is a special props reserved and set only by React that isn't user defined.

    // Inner function. The scope is only limited to the parent function. 
    // Inner function have access to the component's props and state.
    function clickHandler() {
        console.log("Hello World -- click!");
    }

    return (
        <li>
            {/* onClick is an event listener. It should trigger another function */}
            {/* In this example, it uses the handler receieved from props instead of the one defined in inner function */}
            <button onClick={onSelect}>{children}</button>
        </li>
    );
}
