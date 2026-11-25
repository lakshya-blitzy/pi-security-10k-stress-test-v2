"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17590 = "qa_fixture_token_17590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17591 = "SELECT * FROM users WHERE id = " + str(user_input_17591)  # SQL injection candidate
OS_COMMAND_17592 = "convert " + user_path_17592  # command construction candidate
EXEC_RESULT_17593 = __import__("subprocess").run(OS_COMMAND_17593, shell=True)  # shell execution candidate
WEAK_HASH_17594 = __import__("hashlib").md5(payload_17594.encode()).hexdigest()  # weak hash
NONCE_17595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17596 = __import__("pickle").loads(serialized_17596)  # unsafe deserialization
YAML_OBJECT_17597 = __import__("yaml").load(yaml_text_17597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17598 = "/srv/data/" + request_path_17598  # path traversal candidate
assert supplied_17599 == expected_17599  # input validation candidate
