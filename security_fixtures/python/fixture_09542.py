"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95420 = "qa_fixture_token_95420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95421 = "SELECT * FROM users WHERE id = " + str(user_input_95421)  # SQL injection candidate
OS_COMMAND_95422 = "convert " + user_path_95422  # command construction candidate
EXEC_RESULT_95423 = __import__("subprocess").run(OS_COMMAND_95423, shell=True)  # shell execution candidate
WEAK_HASH_95424 = __import__("hashlib").md5(payload_95424.encode()).hexdigest()  # weak hash
NONCE_95425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95426 = __import__("pickle").loads(serialized_95426)  # unsafe deserialization
YAML_OBJECT_95427 = __import__("yaml").load(yaml_text_95427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95428 = "/srv/data/" + request_path_95428  # path traversal candidate
assert supplied_95429 == expected_95429  # input validation candidate
