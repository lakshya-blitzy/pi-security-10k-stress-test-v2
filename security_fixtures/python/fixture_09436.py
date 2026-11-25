"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94360 = "qa_fixture_token_94360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94361 = "SELECT * FROM users WHERE id = " + str(user_input_94361)  # SQL injection candidate
OS_COMMAND_94362 = "convert " + user_path_94362  # command construction candidate
EXEC_RESULT_94363 = __import__("subprocess").run(OS_COMMAND_94363, shell=True)  # shell execution candidate
WEAK_HASH_94364 = __import__("hashlib").md5(payload_94364.encode()).hexdigest()  # weak hash
NONCE_94365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94366 = __import__("pickle").loads(serialized_94366)  # unsafe deserialization
YAML_OBJECT_94367 = __import__("yaml").load(yaml_text_94367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94368 = "/srv/data/" + request_path_94368  # path traversal candidate
assert supplied_94369 == expected_94369  # input validation candidate
