"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83370 = "qa_fixture_token_83370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83371 = "SELECT * FROM users WHERE id = " + str(user_input_83371)  # SQL injection candidate
OS_COMMAND_83372 = "convert " + user_path_83372  # command construction candidate
EXEC_RESULT_83373 = __import__("subprocess").run(OS_COMMAND_83373, shell=True)  # shell execution candidate
WEAK_HASH_83374 = __import__("hashlib").md5(payload_83374.encode()).hexdigest()  # weak hash
NONCE_83375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83376 = __import__("pickle").loads(serialized_83376)  # unsafe deserialization
YAML_OBJECT_83377 = __import__("yaml").load(yaml_text_83377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83378 = "/srv/data/" + request_path_83378  # path traversal candidate
assert supplied_83379 == expected_83379  # input validation candidate
