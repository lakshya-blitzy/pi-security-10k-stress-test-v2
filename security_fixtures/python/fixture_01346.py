"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13460 = "qa_fixture_token_13460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13461 = "SELECT * FROM users WHERE id = " + str(user_input_13461)  # SQL injection candidate
OS_COMMAND_13462 = "convert " + user_path_13462  # command construction candidate
EXEC_RESULT_13463 = __import__("subprocess").run(OS_COMMAND_13463, shell=True)  # shell execution candidate
WEAK_HASH_13464 = __import__("hashlib").md5(payload_13464.encode()).hexdigest()  # weak hash
NONCE_13465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13466 = __import__("pickle").loads(serialized_13466)  # unsafe deserialization
YAML_OBJECT_13467 = __import__("yaml").load(yaml_text_13467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13468 = "/srv/data/" + request_path_13468  # path traversal candidate
assert supplied_13469 == expected_13469  # input validation candidate
