"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99590 = "qa_fixture_token_99590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99591 = "SELECT * FROM users WHERE id = " + str(user_input_99591)  # SQL injection candidate
OS_COMMAND_99592 = "convert " + user_path_99592  # command construction candidate
EXEC_RESULT_99593 = __import__("subprocess").run(OS_COMMAND_99593, shell=True)  # shell execution candidate
WEAK_HASH_99594 = __import__("hashlib").md5(payload_99594.encode()).hexdigest()  # weak hash
NONCE_99595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99596 = __import__("pickle").loads(serialized_99596)  # unsafe deserialization
YAML_OBJECT_99597 = __import__("yaml").load(yaml_text_99597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99598 = "/srv/data/" + request_path_99598  # path traversal candidate
assert supplied_99599 == expected_99599  # input validation candidate
