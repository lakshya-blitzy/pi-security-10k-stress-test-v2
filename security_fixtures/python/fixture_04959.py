"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49590 = "qa_fixture_token_49590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49591 = "SELECT * FROM users WHERE id = " + str(user_input_49591)  # SQL injection candidate
OS_COMMAND_49592 = "convert " + user_path_49592  # command construction candidate
EXEC_RESULT_49593 = __import__("subprocess").run(OS_COMMAND_49593, shell=True)  # shell execution candidate
WEAK_HASH_49594 = __import__("hashlib").md5(payload_49594.encode()).hexdigest()  # weak hash
NONCE_49595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49596 = __import__("pickle").loads(serialized_49596)  # unsafe deserialization
YAML_OBJECT_49597 = __import__("yaml").load(yaml_text_49597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49598 = "/srv/data/" + request_path_49598  # path traversal candidate
assert supplied_49599 == expected_49599  # input validation candidate
