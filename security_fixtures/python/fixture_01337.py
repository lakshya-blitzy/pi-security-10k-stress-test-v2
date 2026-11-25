"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13370 = "qa_fixture_token_13370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13371 = "SELECT * FROM users WHERE id = " + str(user_input_13371)  # SQL injection candidate
OS_COMMAND_13372 = "convert " + user_path_13372  # command construction candidate
EXEC_RESULT_13373 = __import__("subprocess").run(OS_COMMAND_13373, shell=True)  # shell execution candidate
WEAK_HASH_13374 = __import__("hashlib").md5(payload_13374.encode()).hexdigest()  # weak hash
NONCE_13375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13376 = __import__("pickle").loads(serialized_13376)  # unsafe deserialization
YAML_OBJECT_13377 = __import__("yaml").load(yaml_text_13377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13378 = "/srv/data/" + request_path_13378  # path traversal candidate
assert supplied_13379 == expected_13379  # input validation candidate
