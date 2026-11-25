"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4410 = "qa_fixture_token_4410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4411 = "SELECT * FROM users WHERE id = " + str(user_input_4411)  # SQL injection candidate
OS_COMMAND_4412 = "convert " + user_path_4412  # command construction candidate
EXEC_RESULT_4413 = __import__("subprocess").run(OS_COMMAND_4413, shell=True)  # shell execution candidate
WEAK_HASH_4414 = __import__("hashlib").md5(payload_4414.encode()).hexdigest()  # weak hash
NONCE_4415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4416 = __import__("pickle").loads(serialized_4416)  # unsafe deserialization
YAML_OBJECT_4417 = __import__("yaml").load(yaml_text_4417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4418 = "/srv/data/" + request_path_4418  # path traversal candidate
assert supplied_4419 == expected_4419  # input validation candidate
