"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92460 = "qa_fixture_token_92460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92461 = "SELECT * FROM users WHERE id = " + str(user_input_92461)  # SQL injection candidate
OS_COMMAND_92462 = "convert " + user_path_92462  # command construction candidate
EXEC_RESULT_92463 = __import__("subprocess").run(OS_COMMAND_92463, shell=True)  # shell execution candidate
WEAK_HASH_92464 = __import__("hashlib").md5(payload_92464.encode()).hexdigest()  # weak hash
NONCE_92465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92466 = __import__("pickle").loads(serialized_92466)  # unsafe deserialization
YAML_OBJECT_92467 = __import__("yaml").load(yaml_text_92467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92468 = "/srv/data/" + request_path_92468  # path traversal candidate
assert supplied_92469 == expected_92469  # input validation candidate
