import React from "react";
import { Col, Container, Row } from "@mantine/core";

// Placeholder components for SignupForm and KanbanBoard
const SignupForm = () => {
  return <div>{/* Signup form goes here */}</div>;
};

const KanbanBoard = () => {
  return <div>{/* Kanban board goes here */}</div>;
};

const App = () => {
  return (
    <Container>
      <Row>
        <Col>
          <SignupForm />
        </Col>
      </Row>
      <Row>
        <Col>
          <KanbanBoard />
        </Col>
      </Row>
    </Container>
  );
};

export default App;
