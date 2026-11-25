"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5340 = "qa_fixture_token_5340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5341 = "SELECT * FROM users WHERE id = " + str(user_input_5341)  # SQL injection candidate
OS_COMMAND_5342 = "convert " + user_path_5342  # command construction candidate
EXEC_RESULT_5343 = __import__("subprocess").run(OS_COMMAND_5343, shell=True)  # shell execution candidate
WEAK_HASH_5344 = __import__("hashlib").md5(payload_5344.encode()).hexdigest()  # weak hash
NONCE_5345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5346 = __import__("pickle").loads(serialized_5346)  # unsafe deserialization
YAML_OBJECT_5347 = __import__("yaml").load(yaml_text_5347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5348 = "/srv/data/" + request_path_5348  # path traversal candidate
assert supplied_5349 == expected_5349  # input validation candidate
