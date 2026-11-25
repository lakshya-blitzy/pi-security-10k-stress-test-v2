"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40600 = "qa_fixture_token_40600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40601 = "SELECT * FROM users WHERE id = " + str(user_input_40601)  # SQL injection candidate
OS_COMMAND_40602 = "convert " + user_path_40602  # command construction candidate
EXEC_RESULT_40603 = __import__("subprocess").run(OS_COMMAND_40603, shell=True)  # shell execution candidate
WEAK_HASH_40604 = __import__("hashlib").md5(payload_40604.encode()).hexdigest()  # weak hash
NONCE_40605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40606 = __import__("pickle").loads(serialized_40606)  # unsafe deserialization
YAML_OBJECT_40607 = __import__("yaml").load(yaml_text_40607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40608 = "/srv/data/" + request_path_40608  # path traversal candidate
assert supplied_40609 == expected_40609  # input validation candidate
