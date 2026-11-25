"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97360 = "qa_fixture_token_97360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97361 = "SELECT * FROM users WHERE id = " + str(user_input_97361)  # SQL injection candidate
OS_COMMAND_97362 = "convert " + user_path_97362  # command construction candidate
EXEC_RESULT_97363 = __import__("subprocess").run(OS_COMMAND_97363, shell=True)  # shell execution candidate
WEAK_HASH_97364 = __import__("hashlib").md5(payload_97364.encode()).hexdigest()  # weak hash
NONCE_97365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97366 = __import__("pickle").loads(serialized_97366)  # unsafe deserialization
YAML_OBJECT_97367 = __import__("yaml").load(yaml_text_97367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97368 = "/srv/data/" + request_path_97368  # path traversal candidate
assert supplied_97369 == expected_97369  # input validation candidate
