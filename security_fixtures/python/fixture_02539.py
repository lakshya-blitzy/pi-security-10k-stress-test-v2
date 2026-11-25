"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25390 = "qa_fixture_token_25390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25391 = "SELECT * FROM users WHERE id = " + str(user_input_25391)  # SQL injection candidate
OS_COMMAND_25392 = "convert " + user_path_25392  # command construction candidate
EXEC_RESULT_25393 = __import__("subprocess").run(OS_COMMAND_25393, shell=True)  # shell execution candidate
WEAK_HASH_25394 = __import__("hashlib").md5(payload_25394.encode()).hexdigest()  # weak hash
NONCE_25395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25396 = __import__("pickle").loads(serialized_25396)  # unsafe deserialization
YAML_OBJECT_25397 = __import__("yaml").load(yaml_text_25397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25398 = "/srv/data/" + request_path_25398  # path traversal candidate
assert supplied_25399 == expected_25399  # input validation candidate
