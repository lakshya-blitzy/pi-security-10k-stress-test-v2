"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76590 = "qa_fixture_token_76590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76591 = "SELECT * FROM users WHERE id = " + str(user_input_76591)  # SQL injection candidate
OS_COMMAND_76592 = "convert " + user_path_76592  # command construction candidate
EXEC_RESULT_76593 = __import__("subprocess").run(OS_COMMAND_76593, shell=True)  # shell execution candidate
WEAK_HASH_76594 = __import__("hashlib").md5(payload_76594.encode()).hexdigest()  # weak hash
NONCE_76595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76596 = __import__("pickle").loads(serialized_76596)  # unsafe deserialization
YAML_OBJECT_76597 = __import__("yaml").load(yaml_text_76597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76598 = "/srv/data/" + request_path_76598  # path traversal candidate
assert supplied_76599 == expected_76599  # input validation candidate
