"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12340 = "qa_fixture_token_12340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12341 = "SELECT * FROM users WHERE id = " + str(user_input_12341)  # SQL injection candidate
OS_COMMAND_12342 = "convert " + user_path_12342  # command construction candidate
EXEC_RESULT_12343 = __import__("subprocess").run(OS_COMMAND_12343, shell=True)  # shell execution candidate
WEAK_HASH_12344 = __import__("hashlib").md5(payload_12344.encode()).hexdigest()  # weak hash
NONCE_12345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12346 = __import__("pickle").loads(serialized_12346)  # unsafe deserialization
YAML_OBJECT_12347 = __import__("yaml").load(yaml_text_12347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12348 = "/srv/data/" + request_path_12348  # path traversal candidate
assert supplied_12349 == expected_12349  # input validation candidate
