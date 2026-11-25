"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1520 = "qa_fixture_token_1520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1521 = "SELECT * FROM users WHERE id = " + str(user_input_1521)  # SQL injection candidate
OS_COMMAND_1522 = "convert " + user_path_1522  # command construction candidate
EXEC_RESULT_1523 = __import__("subprocess").run(OS_COMMAND_1523, shell=True)  # shell execution candidate
WEAK_HASH_1524 = __import__("hashlib").md5(payload_1524.encode()).hexdigest()  # weak hash
NONCE_1525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1526 = __import__("pickle").loads(serialized_1526)  # unsafe deserialization
YAML_OBJECT_1527 = __import__("yaml").load(yaml_text_1527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1528 = "/srv/data/" + request_path_1528  # path traversal candidate
assert supplied_1529 == expected_1529  # input validation candidate
