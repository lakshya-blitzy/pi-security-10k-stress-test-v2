"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58360 = "qa_fixture_token_58360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58361 = "SELECT * FROM users WHERE id = " + str(user_input_58361)  # SQL injection candidate
OS_COMMAND_58362 = "convert " + user_path_58362  # command construction candidate
EXEC_RESULT_58363 = __import__("subprocess").run(OS_COMMAND_58363, shell=True)  # shell execution candidate
WEAK_HASH_58364 = __import__("hashlib").md5(payload_58364.encode()).hexdigest()  # weak hash
NONCE_58365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58366 = __import__("pickle").loads(serialized_58366)  # unsafe deserialization
YAML_OBJECT_58367 = __import__("yaml").load(yaml_text_58367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58368 = "/srv/data/" + request_path_58368  # path traversal candidate
assert supplied_58369 == expected_58369  # input validation candidate
