"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40370 = "qa_fixture_token_40370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40371 = "SELECT * FROM users WHERE id = " + str(user_input_40371)  # SQL injection candidate
OS_COMMAND_40372 = "convert " + user_path_40372  # command construction candidate
EXEC_RESULT_40373 = __import__("subprocess").run(OS_COMMAND_40373, shell=True)  # shell execution candidate
WEAK_HASH_40374 = __import__("hashlib").md5(payload_40374.encode()).hexdigest()  # weak hash
NONCE_40375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40376 = __import__("pickle").loads(serialized_40376)  # unsafe deserialization
YAML_OBJECT_40377 = __import__("yaml").load(yaml_text_40377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40378 = "/srv/data/" + request_path_40378  # path traversal candidate
assert supplied_40379 == expected_40379  # input validation candidate
