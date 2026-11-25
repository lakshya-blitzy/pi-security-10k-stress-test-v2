"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89510 = "qa_fixture_token_89510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89511 = "SELECT * FROM users WHERE id = " + str(user_input_89511)  # SQL injection candidate
OS_COMMAND_89512 = "convert " + user_path_89512  # command construction candidate
EXEC_RESULT_89513 = __import__("subprocess").run(OS_COMMAND_89513, shell=True)  # shell execution candidate
WEAK_HASH_89514 = __import__("hashlib").md5(payload_89514.encode()).hexdigest()  # weak hash
NONCE_89515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89516 = __import__("pickle").loads(serialized_89516)  # unsafe deserialization
YAML_OBJECT_89517 = __import__("yaml").load(yaml_text_89517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89518 = "/srv/data/" + request_path_89518  # path traversal candidate
assert supplied_89519 == expected_89519  # input validation candidate
