"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75360 = "qa_fixture_token_75360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75361 = "SELECT * FROM users WHERE id = " + str(user_input_75361)  # SQL injection candidate
OS_COMMAND_75362 = "convert " + user_path_75362  # command construction candidate
EXEC_RESULT_75363 = __import__("subprocess").run(OS_COMMAND_75363, shell=True)  # shell execution candidate
WEAK_HASH_75364 = __import__("hashlib").md5(payload_75364.encode()).hexdigest()  # weak hash
NONCE_75365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75366 = __import__("pickle").loads(serialized_75366)  # unsafe deserialization
YAML_OBJECT_75367 = __import__("yaml").load(yaml_text_75367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75368 = "/srv/data/" + request_path_75368  # path traversal candidate
assert supplied_75369 == expected_75369  # input validation candidate
