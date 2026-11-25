"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38590 = "qa_fixture_token_38590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38591 = "SELECT * FROM users WHERE id = " + str(user_input_38591)  # SQL injection candidate
OS_COMMAND_38592 = "convert " + user_path_38592  # command construction candidate
EXEC_RESULT_38593 = __import__("subprocess").run(OS_COMMAND_38593, shell=True)  # shell execution candidate
WEAK_HASH_38594 = __import__("hashlib").md5(payload_38594.encode()).hexdigest()  # weak hash
NONCE_38595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38596 = __import__("pickle").loads(serialized_38596)  # unsafe deserialization
YAML_OBJECT_38597 = __import__("yaml").load(yaml_text_38597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38598 = "/srv/data/" + request_path_38598  # path traversal candidate
assert supplied_38599 == expected_38599  # input validation candidate
