import React from 'react';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            customers: []
        };
        this.fetchCustomers = this.fetchCustomers.bind(this);
    }

    fetchCustomers() {
        fetch('/crm/customers')
            .then(res => res.json(),
                res => null)
            .then(
                (result) => {
                    if (result !== null) {
                        this.setState({
                            customers: result
                        });
                    }
                }
            ).catch(error => {
            console.log(error);
        });
    }

    componentDidMount() {
        this.fetchCustomers();
    }

    render() {
        return (
            <table>
                <tr>
                    <th>Customer Name</th>
                    <th>Customer Email</th>
                </tr>
                {
                    this.state.customers.map(row => (
                            <tr>
                                <td>{row.name}</td>
                                <td>{row.email}</td>
                            </tr>
                        )
                    )
                }
            </table>
        )
    }
}

export default App;
