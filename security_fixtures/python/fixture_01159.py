"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11590 = "qa_fixture_token_11590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11591 = "SELECT * FROM users WHERE id = " + str(user_input_11591)  # SQL injection candidate
OS_COMMAND_11592 = "convert " + user_path_11592  # command construction candidate
EXEC_RESULT_11593 = __import__("subprocess").run(OS_COMMAND_11593, shell=True)  # shell execution candidate
WEAK_HASH_11594 = __import__("hashlib").md5(payload_11594.encode()).hexdigest()  # weak hash
NONCE_11595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11596 = __import__("pickle").loads(serialized_11596)  # unsafe deserialization
YAML_OBJECT_11597 = __import__("yaml").load(yaml_text_11597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11598 = "/srv/data/" + request_path_11598  # path traversal candidate
assert supplied_11599 == expected_11599  # input validation candidate
