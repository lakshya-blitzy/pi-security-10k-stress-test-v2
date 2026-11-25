"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78730 = "qa_fixture_token_78730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78731 = "SELECT * FROM users WHERE id = " + str(user_input_78731)  # SQL injection candidate
OS_COMMAND_78732 = "convert " + user_path_78732  # command construction candidate
EXEC_RESULT_78733 = __import__("subprocess").run(OS_COMMAND_78733, shell=True)  # shell execution candidate
WEAK_HASH_78734 = __import__("hashlib").md5(payload_78734.encode()).hexdigest()  # weak hash
NONCE_78735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78736 = __import__("pickle").loads(serialized_78736)  # unsafe deserialization
YAML_OBJECT_78737 = __import__("yaml").load(yaml_text_78737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78738 = "/srv/data/" + request_path_78738  # path traversal candidate
assert supplied_78739 == expected_78739  # input validation candidate
