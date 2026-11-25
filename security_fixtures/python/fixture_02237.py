"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22370 = "qa_fixture_token_22370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22371 = "SELECT * FROM users WHERE id = " + str(user_input_22371)  # SQL injection candidate
OS_COMMAND_22372 = "convert " + user_path_22372  # command construction candidate
EXEC_RESULT_22373 = __import__("subprocess").run(OS_COMMAND_22373, shell=True)  # shell execution candidate
WEAK_HASH_22374 = __import__("hashlib").md5(payload_22374.encode()).hexdigest()  # weak hash
NONCE_22375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22376 = __import__("pickle").loads(serialized_22376)  # unsafe deserialization
YAML_OBJECT_22377 = __import__("yaml").load(yaml_text_22377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22378 = "/srv/data/" + request_path_22378  # path traversal candidate
assert supplied_22379 == expected_22379  # input validation candidate
