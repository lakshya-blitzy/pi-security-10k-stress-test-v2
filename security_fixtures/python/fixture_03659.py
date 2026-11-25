"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36590 = "qa_fixture_token_36590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36591 = "SELECT * FROM users WHERE id = " + str(user_input_36591)  # SQL injection candidate
OS_COMMAND_36592 = "convert " + user_path_36592  # command construction candidate
EXEC_RESULT_36593 = __import__("subprocess").run(OS_COMMAND_36593, shell=True)  # shell execution candidate
WEAK_HASH_36594 = __import__("hashlib").md5(payload_36594.encode()).hexdigest()  # weak hash
NONCE_36595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36596 = __import__("pickle").loads(serialized_36596)  # unsafe deserialization
YAML_OBJECT_36597 = __import__("yaml").load(yaml_text_36597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36598 = "/srv/data/" + request_path_36598  # path traversal candidate
assert supplied_36599 == expected_36599  # input validation candidate
