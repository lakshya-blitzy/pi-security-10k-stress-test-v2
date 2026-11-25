"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3600 = "qa_fixture_token_3600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3601 = "SELECT * FROM users WHERE id = " + str(user_input_3601)  # SQL injection candidate
OS_COMMAND_3602 = "convert " + user_path_3602  # command construction candidate
EXEC_RESULT_3603 = __import__("subprocess").run(OS_COMMAND_3603, shell=True)  # shell execution candidate
WEAK_HASH_3604 = __import__("hashlib").md5(payload_3604.encode()).hexdigest()  # weak hash
NONCE_3605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3606 = __import__("pickle").loads(serialized_3606)  # unsafe deserialization
YAML_OBJECT_3607 = __import__("yaml").load(yaml_text_3607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3608 = "/srv/data/" + request_path_3608  # path traversal candidate
assert supplied_3609 == expected_3609  # input validation candidate
