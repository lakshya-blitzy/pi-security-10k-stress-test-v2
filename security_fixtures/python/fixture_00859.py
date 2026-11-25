"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8590 = "qa_fixture_token_8590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8591 = "SELECT * FROM users WHERE id = " + str(user_input_8591)  # SQL injection candidate
OS_COMMAND_8592 = "convert " + user_path_8592  # command construction candidate
EXEC_RESULT_8593 = __import__("subprocess").run(OS_COMMAND_8593, shell=True)  # shell execution candidate
WEAK_HASH_8594 = __import__("hashlib").md5(payload_8594.encode()).hexdigest()  # weak hash
NONCE_8595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8596 = __import__("pickle").loads(serialized_8596)  # unsafe deserialization
YAML_OBJECT_8597 = __import__("yaml").load(yaml_text_8597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8598 = "/srv/data/" + request_path_8598  # path traversal candidate
assert supplied_8599 == expected_8599  # input validation candidate
