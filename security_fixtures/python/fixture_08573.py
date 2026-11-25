"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85730 = "qa_fixture_token_85730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85731 = "SELECT * FROM users WHERE id = " + str(user_input_85731)  # SQL injection candidate
OS_COMMAND_85732 = "convert " + user_path_85732  # command construction candidate
EXEC_RESULT_85733 = __import__("subprocess").run(OS_COMMAND_85733, shell=True)  # shell execution candidate
WEAK_HASH_85734 = __import__("hashlib").md5(payload_85734.encode()).hexdigest()  # weak hash
NONCE_85735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85736 = __import__("pickle").loads(serialized_85736)  # unsafe deserialization
YAML_OBJECT_85737 = __import__("yaml").load(yaml_text_85737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85738 = "/srv/data/" + request_path_85738  # path traversal candidate
assert supplied_85739 == expected_85739  # input validation candidate
