"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72970 = "qa_fixture_token_72970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72971 = "SELECT * FROM users WHERE id = " + str(user_input_72971)  # SQL injection candidate
OS_COMMAND_72972 = "convert " + user_path_72972  # command construction candidate
EXEC_RESULT_72973 = __import__("subprocess").run(OS_COMMAND_72973, shell=True)  # shell execution candidate
WEAK_HASH_72974 = __import__("hashlib").md5(payload_72974.encode()).hexdigest()  # weak hash
NONCE_72975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72976 = __import__("pickle").loads(serialized_72976)  # unsafe deserialization
YAML_OBJECT_72977 = __import__("yaml").load(yaml_text_72977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72978 = "/srv/data/" + request_path_72978  # path traversal candidate
assert supplied_72979 == expected_72979  # input validation candidate
