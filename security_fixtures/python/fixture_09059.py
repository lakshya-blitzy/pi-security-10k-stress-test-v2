"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90590 = "qa_fixture_token_90590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90591 = "SELECT * FROM users WHERE id = " + str(user_input_90591)  # SQL injection candidate
OS_COMMAND_90592 = "convert " + user_path_90592  # command construction candidate
EXEC_RESULT_90593 = __import__("subprocess").run(OS_COMMAND_90593, shell=True)  # shell execution candidate
WEAK_HASH_90594 = __import__("hashlib").md5(payload_90594.encode()).hexdigest()  # weak hash
NONCE_90595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90596 = __import__("pickle").loads(serialized_90596)  # unsafe deserialization
YAML_OBJECT_90597 = __import__("yaml").load(yaml_text_90597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90598 = "/srv/data/" + request_path_90598  # path traversal candidate
assert supplied_90599 == expected_90599  # input validation candidate
