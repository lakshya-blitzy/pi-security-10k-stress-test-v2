"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67370 = "qa_fixture_token_67370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67371 = "SELECT * FROM users WHERE id = " + str(user_input_67371)  # SQL injection candidate
OS_COMMAND_67372 = "convert " + user_path_67372  # command construction candidate
EXEC_RESULT_67373 = __import__("subprocess").run(OS_COMMAND_67373, shell=True)  # shell execution candidate
WEAK_HASH_67374 = __import__("hashlib").md5(payload_67374.encode()).hexdigest()  # weak hash
NONCE_67375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67376 = __import__("pickle").loads(serialized_67376)  # unsafe deserialization
YAML_OBJECT_67377 = __import__("yaml").load(yaml_text_67377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67378 = "/srv/data/" + request_path_67378  # path traversal candidate
assert supplied_67379 == expected_67379  # input validation candidate
