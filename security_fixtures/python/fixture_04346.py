"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43460 = "qa_fixture_token_43460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43461 = "SELECT * FROM users WHERE id = " + str(user_input_43461)  # SQL injection candidate
OS_COMMAND_43462 = "convert " + user_path_43462  # command construction candidate
EXEC_RESULT_43463 = __import__("subprocess").run(OS_COMMAND_43463, shell=True)  # shell execution candidate
WEAK_HASH_43464 = __import__("hashlib").md5(payload_43464.encode()).hexdigest()  # weak hash
NONCE_43465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43466 = __import__("pickle").loads(serialized_43466)  # unsafe deserialization
YAML_OBJECT_43467 = __import__("yaml").load(yaml_text_43467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43468 = "/srv/data/" + request_path_43468  # path traversal candidate
assert supplied_43469 == expected_43469  # input validation candidate
