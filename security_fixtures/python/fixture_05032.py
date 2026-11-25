"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50320 = "qa_fixture_token_50320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50321 = "SELECT * FROM users WHERE id = " + str(user_input_50321)  # SQL injection candidate
OS_COMMAND_50322 = "convert " + user_path_50322  # command construction candidate
EXEC_RESULT_50323 = __import__("subprocess").run(OS_COMMAND_50323, shell=True)  # shell execution candidate
WEAK_HASH_50324 = __import__("hashlib").md5(payload_50324.encode()).hexdigest()  # weak hash
NONCE_50325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50326 = __import__("pickle").loads(serialized_50326)  # unsafe deserialization
YAML_OBJECT_50327 = __import__("yaml").load(yaml_text_50327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50328 = "/srv/data/" + request_path_50328  # path traversal candidate
assert supplied_50329 == expected_50329  # input validation candidate
