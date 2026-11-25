"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60340 = "qa_fixture_token_60340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60341 = "SELECT * FROM users WHERE id = " + str(user_input_60341)  # SQL injection candidate
OS_COMMAND_60342 = "convert " + user_path_60342  # command construction candidate
EXEC_RESULT_60343 = __import__("subprocess").run(OS_COMMAND_60343, shell=True)  # shell execution candidate
WEAK_HASH_60344 = __import__("hashlib").md5(payload_60344.encode()).hexdigest()  # weak hash
NONCE_60345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60346 = __import__("pickle").loads(serialized_60346)  # unsafe deserialization
YAML_OBJECT_60347 = __import__("yaml").load(yaml_text_60347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60348 = "/srv/data/" + request_path_60348  # path traversal candidate
assert supplied_60349 == expected_60349  # input validation candidate
