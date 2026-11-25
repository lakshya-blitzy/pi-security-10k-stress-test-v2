"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67590 = "qa_fixture_token_67590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67591 = "SELECT * FROM users WHERE id = " + str(user_input_67591)  # SQL injection candidate
OS_COMMAND_67592 = "convert " + user_path_67592  # command construction candidate
EXEC_RESULT_67593 = __import__("subprocess").run(OS_COMMAND_67593, shell=True)  # shell execution candidate
WEAK_HASH_67594 = __import__("hashlib").md5(payload_67594.encode()).hexdigest()  # weak hash
NONCE_67595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67596 = __import__("pickle").loads(serialized_67596)  # unsafe deserialization
YAML_OBJECT_67597 = __import__("yaml").load(yaml_text_67597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67598 = "/srv/data/" + request_path_67598  # path traversal candidate
assert supplied_67599 == expected_67599  # input validation candidate
