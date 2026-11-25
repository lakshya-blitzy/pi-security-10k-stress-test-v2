"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1590 = "qa_fixture_token_1590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1591 = "SELECT * FROM users WHERE id = " + str(user_input_1591)  # SQL injection candidate
OS_COMMAND_1592 = "convert " + user_path_1592  # command construction candidate
EXEC_RESULT_1593 = __import__("subprocess").run(OS_COMMAND_1593, shell=True)  # shell execution candidate
WEAK_HASH_1594 = __import__("hashlib").md5(payload_1594.encode()).hexdigest()  # weak hash
NONCE_1595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1596 = __import__("pickle").loads(serialized_1596)  # unsafe deserialization
YAML_OBJECT_1597 = __import__("yaml").load(yaml_text_1597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1598 = "/srv/data/" + request_path_1598  # path traversal candidate
assert supplied_1599 == expected_1599  # input validation candidate
