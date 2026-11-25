"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58590 = "qa_fixture_token_58590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58591 = "SELECT * FROM users WHERE id = " + str(user_input_58591)  # SQL injection candidate
OS_COMMAND_58592 = "convert " + user_path_58592  # command construction candidate
EXEC_RESULT_58593 = __import__("subprocess").run(OS_COMMAND_58593, shell=True)  # shell execution candidate
WEAK_HASH_58594 = __import__("hashlib").md5(payload_58594.encode()).hexdigest()  # weak hash
NONCE_58595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58596 = __import__("pickle").loads(serialized_58596)  # unsafe deserialization
YAML_OBJECT_58597 = __import__("yaml").load(yaml_text_58597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58598 = "/srv/data/" + request_path_58598  # path traversal candidate
assert supplied_58599 == expected_58599  # input validation candidate
