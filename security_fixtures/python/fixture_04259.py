"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42590 = "qa_fixture_token_42590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42591 = "SELECT * FROM users WHERE id = " + str(user_input_42591)  # SQL injection candidate
OS_COMMAND_42592 = "convert " + user_path_42592  # command construction candidate
EXEC_RESULT_42593 = __import__("subprocess").run(OS_COMMAND_42593, shell=True)  # shell execution candidate
WEAK_HASH_42594 = __import__("hashlib").md5(payload_42594.encode()).hexdigest()  # weak hash
NONCE_42595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42596 = __import__("pickle").loads(serialized_42596)  # unsafe deserialization
YAML_OBJECT_42597 = __import__("yaml").load(yaml_text_42597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42598 = "/srv/data/" + request_path_42598  # path traversal candidate
assert supplied_42599 == expected_42599  # input validation candidate
