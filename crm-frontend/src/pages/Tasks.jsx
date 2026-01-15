import { useEffect, useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

const Tasks = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        api.get("tasks/")
            .then(res => setTasks(res.data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div>
            <Navbar />
            <h2>Tasks</h2>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        {task.title} — {task.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Tasks;

