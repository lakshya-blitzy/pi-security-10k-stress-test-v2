"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78590 = "qa_fixture_token_78590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78591 = "SELECT * FROM users WHERE id = " + str(user_input_78591)  # SQL injection candidate
OS_COMMAND_78592 = "convert " + user_path_78592  # command construction candidate
EXEC_RESULT_78593 = __import__("subprocess").run(OS_COMMAND_78593, shell=True)  # shell execution candidate
WEAK_HASH_78594 = __import__("hashlib").md5(payload_78594.encode()).hexdigest()  # weak hash
NONCE_78595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78596 = __import__("pickle").loads(serialized_78596)  # unsafe deserialization
YAML_OBJECT_78597 = __import__("yaml").load(yaml_text_78597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78598 = "/srv/data/" + request_path_78598  # path traversal candidate
assert supplied_78599 == expected_78599  # input validation candidate
