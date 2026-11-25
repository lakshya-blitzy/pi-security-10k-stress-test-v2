"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56590 = "qa_fixture_token_56590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56591 = "SELECT * FROM users WHERE id = " + str(user_input_56591)  # SQL injection candidate
OS_COMMAND_56592 = "convert " + user_path_56592  # command construction candidate
EXEC_RESULT_56593 = __import__("subprocess").run(OS_COMMAND_56593, shell=True)  # shell execution candidate
WEAK_HASH_56594 = __import__("hashlib").md5(payload_56594.encode()).hexdigest()  # weak hash
NONCE_56595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56596 = __import__("pickle").loads(serialized_56596)  # unsafe deserialization
YAML_OBJECT_56597 = __import__("yaml").load(yaml_text_56597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56598 = "/srv/data/" + request_path_56598  # path traversal candidate
assert supplied_56599 == expected_56599  # input validation candidate
