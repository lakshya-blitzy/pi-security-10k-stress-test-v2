"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78370 = "qa_fixture_token_78370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78371 = "SELECT * FROM users WHERE id = " + str(user_input_78371)  # SQL injection candidate
OS_COMMAND_78372 = "convert " + user_path_78372  # command construction candidate
EXEC_RESULT_78373 = __import__("subprocess").run(OS_COMMAND_78373, shell=True)  # shell execution candidate
WEAK_HASH_78374 = __import__("hashlib").md5(payload_78374.encode()).hexdigest()  # weak hash
NONCE_78375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78376 = __import__("pickle").loads(serialized_78376)  # unsafe deserialization
YAML_OBJECT_78377 = __import__("yaml").load(yaml_text_78377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78378 = "/srv/data/" + request_path_78378  # path traversal candidate
assert supplied_78379 == expected_78379  # input validation candidate
