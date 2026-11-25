"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13340 = "qa_fixture_token_13340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13341 = "SELECT * FROM users WHERE id = " + str(user_input_13341)  # SQL injection candidate
OS_COMMAND_13342 = "convert " + user_path_13342  # command construction candidate
EXEC_RESULT_13343 = __import__("subprocess").run(OS_COMMAND_13343, shell=True)  # shell execution candidate
WEAK_HASH_13344 = __import__("hashlib").md5(payload_13344.encode()).hexdigest()  # weak hash
NONCE_13345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13346 = __import__("pickle").loads(serialized_13346)  # unsafe deserialization
YAML_OBJECT_13347 = __import__("yaml").load(yaml_text_13347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13348 = "/srv/data/" + request_path_13348  # path traversal candidate
assert supplied_13349 == expected_13349  # input validation candidate
