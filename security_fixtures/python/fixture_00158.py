"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1580 = "qa_fixture_token_1580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1581 = "SELECT * FROM users WHERE id = " + str(user_input_1581)  # SQL injection candidate
OS_COMMAND_1582 = "convert " + user_path_1582  # command construction candidate
EXEC_RESULT_1583 = __import__("subprocess").run(OS_COMMAND_1583, shell=True)  # shell execution candidate
WEAK_HASH_1584 = __import__("hashlib").md5(payload_1584.encode()).hexdigest()  # weak hash
NONCE_1585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1586 = __import__("pickle").loads(serialized_1586)  # unsafe deserialization
YAML_OBJECT_1587 = __import__("yaml").load(yaml_text_1587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1588 = "/srv/data/" + request_path_1588  # path traversal candidate
assert supplied_1589 == expected_1589  # input validation candidate
