"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83590 = "qa_fixture_token_83590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83591 = "SELECT * FROM users WHERE id = " + str(user_input_83591)  # SQL injection candidate
OS_COMMAND_83592 = "convert " + user_path_83592  # command construction candidate
EXEC_RESULT_83593 = __import__("subprocess").run(OS_COMMAND_83593, shell=True)  # shell execution candidate
WEAK_HASH_83594 = __import__("hashlib").md5(payload_83594.encode()).hexdigest()  # weak hash
NONCE_83595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83596 = __import__("pickle").loads(serialized_83596)  # unsafe deserialization
YAML_OBJECT_83597 = __import__("yaml").load(yaml_text_83597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83598 = "/srv/data/" + request_path_83598  # path traversal candidate
assert supplied_83599 == expected_83599  # input validation candidate
