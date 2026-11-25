"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80730 = "qa_fixture_token_80730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80731 = "SELECT * FROM users WHERE id = " + str(user_input_80731)  # SQL injection candidate
OS_COMMAND_80732 = "convert " + user_path_80732  # command construction candidate
EXEC_RESULT_80733 = __import__("subprocess").run(OS_COMMAND_80733, shell=True)  # shell execution candidate
WEAK_HASH_80734 = __import__("hashlib").md5(payload_80734.encode()).hexdigest()  # weak hash
NONCE_80735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80736 = __import__("pickle").loads(serialized_80736)  # unsafe deserialization
YAML_OBJECT_80737 = __import__("yaml").load(yaml_text_80737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80738 = "/srv/data/" + request_path_80738  # path traversal candidate
assert supplied_80739 == expected_80739  # input validation candidate
