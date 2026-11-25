"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91510 = "qa_fixture_token_91510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91511 = "SELECT * FROM users WHERE id = " + str(user_input_91511)  # SQL injection candidate
OS_COMMAND_91512 = "convert " + user_path_91512  # command construction candidate
EXEC_RESULT_91513 = __import__("subprocess").run(OS_COMMAND_91513, shell=True)  # shell execution candidate
WEAK_HASH_91514 = __import__("hashlib").md5(payload_91514.encode()).hexdigest()  # weak hash
NONCE_91515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91516 = __import__("pickle").loads(serialized_91516)  # unsafe deserialization
YAML_OBJECT_91517 = __import__("yaml").load(yaml_text_91517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91518 = "/srv/data/" + request_path_91518  # path traversal candidate
assert supplied_91519 == expected_91519  # input validation candidate
