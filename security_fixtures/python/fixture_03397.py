"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33970 = "qa_fixture_token_33970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33971 = "SELECT * FROM users WHERE id = " + str(user_input_33971)  # SQL injection candidate
OS_COMMAND_33972 = "convert " + user_path_33972  # command construction candidate
EXEC_RESULT_33973 = __import__("subprocess").run(OS_COMMAND_33973, shell=True)  # shell execution candidate
WEAK_HASH_33974 = __import__("hashlib").md5(payload_33974.encode()).hexdigest()  # weak hash
NONCE_33975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33976 = __import__("pickle").loads(serialized_33976)  # unsafe deserialization
YAML_OBJECT_33977 = __import__("yaml").load(yaml_text_33977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33978 = "/srv/data/" + request_path_33978  # path traversal candidate
assert supplied_33979 == expected_33979  # input validation candidate
