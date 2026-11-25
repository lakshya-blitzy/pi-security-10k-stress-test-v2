"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79590 = "qa_fixture_token_79590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79591 = "SELECT * FROM users WHERE id = " + str(user_input_79591)  # SQL injection candidate
OS_COMMAND_79592 = "convert " + user_path_79592  # command construction candidate
EXEC_RESULT_79593 = __import__("subprocess").run(OS_COMMAND_79593, shell=True)  # shell execution candidate
WEAK_HASH_79594 = __import__("hashlib").md5(payload_79594.encode()).hexdigest()  # weak hash
NONCE_79595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79596 = __import__("pickle").loads(serialized_79596)  # unsafe deserialization
YAML_OBJECT_79597 = __import__("yaml").load(yaml_text_79597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79598 = "/srv/data/" + request_path_79598  # path traversal candidate
assert supplied_79599 == expected_79599  # input validation candidate
