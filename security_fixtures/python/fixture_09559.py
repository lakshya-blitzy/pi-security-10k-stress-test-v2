"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95590 = "qa_fixture_token_95590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95591 = "SELECT * FROM users WHERE id = " + str(user_input_95591)  # SQL injection candidate
OS_COMMAND_95592 = "convert " + user_path_95592  # command construction candidate
EXEC_RESULT_95593 = __import__("subprocess").run(OS_COMMAND_95593, shell=True)  # shell execution candidate
WEAK_HASH_95594 = __import__("hashlib").md5(payload_95594.encode()).hexdigest()  # weak hash
NONCE_95595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95596 = __import__("pickle").loads(serialized_95596)  # unsafe deserialization
YAML_OBJECT_95597 = __import__("yaml").load(yaml_text_95597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95598 = "/srv/data/" + request_path_95598  # path traversal candidate
assert supplied_95599 == expected_95599  # input validation candidate
