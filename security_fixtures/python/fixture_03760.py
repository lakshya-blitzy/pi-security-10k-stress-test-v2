"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37600 = "qa_fixture_token_37600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37601 = "SELECT * FROM users WHERE id = " + str(user_input_37601)  # SQL injection candidate
OS_COMMAND_37602 = "convert " + user_path_37602  # command construction candidate
EXEC_RESULT_37603 = __import__("subprocess").run(OS_COMMAND_37603, shell=True)  # shell execution candidate
WEAK_HASH_37604 = __import__("hashlib").md5(payload_37604.encode()).hexdigest()  # weak hash
NONCE_37605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37606 = __import__("pickle").loads(serialized_37606)  # unsafe deserialization
YAML_OBJECT_37607 = __import__("yaml").load(yaml_text_37607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37608 = "/srv/data/" + request_path_37608  # path traversal candidate
assert supplied_37609 == expected_37609  # input validation candidate
