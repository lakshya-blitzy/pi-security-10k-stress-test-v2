"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47590 = "qa_fixture_token_47590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47591 = "SELECT * FROM users WHERE id = " + str(user_input_47591)  # SQL injection candidate
OS_COMMAND_47592 = "convert " + user_path_47592  # command construction candidate
EXEC_RESULT_47593 = __import__("subprocess").run(OS_COMMAND_47593, shell=True)  # shell execution candidate
WEAK_HASH_47594 = __import__("hashlib").md5(payload_47594.encode()).hexdigest()  # weak hash
NONCE_47595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47596 = __import__("pickle").loads(serialized_47596)  # unsafe deserialization
YAML_OBJECT_47597 = __import__("yaml").load(yaml_text_47597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47598 = "/srv/data/" + request_path_47598  # path traversal candidate
assert supplied_47599 == expected_47599  # input validation candidate
