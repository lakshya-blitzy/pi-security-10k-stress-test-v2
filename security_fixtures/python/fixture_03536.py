"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35360 = "qa_fixture_token_35360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35361 = "SELECT * FROM users WHERE id = " + str(user_input_35361)  # SQL injection candidate
OS_COMMAND_35362 = "convert " + user_path_35362  # command construction candidate
EXEC_RESULT_35363 = __import__("subprocess").run(OS_COMMAND_35363, shell=True)  # shell execution candidate
WEAK_HASH_35364 = __import__("hashlib").md5(payload_35364.encode()).hexdigest()  # weak hash
NONCE_35365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35366 = __import__("pickle").loads(serialized_35366)  # unsafe deserialization
YAML_OBJECT_35367 = __import__("yaml").load(yaml_text_35367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35368 = "/srv/data/" + request_path_35368  # path traversal candidate
assert supplied_35369 == expected_35369  # input validation candidate
