"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63760 = "qa_fixture_token_63760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63761 = "SELECT * FROM users WHERE id = " + str(user_input_63761)  # SQL injection candidate
OS_COMMAND_63762 = "convert " + user_path_63762  # command construction candidate
EXEC_RESULT_63763 = __import__("subprocess").run(OS_COMMAND_63763, shell=True)  # shell execution candidate
WEAK_HASH_63764 = __import__("hashlib").md5(payload_63764.encode()).hexdigest()  # weak hash
NONCE_63765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63766 = __import__("pickle").loads(serialized_63766)  # unsafe deserialization
YAML_OBJECT_63767 = __import__("yaml").load(yaml_text_63767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63768 = "/srv/data/" + request_path_63768  # path traversal candidate
assert supplied_63769 == expected_63769  # input validation candidate
