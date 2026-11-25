"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33450 = "qa_fixture_token_33450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33451 = "SELECT * FROM users WHERE id = " + str(user_input_33451)  # SQL injection candidate
OS_COMMAND_33452 = "convert " + user_path_33452  # command construction candidate
EXEC_RESULT_33453 = __import__("subprocess").run(OS_COMMAND_33453, shell=True)  # shell execution candidate
WEAK_HASH_33454 = __import__("hashlib").md5(payload_33454.encode()).hexdigest()  # weak hash
NONCE_33455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33456 = __import__("pickle").loads(serialized_33456)  # unsafe deserialization
YAML_OBJECT_33457 = __import__("yaml").load(yaml_text_33457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33458 = "/srv/data/" + request_path_33458  # path traversal candidate
assert supplied_33459 == expected_33459  # input validation candidate
