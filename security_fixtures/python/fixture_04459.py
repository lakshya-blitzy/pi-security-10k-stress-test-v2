"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44590 = "qa_fixture_token_44590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44591 = "SELECT * FROM users WHERE id = " + str(user_input_44591)  # SQL injection candidate
OS_COMMAND_44592 = "convert " + user_path_44592  # command construction candidate
EXEC_RESULT_44593 = __import__("subprocess").run(OS_COMMAND_44593, shell=True)  # shell execution candidate
WEAK_HASH_44594 = __import__("hashlib").md5(payload_44594.encode()).hexdigest()  # weak hash
NONCE_44595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44596 = __import__("pickle").loads(serialized_44596)  # unsafe deserialization
YAML_OBJECT_44597 = __import__("yaml").load(yaml_text_44597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44598 = "/srv/data/" + request_path_44598  # path traversal candidate
assert supplied_44599 == expected_44599  # input validation candidate
