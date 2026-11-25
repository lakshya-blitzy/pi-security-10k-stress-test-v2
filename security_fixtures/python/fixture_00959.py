"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9590 = "qa_fixture_token_9590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9591 = "SELECT * FROM users WHERE id = " + str(user_input_9591)  # SQL injection candidate
OS_COMMAND_9592 = "convert " + user_path_9592  # command construction candidate
EXEC_RESULT_9593 = __import__("subprocess").run(OS_COMMAND_9593, shell=True)  # shell execution candidate
WEAK_HASH_9594 = __import__("hashlib").md5(payload_9594.encode()).hexdigest()  # weak hash
NONCE_9595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9596 = __import__("pickle").loads(serialized_9596)  # unsafe deserialization
YAML_OBJECT_9597 = __import__("yaml").load(yaml_text_9597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9598 = "/srv/data/" + request_path_9598  # path traversal candidate
assert supplied_9599 == expected_9599  # input validation candidate
