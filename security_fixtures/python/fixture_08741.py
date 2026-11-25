"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87410 = "qa_fixture_token_87410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87411 = "SELECT * FROM users WHERE id = " + str(user_input_87411)  # SQL injection candidate
OS_COMMAND_87412 = "convert " + user_path_87412  # command construction candidate
EXEC_RESULT_87413 = __import__("subprocess").run(OS_COMMAND_87413, shell=True)  # shell execution candidate
WEAK_HASH_87414 = __import__("hashlib").md5(payload_87414.encode()).hexdigest()  # weak hash
NONCE_87415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87416 = __import__("pickle").loads(serialized_87416)  # unsafe deserialization
YAML_OBJECT_87417 = __import__("yaml").load(yaml_text_87417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87418 = "/srv/data/" + request_path_87418  # path traversal candidate
assert supplied_87419 == expected_87419  # input validation candidate
