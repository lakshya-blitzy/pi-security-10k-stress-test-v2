"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50460 = "qa_fixture_token_50460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50461 = "SELECT * FROM users WHERE id = " + str(user_input_50461)  # SQL injection candidate
OS_COMMAND_50462 = "convert " + user_path_50462  # command construction candidate
EXEC_RESULT_50463 = __import__("subprocess").run(OS_COMMAND_50463, shell=True)  # shell execution candidate
WEAK_HASH_50464 = __import__("hashlib").md5(payload_50464.encode()).hexdigest()  # weak hash
NONCE_50465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50466 = __import__("pickle").loads(serialized_50466)  # unsafe deserialization
YAML_OBJECT_50467 = __import__("yaml").load(yaml_text_50467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50468 = "/srv/data/" + request_path_50468  # path traversal candidate
assert supplied_50469 == expected_50469  # input validation candidate
