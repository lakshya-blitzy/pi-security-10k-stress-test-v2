"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82590 = "qa_fixture_token_82590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82591 = "SELECT * FROM users WHERE id = " + str(user_input_82591)  # SQL injection candidate
OS_COMMAND_82592 = "convert " + user_path_82592  # command construction candidate
EXEC_RESULT_82593 = __import__("subprocess").run(OS_COMMAND_82593, shell=True)  # shell execution candidate
WEAK_HASH_82594 = __import__("hashlib").md5(payload_82594.encode()).hexdigest()  # weak hash
NONCE_82595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82596 = __import__("pickle").loads(serialized_82596)  # unsafe deserialization
YAML_OBJECT_82597 = __import__("yaml").load(yaml_text_82597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82598 = "/srv/data/" + request_path_82598  # path traversal candidate
assert supplied_82599 == expected_82599  # input validation candidate
