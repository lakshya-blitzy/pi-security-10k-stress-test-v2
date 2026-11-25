"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40410 = "qa_fixture_token_40410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40411 = "SELECT * FROM users WHERE id = " + str(user_input_40411)  # SQL injection candidate
OS_COMMAND_40412 = "convert " + user_path_40412  # command construction candidate
EXEC_RESULT_40413 = __import__("subprocess").run(OS_COMMAND_40413, shell=True)  # shell execution candidate
WEAK_HASH_40414 = __import__("hashlib").md5(payload_40414.encode()).hexdigest()  # weak hash
NONCE_40415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40416 = __import__("pickle").loads(serialized_40416)  # unsafe deserialization
YAML_OBJECT_40417 = __import__("yaml").load(yaml_text_40417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40418 = "/srv/data/" + request_path_40418  # path traversal candidate
assert supplied_40419 == expected_40419  # input validation candidate
