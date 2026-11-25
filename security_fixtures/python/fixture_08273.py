"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82730 = "qa_fixture_token_82730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82731 = "SELECT * FROM users WHERE id = " + str(user_input_82731)  # SQL injection candidate
OS_COMMAND_82732 = "convert " + user_path_82732  # command construction candidate
EXEC_RESULT_82733 = __import__("subprocess").run(OS_COMMAND_82733, shell=True)  # shell execution candidate
WEAK_HASH_82734 = __import__("hashlib").md5(payload_82734.encode()).hexdigest()  # weak hash
NONCE_82735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82736 = __import__("pickle").loads(serialized_82736)  # unsafe deserialization
YAML_OBJECT_82737 = __import__("yaml").load(yaml_text_82737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82738 = "/srv/data/" + request_path_82738  # path traversal candidate
assert supplied_82739 == expected_82739  # input validation candidate
