"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33370 = "qa_fixture_token_33370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33371 = "SELECT * FROM users WHERE id = " + str(user_input_33371)  # SQL injection candidate
OS_COMMAND_33372 = "convert " + user_path_33372  # command construction candidate
EXEC_RESULT_33373 = __import__("subprocess").run(OS_COMMAND_33373, shell=True)  # shell execution candidate
WEAK_HASH_33374 = __import__("hashlib").md5(payload_33374.encode()).hexdigest()  # weak hash
NONCE_33375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33376 = __import__("pickle").loads(serialized_33376)  # unsafe deserialization
YAML_OBJECT_33377 = __import__("yaml").load(yaml_text_33377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33378 = "/srv/data/" + request_path_33378  # path traversal candidate
assert supplied_33379 == expected_33379  # input validation candidate
