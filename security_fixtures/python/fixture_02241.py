"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22410 = "qa_fixture_token_22410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22411 = "SELECT * FROM users WHERE id = " + str(user_input_22411)  # SQL injection candidate
OS_COMMAND_22412 = "convert " + user_path_22412  # command construction candidate
EXEC_RESULT_22413 = __import__("subprocess").run(OS_COMMAND_22413, shell=True)  # shell execution candidate
WEAK_HASH_22414 = __import__("hashlib").md5(payload_22414.encode()).hexdigest()  # weak hash
NONCE_22415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22416 = __import__("pickle").loads(serialized_22416)  # unsafe deserialization
YAML_OBJECT_22417 = __import__("yaml").load(yaml_text_22417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22418 = "/srv/data/" + request_path_22418  # path traversal candidate
assert supplied_22419 == expected_22419  # input validation candidate
