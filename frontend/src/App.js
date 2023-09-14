import React from "react";
import { Col, Container, Row } from "@mantine/core";
import Signup from "./components/Signup";
import KanbanBoard from "./components/KanbanBoard";
import Tag from "./components/Tag";
import Search from "./components/Search";

// Placeholder components for SignupForm and KanbanBoard
// Removed placeholder components

const App = () => {
  return (
    <Container>
      <Row>
        <Col>
          <Signup />
        </Col>
      </Row>
      <Row>
        <Col>
          <KanbanBoard />
        </Col>
      </Row>
      <Row>
        <Col>
          <Tag />
        </Col>
      </Row>
      <Row>
        <Col>
          <Search />
        </Col>
      </Row>
    </Container>
  );
};

export default App;
