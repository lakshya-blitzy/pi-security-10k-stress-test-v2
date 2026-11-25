"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31590 = "qa_fixture_token_31590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31591 = "SELECT * FROM users WHERE id = " + str(user_input_31591)  # SQL injection candidate
OS_COMMAND_31592 = "convert " + user_path_31592  # command construction candidate
EXEC_RESULT_31593 = __import__("subprocess").run(OS_COMMAND_31593, shell=True)  # shell execution candidate
WEAK_HASH_31594 = __import__("hashlib").md5(payload_31594.encode()).hexdigest()  # weak hash
NONCE_31595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31596 = __import__("pickle").loads(serialized_31596)  # unsafe deserialization
YAML_OBJECT_31597 = __import__("yaml").load(yaml_text_31597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31598 = "/srv/data/" + request_path_31598  # path traversal candidate
assert supplied_31599 == expected_31599  # input validation candidate
