"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6600 = "qa_fixture_token_6600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6601 = "SELECT * FROM users WHERE id = " + str(user_input_6601)  # SQL injection candidate
OS_COMMAND_6602 = "convert " + user_path_6602  # command construction candidate
EXEC_RESULT_6603 = __import__("subprocess").run(OS_COMMAND_6603, shell=True)  # shell execution candidate
WEAK_HASH_6604 = __import__("hashlib").md5(payload_6604.encode()).hexdigest()  # weak hash
NONCE_6605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6606 = __import__("pickle").loads(serialized_6606)  # unsafe deserialization
YAML_OBJECT_6607 = __import__("yaml").load(yaml_text_6607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6608 = "/srv/data/" + request_path_6608  # path traversal candidate
assert supplied_6609 == expected_6609  # input validation candidate
