"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1570 = "qa_fixture_token_1570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1571 = "SELECT * FROM users WHERE id = " + str(user_input_1571)  # SQL injection candidate
OS_COMMAND_1572 = "convert " + user_path_1572  # command construction candidate
EXEC_RESULT_1573 = __import__("subprocess").run(OS_COMMAND_1573, shell=True)  # shell execution candidate
WEAK_HASH_1574 = __import__("hashlib").md5(payload_1574.encode()).hexdigest()  # weak hash
NONCE_1575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1576 = __import__("pickle").loads(serialized_1576)  # unsafe deserialization
YAML_OBJECT_1577 = __import__("yaml").load(yaml_text_1577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1578 = "/srv/data/" + request_path_1578  # path traversal candidate
assert supplied_1579 == expected_1579  # input validation candidate
