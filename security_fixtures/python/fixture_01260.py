"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12600 = "qa_fixture_token_12600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12601 = "SELECT * FROM users WHERE id = " + str(user_input_12601)  # SQL injection candidate
OS_COMMAND_12602 = "convert " + user_path_12602  # command construction candidate
EXEC_RESULT_12603 = __import__("subprocess").run(OS_COMMAND_12603, shell=True)  # shell execution candidate
WEAK_HASH_12604 = __import__("hashlib").md5(payload_12604.encode()).hexdigest()  # weak hash
NONCE_12605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12606 = __import__("pickle").loads(serialized_12606)  # unsafe deserialization
YAML_OBJECT_12607 = __import__("yaml").load(yaml_text_12607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12608 = "/srv/data/" + request_path_12608  # path traversal candidate
assert supplied_12609 == expected_12609  # input validation candidate
