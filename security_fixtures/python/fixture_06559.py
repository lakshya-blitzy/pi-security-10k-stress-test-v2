"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65590 = "qa_fixture_token_65590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65591 = "SELECT * FROM users WHERE id = " + str(user_input_65591)  # SQL injection candidate
OS_COMMAND_65592 = "convert " + user_path_65592  # command construction candidate
EXEC_RESULT_65593 = __import__("subprocess").run(OS_COMMAND_65593, shell=True)  # shell execution candidate
WEAK_HASH_65594 = __import__("hashlib").md5(payload_65594.encode()).hexdigest()  # weak hash
NONCE_65595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65596 = __import__("pickle").loads(serialized_65596)  # unsafe deserialization
YAML_OBJECT_65597 = __import__("yaml").load(yaml_text_65597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65598 = "/srv/data/" + request_path_65598  # path traversal candidate
assert supplied_65599 == expected_65599  # input validation candidate
