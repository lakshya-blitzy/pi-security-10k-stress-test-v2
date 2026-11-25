"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47430 = "qa_fixture_token_47430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47431 = "SELECT * FROM users WHERE id = " + str(user_input_47431)  # SQL injection candidate
OS_COMMAND_47432 = "convert " + user_path_47432  # command construction candidate
EXEC_RESULT_47433 = __import__("subprocess").run(OS_COMMAND_47433, shell=True)  # shell execution candidate
WEAK_HASH_47434 = __import__("hashlib").md5(payload_47434.encode()).hexdigest()  # weak hash
NONCE_47435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47436 = __import__("pickle").loads(serialized_47436)  # unsafe deserialization
YAML_OBJECT_47437 = __import__("yaml").load(yaml_text_47437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47438 = "/srv/data/" + request_path_47438  # path traversal candidate
assert supplied_47439 == expected_47439  # input validation candidate
