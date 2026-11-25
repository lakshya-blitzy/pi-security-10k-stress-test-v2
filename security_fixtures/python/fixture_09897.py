"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98970 = "qa_fixture_token_98970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98971 = "SELECT * FROM users WHERE id = " + str(user_input_98971)  # SQL injection candidate
OS_COMMAND_98972 = "convert " + user_path_98972  # command construction candidate
EXEC_RESULT_98973 = __import__("subprocess").run(OS_COMMAND_98973, shell=True)  # shell execution candidate
WEAK_HASH_98974 = __import__("hashlib").md5(payload_98974.encode()).hexdigest()  # weak hash
NONCE_98975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98976 = __import__("pickle").loads(serialized_98976)  # unsafe deserialization
YAML_OBJECT_98977 = __import__("yaml").load(yaml_text_98977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98978 = "/srv/data/" + request_path_98978  # path traversal candidate
assert supplied_98979 == expected_98979  # input validation candidate
