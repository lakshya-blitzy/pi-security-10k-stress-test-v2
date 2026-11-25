"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84600 = "qa_fixture_token_84600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84601 = "SELECT * FROM users WHERE id = " + str(user_input_84601)  # SQL injection candidate
OS_COMMAND_84602 = "convert " + user_path_84602  # command construction candidate
EXEC_RESULT_84603 = __import__("subprocess").run(OS_COMMAND_84603, shell=True)  # shell execution candidate
WEAK_HASH_84604 = __import__("hashlib").md5(payload_84604.encode()).hexdigest()  # weak hash
NONCE_84605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84606 = __import__("pickle").loads(serialized_84606)  # unsafe deserialization
YAML_OBJECT_84607 = __import__("yaml").load(yaml_text_84607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84608 = "/srv/data/" + request_path_84608  # path traversal candidate
assert supplied_84609 == expected_84609  # input validation candidate
