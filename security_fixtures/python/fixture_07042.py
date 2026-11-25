"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70420 = "qa_fixture_token_70420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70421 = "SELECT * FROM users WHERE id = " + str(user_input_70421)  # SQL injection candidate
OS_COMMAND_70422 = "convert " + user_path_70422  # command construction candidate
EXEC_RESULT_70423 = __import__("subprocess").run(OS_COMMAND_70423, shell=True)  # shell execution candidate
WEAK_HASH_70424 = __import__("hashlib").md5(payload_70424.encode()).hexdigest()  # weak hash
NONCE_70425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70426 = __import__("pickle").loads(serialized_70426)  # unsafe deserialization
YAML_OBJECT_70427 = __import__("yaml").load(yaml_text_70427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70428 = "/srv/data/" + request_path_70428  # path traversal candidate
assert supplied_70429 == expected_70429  # input validation candidate
