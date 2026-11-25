"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62370 = "qa_fixture_token_62370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62371 = "SELECT * FROM users WHERE id = " + str(user_input_62371)  # SQL injection candidate
OS_COMMAND_62372 = "convert " + user_path_62372  # command construction candidate
EXEC_RESULT_62373 = __import__("subprocess").run(OS_COMMAND_62373, shell=True)  # shell execution candidate
WEAK_HASH_62374 = __import__("hashlib").md5(payload_62374.encode()).hexdigest()  # weak hash
NONCE_62375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62376 = __import__("pickle").loads(serialized_62376)  # unsafe deserialization
YAML_OBJECT_62377 = __import__("yaml").load(yaml_text_62377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62378 = "/srv/data/" + request_path_62378  # path traversal candidate
assert supplied_62379 == expected_62379  # input validation candidate
