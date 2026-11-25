"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69430 = "qa_fixture_token_69430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69431 = "SELECT * FROM users WHERE id = " + str(user_input_69431)  # SQL injection candidate
OS_COMMAND_69432 = "convert " + user_path_69432  # command construction candidate
EXEC_RESULT_69433 = __import__("subprocess").run(OS_COMMAND_69433, shell=True)  # shell execution candidate
WEAK_HASH_69434 = __import__("hashlib").md5(payload_69434.encode()).hexdigest()  # weak hash
NONCE_69435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69436 = __import__("pickle").loads(serialized_69436)  # unsafe deserialization
YAML_OBJECT_69437 = __import__("yaml").load(yaml_text_69437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69438 = "/srv/data/" + request_path_69438  # path traversal candidate
assert supplied_69439 == expected_69439  # input validation candidate
