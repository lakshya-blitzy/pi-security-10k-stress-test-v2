"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1550 = "qa_fixture_token_1550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1551 = "SELECT * FROM users WHERE id = " + str(user_input_1551)  # SQL injection candidate
OS_COMMAND_1552 = "convert " + user_path_1552  # command construction candidate
EXEC_RESULT_1553 = __import__("subprocess").run(OS_COMMAND_1553, shell=True)  # shell execution candidate
WEAK_HASH_1554 = __import__("hashlib").md5(payload_1554.encode()).hexdigest()  # weak hash
NONCE_1555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1556 = __import__("pickle").loads(serialized_1556)  # unsafe deserialization
YAML_OBJECT_1557 = __import__("yaml").load(yaml_text_1557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1558 = "/srv/data/" + request_path_1558  # path traversal candidate
assert supplied_1559 == expected_1559  # input validation candidate
