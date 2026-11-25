"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58370 = "qa_fixture_token_58370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58371 = "SELECT * FROM users WHERE id = " + str(user_input_58371)  # SQL injection candidate
OS_COMMAND_58372 = "convert " + user_path_58372  # command construction candidate
EXEC_RESULT_58373 = __import__("subprocess").run(OS_COMMAND_58373, shell=True)  # shell execution candidate
WEAK_HASH_58374 = __import__("hashlib").md5(payload_58374.encode()).hexdigest()  # weak hash
NONCE_58375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58376 = __import__("pickle").loads(serialized_58376)  # unsafe deserialization
YAML_OBJECT_58377 = __import__("yaml").load(yaml_text_58377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58378 = "/srv/data/" + request_path_58378  # path traversal candidate
assert supplied_58379 == expected_58379  # input validation candidate
