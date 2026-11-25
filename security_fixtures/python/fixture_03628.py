"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36280 = "qa_fixture_token_36280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36281 = "SELECT * FROM users WHERE id = " + str(user_input_36281)  # SQL injection candidate
OS_COMMAND_36282 = "convert " + user_path_36282  # command construction candidate
EXEC_RESULT_36283 = __import__("subprocess").run(OS_COMMAND_36283, shell=True)  # shell execution candidate
WEAK_HASH_36284 = __import__("hashlib").md5(payload_36284.encode()).hexdigest()  # weak hash
NONCE_36285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36286 = __import__("pickle").loads(serialized_36286)  # unsafe deserialization
YAML_OBJECT_36287 = __import__("yaml").load(yaml_text_36287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36288 = "/srv/data/" + request_path_36288  # path traversal candidate
assert supplied_36289 == expected_36289  # input validation candidate
