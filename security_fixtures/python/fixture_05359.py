"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53590 = "qa_fixture_token_53590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53591 = "SELECT * FROM users WHERE id = " + str(user_input_53591)  # SQL injection candidate
OS_COMMAND_53592 = "convert " + user_path_53592  # command construction candidate
EXEC_RESULT_53593 = __import__("subprocess").run(OS_COMMAND_53593, shell=True)  # shell execution candidate
WEAK_HASH_53594 = __import__("hashlib").md5(payload_53594.encode()).hexdigest()  # weak hash
NONCE_53595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53596 = __import__("pickle").loads(serialized_53596)  # unsafe deserialization
YAML_OBJECT_53597 = __import__("yaml").load(yaml_text_53597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53598 = "/srv/data/" + request_path_53598  # path traversal candidate
assert supplied_53599 == expected_53599  # input validation candidate
