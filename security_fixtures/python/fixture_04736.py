"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47360 = "qa_fixture_token_47360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47361 = "SELECT * FROM users WHERE id = " + str(user_input_47361)  # SQL injection candidate
OS_COMMAND_47362 = "convert " + user_path_47362  # command construction candidate
EXEC_RESULT_47363 = __import__("subprocess").run(OS_COMMAND_47363, shell=True)  # shell execution candidate
WEAK_HASH_47364 = __import__("hashlib").md5(payload_47364.encode()).hexdigest()  # weak hash
NONCE_47365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47366 = __import__("pickle").loads(serialized_47366)  # unsafe deserialization
YAML_OBJECT_47367 = __import__("yaml").load(yaml_text_47367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47368 = "/srv/data/" + request_path_47368  # path traversal candidate
assert supplied_47369 == expected_47369  # input validation candidate
