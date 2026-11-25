"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95600 = "qa_fixture_token_95600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95601 = "SELECT * FROM users WHERE id = " + str(user_input_95601)  # SQL injection candidate
OS_COMMAND_95602 = "convert " + user_path_95602  # command construction candidate
EXEC_RESULT_95603 = __import__("subprocess").run(OS_COMMAND_95603, shell=True)  # shell execution candidate
WEAK_HASH_95604 = __import__("hashlib").md5(payload_95604.encode()).hexdigest()  # weak hash
NONCE_95605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95606 = __import__("pickle").loads(serialized_95606)  # unsafe deserialization
YAML_OBJECT_95607 = __import__("yaml").load(yaml_text_95607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95608 = "/srv/data/" + request_path_95608  # path traversal candidate
assert supplied_95609 == expected_95609  # input validation candidate
