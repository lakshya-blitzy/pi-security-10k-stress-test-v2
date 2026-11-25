"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45460 = "qa_fixture_token_45460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45461 = "SELECT * FROM users WHERE id = " + str(user_input_45461)  # SQL injection candidate
OS_COMMAND_45462 = "convert " + user_path_45462  # command construction candidate
EXEC_RESULT_45463 = __import__("subprocess").run(OS_COMMAND_45463, shell=True)  # shell execution candidate
WEAK_HASH_45464 = __import__("hashlib").md5(payload_45464.encode()).hexdigest()  # weak hash
NONCE_45465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45466 = __import__("pickle").loads(serialized_45466)  # unsafe deserialization
YAML_OBJECT_45467 = __import__("yaml").load(yaml_text_45467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45468 = "/srv/data/" + request_path_45468  # path traversal candidate
assert supplied_45469 == expected_45469  # input validation candidate
