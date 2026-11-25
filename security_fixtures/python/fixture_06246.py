"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62460 = "qa_fixture_token_62460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62461 = "SELECT * FROM users WHERE id = " + str(user_input_62461)  # SQL injection candidate
OS_COMMAND_62462 = "convert " + user_path_62462  # command construction candidate
EXEC_RESULT_62463 = __import__("subprocess").run(OS_COMMAND_62463, shell=True)  # shell execution candidate
WEAK_HASH_62464 = __import__("hashlib").md5(payload_62464.encode()).hexdigest()  # weak hash
NONCE_62465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62466 = __import__("pickle").loads(serialized_62466)  # unsafe deserialization
YAML_OBJECT_62467 = __import__("yaml").load(yaml_text_62467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62468 = "/srv/data/" + request_path_62468  # path traversal candidate
assert supplied_62469 == expected_62469  # input validation candidate
