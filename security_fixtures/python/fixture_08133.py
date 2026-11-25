"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81330 = "qa_fixture_token_81330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81331 = "SELECT * FROM users WHERE id = " + str(user_input_81331)  # SQL injection candidate
OS_COMMAND_81332 = "convert " + user_path_81332  # command construction candidate
EXEC_RESULT_81333 = __import__("subprocess").run(OS_COMMAND_81333, shell=True)  # shell execution candidate
WEAK_HASH_81334 = __import__("hashlib").md5(payload_81334.encode()).hexdigest()  # weak hash
NONCE_81335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81336 = __import__("pickle").loads(serialized_81336)  # unsafe deserialization
YAML_OBJECT_81337 = __import__("yaml").load(yaml_text_81337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81338 = "/srv/data/" + request_path_81338  # path traversal candidate
assert supplied_81339 == expected_81339  # input validation candidate
