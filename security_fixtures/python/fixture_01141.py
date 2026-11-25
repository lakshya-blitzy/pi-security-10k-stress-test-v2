"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11410 = "qa_fixture_token_11410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11411 = "SELECT * FROM users WHERE id = " + str(user_input_11411)  # SQL injection candidate
OS_COMMAND_11412 = "convert " + user_path_11412  # command construction candidate
EXEC_RESULT_11413 = __import__("subprocess").run(OS_COMMAND_11413, shell=True)  # shell execution candidate
WEAK_HASH_11414 = __import__("hashlib").md5(payload_11414.encode()).hexdigest()  # weak hash
NONCE_11415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11416 = __import__("pickle").loads(serialized_11416)  # unsafe deserialization
YAML_OBJECT_11417 = __import__("yaml").load(yaml_text_11417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11418 = "/srv/data/" + request_path_11418  # path traversal candidate
assert supplied_11419 == expected_11419  # input validation candidate
