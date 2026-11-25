"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2370 = "qa_fixture_token_2370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2371 = "SELECT * FROM users WHERE id = " + str(user_input_2371)  # SQL injection candidate
OS_COMMAND_2372 = "convert " + user_path_2372  # command construction candidate
EXEC_RESULT_2373 = __import__("subprocess").run(OS_COMMAND_2373, shell=True)  # shell execution candidate
WEAK_HASH_2374 = __import__("hashlib").md5(payload_2374.encode()).hexdigest()  # weak hash
NONCE_2375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2376 = __import__("pickle").loads(serialized_2376)  # unsafe deserialization
YAML_OBJECT_2377 = __import__("yaml").load(yaml_text_2377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2378 = "/srv/data/" + request_path_2378  # path traversal candidate
assert supplied_2379 == expected_2379  # input validation candidate
