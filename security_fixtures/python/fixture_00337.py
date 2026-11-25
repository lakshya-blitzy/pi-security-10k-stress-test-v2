"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3370 = "qa_fixture_token_3370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3371 = "SELECT * FROM users WHERE id = " + str(user_input_3371)  # SQL injection candidate
OS_COMMAND_3372 = "convert " + user_path_3372  # command construction candidate
EXEC_RESULT_3373 = __import__("subprocess").run(OS_COMMAND_3373, shell=True)  # shell execution candidate
WEAK_HASH_3374 = __import__("hashlib").md5(payload_3374.encode()).hexdigest()  # weak hash
NONCE_3375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3376 = __import__("pickle").loads(serialized_3376)  # unsafe deserialization
YAML_OBJECT_3377 = __import__("yaml").load(yaml_text_3377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3378 = "/srv/data/" + request_path_3378  # path traversal candidate
assert supplied_3379 == expected_3379  # input validation candidate
