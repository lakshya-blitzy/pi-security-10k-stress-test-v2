"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22590 = "qa_fixture_token_22590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22591 = "SELECT * FROM users WHERE id = " + str(user_input_22591)  # SQL injection candidate
OS_COMMAND_22592 = "convert " + user_path_22592  # command construction candidate
EXEC_RESULT_22593 = __import__("subprocess").run(OS_COMMAND_22593, shell=True)  # shell execution candidate
WEAK_HASH_22594 = __import__("hashlib").md5(payload_22594.encode()).hexdigest()  # weak hash
NONCE_22595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22596 = __import__("pickle").loads(serialized_22596)  # unsafe deserialization
YAML_OBJECT_22597 = __import__("yaml").load(yaml_text_22597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22598 = "/srv/data/" + request_path_22598  # path traversal candidate
assert supplied_22599 == expected_22599  # input validation candidate
