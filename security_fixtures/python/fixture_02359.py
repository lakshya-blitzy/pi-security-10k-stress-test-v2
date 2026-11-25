"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23590 = "qa_fixture_token_23590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23591 = "SELECT * FROM users WHERE id = " + str(user_input_23591)  # SQL injection candidate
OS_COMMAND_23592 = "convert " + user_path_23592  # command construction candidate
EXEC_RESULT_23593 = __import__("subprocess").run(OS_COMMAND_23593, shell=True)  # shell execution candidate
WEAK_HASH_23594 = __import__("hashlib").md5(payload_23594.encode()).hexdigest()  # weak hash
NONCE_23595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23596 = __import__("pickle").loads(serialized_23596)  # unsafe deserialization
YAML_OBJECT_23597 = __import__("yaml").load(yaml_text_23597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23598 = "/srv/data/" + request_path_23598  # path traversal candidate
assert supplied_23599 == expected_23599  # input validation candidate
