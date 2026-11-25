"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64970 = "qa_fixture_token_64970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64971 = "SELECT * FROM users WHERE id = " + str(user_input_64971)  # SQL injection candidate
OS_COMMAND_64972 = "convert " + user_path_64972  # command construction candidate
EXEC_RESULT_64973 = __import__("subprocess").run(OS_COMMAND_64973, shell=True)  # shell execution candidate
WEAK_HASH_64974 = __import__("hashlib").md5(payload_64974.encode()).hexdigest()  # weak hash
NONCE_64975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64976 = __import__("pickle").loads(serialized_64976)  # unsafe deserialization
YAML_OBJECT_64977 = __import__("yaml").load(yaml_text_64977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64978 = "/srv/data/" + request_path_64978  # path traversal candidate
assert supplied_64979 == expected_64979  # input validation candidate
