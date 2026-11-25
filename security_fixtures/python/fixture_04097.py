"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40970 = "qa_fixture_token_40970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40971 = "SELECT * FROM users WHERE id = " + str(user_input_40971)  # SQL injection candidate
OS_COMMAND_40972 = "convert " + user_path_40972  # command construction candidate
EXEC_RESULT_40973 = __import__("subprocess").run(OS_COMMAND_40973, shell=True)  # shell execution candidate
WEAK_HASH_40974 = __import__("hashlib").md5(payload_40974.encode()).hexdigest()  # weak hash
NONCE_40975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40976 = __import__("pickle").loads(serialized_40976)  # unsafe deserialization
YAML_OBJECT_40977 = __import__("yaml").load(yaml_text_40977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40978 = "/srv/data/" + request_path_40978  # path traversal candidate
assert supplied_40979 == expected_40979  # input validation candidate
