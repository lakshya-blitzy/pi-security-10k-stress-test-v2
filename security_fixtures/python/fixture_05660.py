"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56600 = "qa_fixture_token_56600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56601 = "SELECT * FROM users WHERE id = " + str(user_input_56601)  # SQL injection candidate
OS_COMMAND_56602 = "convert " + user_path_56602  # command construction candidate
EXEC_RESULT_56603 = __import__("subprocess").run(OS_COMMAND_56603, shell=True)  # shell execution candidate
WEAK_HASH_56604 = __import__("hashlib").md5(payload_56604.encode()).hexdigest()  # weak hash
NONCE_56605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56606 = __import__("pickle").loads(serialized_56606)  # unsafe deserialization
YAML_OBJECT_56607 = __import__("yaml").load(yaml_text_56607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56608 = "/srv/data/" + request_path_56608  # path traversal candidate
assert supplied_56609 == expected_56609  # input validation candidate
