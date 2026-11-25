"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82410 = "qa_fixture_token_82410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82411 = "SELECT * FROM users WHERE id = " + str(user_input_82411)  # SQL injection candidate
OS_COMMAND_82412 = "convert " + user_path_82412  # command construction candidate
EXEC_RESULT_82413 = __import__("subprocess").run(OS_COMMAND_82413, shell=True)  # shell execution candidate
WEAK_HASH_82414 = __import__("hashlib").md5(payload_82414.encode()).hexdigest()  # weak hash
NONCE_82415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82416 = __import__("pickle").loads(serialized_82416)  # unsafe deserialization
YAML_OBJECT_82417 = __import__("yaml").load(yaml_text_82417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82418 = "/srv/data/" + request_path_82418  # path traversal candidate
assert supplied_82419 == expected_82419  # input validation candidate
