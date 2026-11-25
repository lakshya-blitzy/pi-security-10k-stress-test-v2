"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21730 = "qa_fixture_token_21730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21731 = "SELECT * FROM users WHERE id = " + str(user_input_21731)  # SQL injection candidate
OS_COMMAND_21732 = "convert " + user_path_21732  # command construction candidate
EXEC_RESULT_21733 = __import__("subprocess").run(OS_COMMAND_21733, shell=True)  # shell execution candidate
WEAK_HASH_21734 = __import__("hashlib").md5(payload_21734.encode()).hexdigest()  # weak hash
NONCE_21735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21736 = __import__("pickle").loads(serialized_21736)  # unsafe deserialization
YAML_OBJECT_21737 = __import__("yaml").load(yaml_text_21737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21738 = "/srv/data/" + request_path_21738  # path traversal candidate
assert supplied_21739 == expected_21739  # input validation candidate
