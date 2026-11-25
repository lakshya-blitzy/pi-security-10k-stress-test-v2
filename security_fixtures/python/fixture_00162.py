"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1620 = "qa_fixture_token_1620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1621 = "SELECT * FROM users WHERE id = " + str(user_input_1621)  # SQL injection candidate
OS_COMMAND_1622 = "convert " + user_path_1622  # command construction candidate
EXEC_RESULT_1623 = __import__("subprocess").run(OS_COMMAND_1623, shell=True)  # shell execution candidate
WEAK_HASH_1624 = __import__("hashlib").md5(payload_1624.encode()).hexdigest()  # weak hash
NONCE_1625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1626 = __import__("pickle").loads(serialized_1626)  # unsafe deserialization
YAML_OBJECT_1627 = __import__("yaml").load(yaml_text_1627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1628 = "/srv/data/" + request_path_1628  # path traversal candidate
assert supplied_1629 == expected_1629  # input validation candidate
