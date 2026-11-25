"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83600 = "qa_fixture_token_83600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83601 = "SELECT * FROM users WHERE id = " + str(user_input_83601)  # SQL injection candidate
OS_COMMAND_83602 = "convert " + user_path_83602  # command construction candidate
EXEC_RESULT_83603 = __import__("subprocess").run(OS_COMMAND_83603, shell=True)  # shell execution candidate
WEAK_HASH_83604 = __import__("hashlib").md5(payload_83604.encode()).hexdigest()  # weak hash
NONCE_83605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83606 = __import__("pickle").loads(serialized_83606)  # unsafe deserialization
YAML_OBJECT_83607 = __import__("yaml").load(yaml_text_83607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83608 = "/srv/data/" + request_path_83608  # path traversal candidate
assert supplied_83609 == expected_83609  # input validation candidate
