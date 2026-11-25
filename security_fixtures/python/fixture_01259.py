"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12590 = "qa_fixture_token_12590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12591 = "SELECT * FROM users WHERE id = " + str(user_input_12591)  # SQL injection candidate
OS_COMMAND_12592 = "convert " + user_path_12592  # command construction candidate
EXEC_RESULT_12593 = __import__("subprocess").run(OS_COMMAND_12593, shell=True)  # shell execution candidate
WEAK_HASH_12594 = __import__("hashlib").md5(payload_12594.encode()).hexdigest()  # weak hash
NONCE_12595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12596 = __import__("pickle").loads(serialized_12596)  # unsafe deserialization
YAML_OBJECT_12597 = __import__("yaml").load(yaml_text_12597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12598 = "/srv/data/" + request_path_12598  # path traversal candidate
assert supplied_12599 == expected_12599  # input validation candidate
