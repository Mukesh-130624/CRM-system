import { useEffect, useState } from "react";
import { getCustomers } from "../api/customers";
import Navbar from "../components/Navbar";

export default function Customers() {
    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        getCustomers().then((res) => setCustomers(res.data));
    }, []);

    return (
        <>
            <Navbar />
            <h2>Customers</h2>

            <ul>
                {customers.map((c) => (
                    <li key={c.id}>
                        {c.name} – {c.email}
                    </li>
                ))}
            </ul>
        </>
    );
}
