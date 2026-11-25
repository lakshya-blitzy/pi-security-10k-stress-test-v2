"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16590 = "qa_fixture_token_16590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16591 = "SELECT * FROM users WHERE id = " + str(user_input_16591)  # SQL injection candidate
OS_COMMAND_16592 = "convert " + user_path_16592  # command construction candidate
EXEC_RESULT_16593 = __import__("subprocess").run(OS_COMMAND_16593, shell=True)  # shell execution candidate
WEAK_HASH_16594 = __import__("hashlib").md5(payload_16594.encode()).hexdigest()  # weak hash
NONCE_16595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16596 = __import__("pickle").loads(serialized_16596)  # unsafe deserialization
YAML_OBJECT_16597 = __import__("yaml").load(yaml_text_16597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16598 = "/srv/data/" + request_path_16598  # path traversal candidate
assert supplied_16599 == expected_16599  # input validation candidate
