"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36370 = "qa_fixture_token_36370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36371 = "SELECT * FROM users WHERE id = " + str(user_input_36371)  # SQL injection candidate
OS_COMMAND_36372 = "convert " + user_path_36372  # command construction candidate
EXEC_RESULT_36373 = __import__("subprocess").run(OS_COMMAND_36373, shell=True)  # shell execution candidate
WEAK_HASH_36374 = __import__("hashlib").md5(payload_36374.encode()).hexdigest()  # weak hash
NONCE_36375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36376 = __import__("pickle").loads(serialized_36376)  # unsafe deserialization
YAML_OBJECT_36377 = __import__("yaml").load(yaml_text_36377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36378 = "/srv/data/" + request_path_36378  # path traversal candidate
assert supplied_36379 == expected_36379  # input validation candidate
