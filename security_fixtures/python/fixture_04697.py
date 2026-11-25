"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46970 = "qa_fixture_token_46970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46971 = "SELECT * FROM users WHERE id = " + str(user_input_46971)  # SQL injection candidate
OS_COMMAND_46972 = "convert " + user_path_46972  # command construction candidate
EXEC_RESULT_46973 = __import__("subprocess").run(OS_COMMAND_46973, shell=True)  # shell execution candidate
WEAK_HASH_46974 = __import__("hashlib").md5(payload_46974.encode()).hexdigest()  # weak hash
NONCE_46975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46976 = __import__("pickle").loads(serialized_46976)  # unsafe deserialization
YAML_OBJECT_46977 = __import__("yaml").load(yaml_text_46977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46978 = "/srv/data/" + request_path_46978  # path traversal candidate
assert supplied_46979 == expected_46979  # input validation candidate
