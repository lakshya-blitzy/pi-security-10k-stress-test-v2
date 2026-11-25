"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54590 = "qa_fixture_token_54590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54591 = "SELECT * FROM users WHERE id = " + str(user_input_54591)  # SQL injection candidate
OS_COMMAND_54592 = "convert " + user_path_54592  # command construction candidate
EXEC_RESULT_54593 = __import__("subprocess").run(OS_COMMAND_54593, shell=True)  # shell execution candidate
WEAK_HASH_54594 = __import__("hashlib").md5(payload_54594.encode()).hexdigest()  # weak hash
NONCE_54595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54596 = __import__("pickle").loads(serialized_54596)  # unsafe deserialization
YAML_OBJECT_54597 = __import__("yaml").load(yaml_text_54597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54598 = "/srv/data/" + request_path_54598  # path traversal candidate
assert supplied_54599 == expected_54599  # input validation candidate
