"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88590 = "qa_fixture_token_88590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88591 = "SELECT * FROM users WHERE id = " + str(user_input_88591)  # SQL injection candidate
OS_COMMAND_88592 = "convert " + user_path_88592  # command construction candidate
EXEC_RESULT_88593 = __import__("subprocess").run(OS_COMMAND_88593, shell=True)  # shell execution candidate
WEAK_HASH_88594 = __import__("hashlib").md5(payload_88594.encode()).hexdigest()  # weak hash
NONCE_88595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88596 = __import__("pickle").loads(serialized_88596)  # unsafe deserialization
YAML_OBJECT_88597 = __import__("yaml").load(yaml_text_88597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88598 = "/srv/data/" + request_path_88598  # path traversal candidate
assert supplied_88599 == expected_88599  # input validation candidate
