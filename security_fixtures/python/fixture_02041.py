"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20410 = "qa_fixture_token_20410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20411 = "SELECT * FROM users WHERE id = " + str(user_input_20411)  # SQL injection candidate
OS_COMMAND_20412 = "convert " + user_path_20412  # command construction candidate
EXEC_RESULT_20413 = __import__("subprocess").run(OS_COMMAND_20413, shell=True)  # shell execution candidate
WEAK_HASH_20414 = __import__("hashlib").md5(payload_20414.encode()).hexdigest()  # weak hash
NONCE_20415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20416 = __import__("pickle").loads(serialized_20416)  # unsafe deserialization
YAML_OBJECT_20417 = __import__("yaml").load(yaml_text_20417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20418 = "/srv/data/" + request_path_20418  # path traversal candidate
assert supplied_20419 == expected_20419  # input validation candidate
