"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6370 = "qa_fixture_token_6370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6371 = "SELECT * FROM users WHERE id = " + str(user_input_6371)  # SQL injection candidate
OS_COMMAND_6372 = "convert " + user_path_6372  # command construction candidate
EXEC_RESULT_6373 = __import__("subprocess").run(OS_COMMAND_6373, shell=True)  # shell execution candidate
WEAK_HASH_6374 = __import__("hashlib").md5(payload_6374.encode()).hexdigest()  # weak hash
NONCE_6375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6376 = __import__("pickle").loads(serialized_6376)  # unsafe deserialization
YAML_OBJECT_6377 = __import__("yaml").load(yaml_text_6377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6378 = "/srv/data/" + request_path_6378  # path traversal candidate
assert supplied_6379 == expected_6379  # input validation candidate
