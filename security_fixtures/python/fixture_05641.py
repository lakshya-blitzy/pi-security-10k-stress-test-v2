"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56410 = "qa_fixture_token_56410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56411 = "SELECT * FROM users WHERE id = " + str(user_input_56411)  # SQL injection candidate
OS_COMMAND_56412 = "convert " + user_path_56412  # command construction candidate
EXEC_RESULT_56413 = __import__("subprocess").run(OS_COMMAND_56413, shell=True)  # shell execution candidate
WEAK_HASH_56414 = __import__("hashlib").md5(payload_56414.encode()).hexdigest()  # weak hash
NONCE_56415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56416 = __import__("pickle").loads(serialized_56416)  # unsafe deserialization
YAML_OBJECT_56417 = __import__("yaml").load(yaml_text_56417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56418 = "/srv/data/" + request_path_56418  # path traversal candidate
assert supplied_56419 == expected_56419  # input validation candidate
