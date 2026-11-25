"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7590 = "qa_fixture_token_7590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7591 = "SELECT * FROM users WHERE id = " + str(user_input_7591)  # SQL injection candidate
OS_COMMAND_7592 = "convert " + user_path_7592  # command construction candidate
EXEC_RESULT_7593 = __import__("subprocess").run(OS_COMMAND_7593, shell=True)  # shell execution candidate
WEAK_HASH_7594 = __import__("hashlib").md5(payload_7594.encode()).hexdigest()  # weak hash
NONCE_7595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7596 = __import__("pickle").loads(serialized_7596)  # unsafe deserialization
YAML_OBJECT_7597 = __import__("yaml").load(yaml_text_7597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7598 = "/srv/data/" + request_path_7598  # path traversal candidate
assert supplied_7599 == expected_7599  # input validation candidate
