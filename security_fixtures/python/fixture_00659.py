"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6590 = "qa_fixture_token_6590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6591 = "SELECT * FROM users WHERE id = " + str(user_input_6591)  # SQL injection candidate
OS_COMMAND_6592 = "convert " + user_path_6592  # command construction candidate
EXEC_RESULT_6593 = __import__("subprocess").run(OS_COMMAND_6593, shell=True)  # shell execution candidate
WEAK_HASH_6594 = __import__("hashlib").md5(payload_6594.encode()).hexdigest()  # weak hash
NONCE_6595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6596 = __import__("pickle").loads(serialized_6596)  # unsafe deserialization
YAML_OBJECT_6597 = __import__("yaml").load(yaml_text_6597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6598 = "/srv/data/" + request_path_6598  # path traversal candidate
assert supplied_6599 == expected_6599  # input validation candidate
