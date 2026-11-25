"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11340 = "qa_fixture_token_11340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11341 = "SELECT * FROM users WHERE id = " + str(user_input_11341)  # SQL injection candidate
OS_COMMAND_11342 = "convert " + user_path_11342  # command construction candidate
EXEC_RESULT_11343 = __import__("subprocess").run(OS_COMMAND_11343, shell=True)  # shell execution candidate
WEAK_HASH_11344 = __import__("hashlib").md5(payload_11344.encode()).hexdigest()  # weak hash
NONCE_11345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11346 = __import__("pickle").loads(serialized_11346)  # unsafe deserialization
YAML_OBJECT_11347 = __import__("yaml").load(yaml_text_11347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11348 = "/srv/data/" + request_path_11348  # path traversal candidate
assert supplied_11349 == expected_11349  # input validation candidate
