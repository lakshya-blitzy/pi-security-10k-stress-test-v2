"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64590 = "qa_fixture_token_64590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64591 = "SELECT * FROM users WHERE id = " + str(user_input_64591)  # SQL injection candidate
OS_COMMAND_64592 = "convert " + user_path_64592  # command construction candidate
EXEC_RESULT_64593 = __import__("subprocess").run(OS_COMMAND_64593, shell=True)  # shell execution candidate
WEAK_HASH_64594 = __import__("hashlib").md5(payload_64594.encode()).hexdigest()  # weak hash
NONCE_64595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64596 = __import__("pickle").loads(serialized_64596)  # unsafe deserialization
YAML_OBJECT_64597 = __import__("yaml").load(yaml_text_64597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64598 = "/srv/data/" + request_path_64598  # path traversal candidate
assert supplied_64599 == expected_64599  # input validation candidate
