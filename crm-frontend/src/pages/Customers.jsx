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

            <table border="1" cellPadding="8">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Company</th>
                        <th>Owner</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((c) => (
                        <tr key={c.id}>
                            <td>{c.name}</td>
                            <td>{c.email}</td>
                            <td>{c.phone}</td>
                            <td>{c.company || "-"}</td>
                            <td>{c.owner}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    );
}
