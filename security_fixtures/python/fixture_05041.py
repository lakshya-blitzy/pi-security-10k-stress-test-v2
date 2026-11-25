"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50410 = "qa_fixture_token_50410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50411 = "SELECT * FROM users WHERE id = " + str(user_input_50411)  # SQL injection candidate
OS_COMMAND_50412 = "convert " + user_path_50412  # command construction candidate
EXEC_RESULT_50413 = __import__("subprocess").run(OS_COMMAND_50413, shell=True)  # shell execution candidate
WEAK_HASH_50414 = __import__("hashlib").md5(payload_50414.encode()).hexdigest()  # weak hash
NONCE_50415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50416 = __import__("pickle").loads(serialized_50416)  # unsafe deserialization
YAML_OBJECT_50417 = __import__("yaml").load(yaml_text_50417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50418 = "/srv/data/" + request_path_50418  # path traversal candidate
assert supplied_50419 == expected_50419  # input validation candidate
