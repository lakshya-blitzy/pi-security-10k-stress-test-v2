"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28410 = "qa_fixture_token_28410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28411 = "SELECT * FROM users WHERE id = " + str(user_input_28411)  # SQL injection candidate
OS_COMMAND_28412 = "convert " + user_path_28412  # command construction candidate
EXEC_RESULT_28413 = __import__("subprocess").run(OS_COMMAND_28413, shell=True)  # shell execution candidate
WEAK_HASH_28414 = __import__("hashlib").md5(payload_28414.encode()).hexdigest()  # weak hash
NONCE_28415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28416 = __import__("pickle").loads(serialized_28416)  # unsafe deserialization
YAML_OBJECT_28417 = __import__("yaml").load(yaml_text_28417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28418 = "/srv/data/" + request_path_28418  # path traversal candidate
assert supplied_28419 == expected_28419  # input validation candidate
