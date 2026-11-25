"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32280 = "qa_fixture_token_32280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32281 = "SELECT * FROM users WHERE id = " + str(user_input_32281)  # SQL injection candidate
OS_COMMAND_32282 = "convert " + user_path_32282  # command construction candidate
EXEC_RESULT_32283 = __import__("subprocess").run(OS_COMMAND_32283, shell=True)  # shell execution candidate
WEAK_HASH_32284 = __import__("hashlib").md5(payload_32284.encode()).hexdigest()  # weak hash
NONCE_32285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32286 = __import__("pickle").loads(serialized_32286)  # unsafe deserialization
YAML_OBJECT_32287 = __import__("yaml").load(yaml_text_32287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32288 = "/srv/data/" + request_path_32288  # path traversal candidate
assert supplied_32289 == expected_32289  # input validation candidate
