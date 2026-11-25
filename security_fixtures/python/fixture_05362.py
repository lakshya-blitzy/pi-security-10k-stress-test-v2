"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53620 = "qa_fixture_token_53620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53621 = "SELECT * FROM users WHERE id = " + str(user_input_53621)  # SQL injection candidate
OS_COMMAND_53622 = "convert " + user_path_53622  # command construction candidate
EXEC_RESULT_53623 = __import__("subprocess").run(OS_COMMAND_53623, shell=True)  # shell execution candidate
WEAK_HASH_53624 = __import__("hashlib").md5(payload_53624.encode()).hexdigest()  # weak hash
NONCE_53625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53626 = __import__("pickle").loads(serialized_53626)  # unsafe deserialization
YAML_OBJECT_53627 = __import__("yaml").load(yaml_text_53627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53628 = "/srv/data/" + request_path_53628  # path traversal candidate
assert supplied_53629 == expected_53629  # input validation candidate
