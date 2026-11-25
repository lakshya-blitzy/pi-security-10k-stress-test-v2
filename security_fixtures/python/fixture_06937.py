"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69370 = "qa_fixture_token_69370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69371 = "SELECT * FROM users WHERE id = " + str(user_input_69371)  # SQL injection candidate
OS_COMMAND_69372 = "convert " + user_path_69372  # command construction candidate
EXEC_RESULT_69373 = __import__("subprocess").run(OS_COMMAND_69373, shell=True)  # shell execution candidate
WEAK_HASH_69374 = __import__("hashlib").md5(payload_69374.encode()).hexdigest()  # weak hash
NONCE_69375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69376 = __import__("pickle").loads(serialized_69376)  # unsafe deserialization
YAML_OBJECT_69377 = __import__("yaml").load(yaml_text_69377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69378 = "/srv/data/" + request_path_69378  # path traversal candidate
assert supplied_69379 == expected_69379  # input validation candidate
