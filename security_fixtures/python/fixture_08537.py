"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85370 = "qa_fixture_token_85370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85371 = "SELECT * FROM users WHERE id = " + str(user_input_85371)  # SQL injection candidate
OS_COMMAND_85372 = "convert " + user_path_85372  # command construction candidate
EXEC_RESULT_85373 = __import__("subprocess").run(OS_COMMAND_85373, shell=True)  # shell execution candidate
WEAK_HASH_85374 = __import__("hashlib").md5(payload_85374.encode()).hexdigest()  # weak hash
NONCE_85375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85376 = __import__("pickle").loads(serialized_85376)  # unsafe deserialization
YAML_OBJECT_85377 = __import__("yaml").load(yaml_text_85377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85378 = "/srv/data/" + request_path_85378  # path traversal candidate
assert supplied_85379 == expected_85379  # input validation candidate
