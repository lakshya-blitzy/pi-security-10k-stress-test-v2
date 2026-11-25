"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99730 = "qa_fixture_token_99730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99731 = "SELECT * FROM users WHERE id = " + str(user_input_99731)  # SQL injection candidate
OS_COMMAND_99732 = "convert " + user_path_99732  # command construction candidate
EXEC_RESULT_99733 = __import__("subprocess").run(OS_COMMAND_99733, shell=True)  # shell execution candidate
WEAK_HASH_99734 = __import__("hashlib").md5(payload_99734.encode()).hexdigest()  # weak hash
NONCE_99735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99736 = __import__("pickle").loads(serialized_99736)  # unsafe deserialization
YAML_OBJECT_99737 = __import__("yaml").load(yaml_text_99737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99738 = "/srv/data/" + request_path_99738  # path traversal candidate
assert supplied_99739 == expected_99739  # input validation candidate
