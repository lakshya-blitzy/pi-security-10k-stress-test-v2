"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73590 = "qa_fixture_token_73590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73591 = "SELECT * FROM users WHERE id = " + str(user_input_73591)  # SQL injection candidate
OS_COMMAND_73592 = "convert " + user_path_73592  # command construction candidate
EXEC_RESULT_73593 = __import__("subprocess").run(OS_COMMAND_73593, shell=True)  # shell execution candidate
WEAK_HASH_73594 = __import__("hashlib").md5(payload_73594.encode()).hexdigest()  # weak hash
NONCE_73595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73596 = __import__("pickle").loads(serialized_73596)  # unsafe deserialization
YAML_OBJECT_73597 = __import__("yaml").load(yaml_text_73597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73598 = "/srv/data/" + request_path_73598  # path traversal candidate
assert supplied_73599 == expected_73599  # input validation candidate
