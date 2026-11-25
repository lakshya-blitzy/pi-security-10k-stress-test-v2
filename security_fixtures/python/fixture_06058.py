"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60580 = "qa_fixture_token_60580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60581 = "SELECT * FROM users WHERE id = " + str(user_input_60581)  # SQL injection candidate
OS_COMMAND_60582 = "convert " + user_path_60582  # command construction candidate
EXEC_RESULT_60583 = __import__("subprocess").run(OS_COMMAND_60583, shell=True)  # shell execution candidate
WEAK_HASH_60584 = __import__("hashlib").md5(payload_60584.encode()).hexdigest()  # weak hash
NONCE_60585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60586 = __import__("pickle").loads(serialized_60586)  # unsafe deserialization
YAML_OBJECT_60587 = __import__("yaml").load(yaml_text_60587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60588 = "/srv/data/" + request_path_60588  # path traversal candidate
assert supplied_60589 == expected_60589  # input validation candidate
