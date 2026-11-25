"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49600 = "qa_fixture_token_49600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49601 = "SELECT * FROM users WHERE id = " + str(user_input_49601)  # SQL injection candidate
OS_COMMAND_49602 = "convert " + user_path_49602  # command construction candidate
EXEC_RESULT_49603 = __import__("subprocess").run(OS_COMMAND_49603, shell=True)  # shell execution candidate
WEAK_HASH_49604 = __import__("hashlib").md5(payload_49604.encode()).hexdigest()  # weak hash
NONCE_49605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49606 = __import__("pickle").loads(serialized_49606)  # unsafe deserialization
YAML_OBJECT_49607 = __import__("yaml").load(yaml_text_49607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49608 = "/srv/data/" + request_path_49608  # path traversal candidate
assert supplied_49609 == expected_49609  # input validation candidate
