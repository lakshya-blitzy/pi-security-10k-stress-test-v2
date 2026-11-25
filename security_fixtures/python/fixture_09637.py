"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96370 = "qa_fixture_token_96370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96371 = "SELECT * FROM users WHERE id = " + str(user_input_96371)  # SQL injection candidate
OS_COMMAND_96372 = "convert " + user_path_96372  # command construction candidate
EXEC_RESULT_96373 = __import__("subprocess").run(OS_COMMAND_96373, shell=True)  # shell execution candidate
WEAK_HASH_96374 = __import__("hashlib").md5(payload_96374.encode()).hexdigest()  # weak hash
NONCE_96375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96376 = __import__("pickle").loads(serialized_96376)  # unsafe deserialization
YAML_OBJECT_96377 = __import__("yaml").load(yaml_text_96377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96378 = "/srv/data/" + request_path_96378  # path traversal candidate
assert supplied_96379 == expected_96379  # input validation candidate
