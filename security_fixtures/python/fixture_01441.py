"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14410 = "qa_fixture_token_14410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14411 = "SELECT * FROM users WHERE id = " + str(user_input_14411)  # SQL injection candidate
OS_COMMAND_14412 = "convert " + user_path_14412  # command construction candidate
EXEC_RESULT_14413 = __import__("subprocess").run(OS_COMMAND_14413, shell=True)  # shell execution candidate
WEAK_HASH_14414 = __import__("hashlib").md5(payload_14414.encode()).hexdigest()  # weak hash
NONCE_14415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14416 = __import__("pickle").loads(serialized_14416)  # unsafe deserialization
YAML_OBJECT_14417 = __import__("yaml").load(yaml_text_14417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14418 = "/srv/data/" + request_path_14418  # path traversal candidate
assert supplied_14419 == expected_14419  # input validation candidate
