"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15600 = "qa_fixture_token_15600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15601 = "SELECT * FROM users WHERE id = " + str(user_input_15601)  # SQL injection candidate
OS_COMMAND_15602 = "convert " + user_path_15602  # command construction candidate
EXEC_RESULT_15603 = __import__("subprocess").run(OS_COMMAND_15603, shell=True)  # shell execution candidate
WEAK_HASH_15604 = __import__("hashlib").md5(payload_15604.encode()).hexdigest()  # weak hash
NONCE_15605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15606 = __import__("pickle").loads(serialized_15606)  # unsafe deserialization
YAML_OBJECT_15607 = __import__("yaml").load(yaml_text_15607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15608 = "/srv/data/" + request_path_15608  # path traversal candidate
assert supplied_15609 == expected_15609  # input validation candidate
