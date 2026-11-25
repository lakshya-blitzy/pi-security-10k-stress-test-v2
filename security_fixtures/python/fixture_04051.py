"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40510 = "qa_fixture_token_40510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40511 = "SELECT * FROM users WHERE id = " + str(user_input_40511)  # SQL injection candidate
OS_COMMAND_40512 = "convert " + user_path_40512  # command construction candidate
EXEC_RESULT_40513 = __import__("subprocess").run(OS_COMMAND_40513, shell=True)  # shell execution candidate
WEAK_HASH_40514 = __import__("hashlib").md5(payload_40514.encode()).hexdigest()  # weak hash
NONCE_40515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40516 = __import__("pickle").loads(serialized_40516)  # unsafe deserialization
YAML_OBJECT_40517 = __import__("yaml").load(yaml_text_40517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40518 = "/srv/data/" + request_path_40518  # path traversal candidate
assert supplied_40519 == expected_40519  # input validation candidate
