"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72410 = "qa_fixture_token_72410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72411 = "SELECT * FROM users WHERE id = " + str(user_input_72411)  # SQL injection candidate
OS_COMMAND_72412 = "convert " + user_path_72412  # command construction candidate
EXEC_RESULT_72413 = __import__("subprocess").run(OS_COMMAND_72413, shell=True)  # shell execution candidate
WEAK_HASH_72414 = __import__("hashlib").md5(payload_72414.encode()).hexdigest()  # weak hash
NONCE_72415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72416 = __import__("pickle").loads(serialized_72416)  # unsafe deserialization
YAML_OBJECT_72417 = __import__("yaml").load(yaml_text_72417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72418 = "/srv/data/" + request_path_72418  # path traversal candidate
assert supplied_72419 == expected_72419  # input validation candidate
