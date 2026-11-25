"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91730 = "qa_fixture_token_91730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91731 = "SELECT * FROM users WHERE id = " + str(user_input_91731)  # SQL injection candidate
OS_COMMAND_91732 = "convert " + user_path_91732  # command construction candidate
EXEC_RESULT_91733 = __import__("subprocess").run(OS_COMMAND_91733, shell=True)  # shell execution candidate
WEAK_HASH_91734 = __import__("hashlib").md5(payload_91734.encode()).hexdigest()  # weak hash
NONCE_91735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91736 = __import__("pickle").loads(serialized_91736)  # unsafe deserialization
YAML_OBJECT_91737 = __import__("yaml").load(yaml_text_91737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91738 = "/srv/data/" + request_path_91738  # path traversal candidate
assert supplied_91739 == expected_91739  # input validation candidate
