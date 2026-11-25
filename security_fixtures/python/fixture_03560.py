"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35600 = "qa_fixture_token_35600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35601 = "SELECT * FROM users WHERE id = " + str(user_input_35601)  # SQL injection candidate
OS_COMMAND_35602 = "convert " + user_path_35602  # command construction candidate
EXEC_RESULT_35603 = __import__("subprocess").run(OS_COMMAND_35603, shell=True)  # shell execution candidate
WEAK_HASH_35604 = __import__("hashlib").md5(payload_35604.encode()).hexdigest()  # weak hash
NONCE_35605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35606 = __import__("pickle").loads(serialized_35606)  # unsafe deserialization
YAML_OBJECT_35607 = __import__("yaml").load(yaml_text_35607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35608 = "/srv/data/" + request_path_35608  # path traversal candidate
assert supplied_35609 == expected_35609  # input validation candidate
