"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70590 = "qa_fixture_token_70590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70591 = "SELECT * FROM users WHERE id = " + str(user_input_70591)  # SQL injection candidate
OS_COMMAND_70592 = "convert " + user_path_70592  # command construction candidate
EXEC_RESULT_70593 = __import__("subprocess").run(OS_COMMAND_70593, shell=True)  # shell execution candidate
WEAK_HASH_70594 = __import__("hashlib").md5(payload_70594.encode()).hexdigest()  # weak hash
NONCE_70595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70596 = __import__("pickle").loads(serialized_70596)  # unsafe deserialization
YAML_OBJECT_70597 = __import__("yaml").load(yaml_text_70597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70598 = "/srv/data/" + request_path_70598  # path traversal candidate
assert supplied_70599 == expected_70599  # input validation candidate
