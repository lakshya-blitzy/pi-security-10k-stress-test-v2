"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91590 = "qa_fixture_token_91590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91591 = "SELECT * FROM users WHERE id = " + str(user_input_91591)  # SQL injection candidate
OS_COMMAND_91592 = "convert " + user_path_91592  # command construction candidate
EXEC_RESULT_91593 = __import__("subprocess").run(OS_COMMAND_91593, shell=True)  # shell execution candidate
WEAK_HASH_91594 = __import__("hashlib").md5(payload_91594.encode()).hexdigest()  # weak hash
NONCE_91595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91596 = __import__("pickle").loads(serialized_91596)  # unsafe deserialization
YAML_OBJECT_91597 = __import__("yaml").load(yaml_text_91597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91598 = "/srv/data/" + request_path_91598  # path traversal candidate
assert supplied_91599 == expected_91599  # input validation candidate
