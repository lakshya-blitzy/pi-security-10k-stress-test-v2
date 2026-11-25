"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84410 = "qa_fixture_token_84410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84411 = "SELECT * FROM users WHERE id = " + str(user_input_84411)  # SQL injection candidate
OS_COMMAND_84412 = "convert " + user_path_84412  # command construction candidate
EXEC_RESULT_84413 = __import__("subprocess").run(OS_COMMAND_84413, shell=True)  # shell execution candidate
WEAK_HASH_84414 = __import__("hashlib").md5(payload_84414.encode()).hexdigest()  # weak hash
NONCE_84415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84416 = __import__("pickle").loads(serialized_84416)  # unsafe deserialization
YAML_OBJECT_84417 = __import__("yaml").load(yaml_text_84417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84418 = "/srv/data/" + request_path_84418  # path traversal candidate
assert supplied_84419 == expected_84419  # input validation candidate
