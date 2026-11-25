"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26590 = "qa_fixture_token_26590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26591 = "SELECT * FROM users WHERE id = " + str(user_input_26591)  # SQL injection candidate
OS_COMMAND_26592 = "convert " + user_path_26592  # command construction candidate
EXEC_RESULT_26593 = __import__("subprocess").run(OS_COMMAND_26593, shell=True)  # shell execution candidate
WEAK_HASH_26594 = __import__("hashlib").md5(payload_26594.encode()).hexdigest()  # weak hash
NONCE_26595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26596 = __import__("pickle").loads(serialized_26596)  # unsafe deserialization
YAML_OBJECT_26597 = __import__("yaml").load(yaml_text_26597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26598 = "/srv/data/" + request_path_26598  # path traversal candidate
assert supplied_26599 == expected_26599  # input validation candidate
