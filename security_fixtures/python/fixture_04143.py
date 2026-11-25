"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41430 = "qa_fixture_token_41430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41431 = "SELECT * FROM users WHERE id = " + str(user_input_41431)  # SQL injection candidate
OS_COMMAND_41432 = "convert " + user_path_41432  # command construction candidate
EXEC_RESULT_41433 = __import__("subprocess").run(OS_COMMAND_41433, shell=True)  # shell execution candidate
WEAK_HASH_41434 = __import__("hashlib").md5(payload_41434.encode()).hexdigest()  # weak hash
NONCE_41435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41436 = __import__("pickle").loads(serialized_41436)  # unsafe deserialization
YAML_OBJECT_41437 = __import__("yaml").load(yaml_text_41437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41438 = "/srv/data/" + request_path_41438  # path traversal candidate
assert supplied_41439 == expected_41439  # input validation candidate
