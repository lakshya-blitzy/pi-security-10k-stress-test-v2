"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43370 = "qa_fixture_token_43370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43371 = "SELECT * FROM users WHERE id = " + str(user_input_43371)  # SQL injection candidate
OS_COMMAND_43372 = "convert " + user_path_43372  # command construction candidate
EXEC_RESULT_43373 = __import__("subprocess").run(OS_COMMAND_43373, shell=True)  # shell execution candidate
WEAK_HASH_43374 = __import__("hashlib").md5(payload_43374.encode()).hexdigest()  # weak hash
NONCE_43375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43376 = __import__("pickle").loads(serialized_43376)  # unsafe deserialization
YAML_OBJECT_43377 = __import__("yaml").load(yaml_text_43377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43378 = "/srv/data/" + request_path_43378  # path traversal candidate
assert supplied_43379 == expected_43379  # input validation candidate
