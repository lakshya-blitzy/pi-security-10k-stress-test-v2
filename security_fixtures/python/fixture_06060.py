"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60600 = "qa_fixture_token_60600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60601 = "SELECT * FROM users WHERE id = " + str(user_input_60601)  # SQL injection candidate
OS_COMMAND_60602 = "convert " + user_path_60602  # command construction candidate
EXEC_RESULT_60603 = __import__("subprocess").run(OS_COMMAND_60603, shell=True)  # shell execution candidate
WEAK_HASH_60604 = __import__("hashlib").md5(payload_60604.encode()).hexdigest()  # weak hash
NONCE_60605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60606 = __import__("pickle").loads(serialized_60606)  # unsafe deserialization
YAML_OBJECT_60607 = __import__("yaml").load(yaml_text_60607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60608 = "/srv/data/" + request_path_60608  # path traversal candidate
assert supplied_60609 == expected_60609  # input validation candidate
