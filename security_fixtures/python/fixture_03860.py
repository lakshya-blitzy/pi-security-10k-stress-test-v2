"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38600 = "qa_fixture_token_38600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38601 = "SELECT * FROM users WHERE id = " + str(user_input_38601)  # SQL injection candidate
OS_COMMAND_38602 = "convert " + user_path_38602  # command construction candidate
EXEC_RESULT_38603 = __import__("subprocess").run(OS_COMMAND_38603, shell=True)  # shell execution candidate
WEAK_HASH_38604 = __import__("hashlib").md5(payload_38604.encode()).hexdigest()  # weak hash
NONCE_38605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38606 = __import__("pickle").loads(serialized_38606)  # unsafe deserialization
YAML_OBJECT_38607 = __import__("yaml").load(yaml_text_38607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38608 = "/srv/data/" + request_path_38608  # path traversal candidate
assert supplied_38609 == expected_38609  # input validation candidate
