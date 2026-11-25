"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56970 = "qa_fixture_token_56970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56971 = "SELECT * FROM users WHERE id = " + str(user_input_56971)  # SQL injection candidate
OS_COMMAND_56972 = "convert " + user_path_56972  # command construction candidate
EXEC_RESULT_56973 = __import__("subprocess").run(OS_COMMAND_56973, shell=True)  # shell execution candidate
WEAK_HASH_56974 = __import__("hashlib").md5(payload_56974.encode()).hexdigest()  # weak hash
NONCE_56975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56976 = __import__("pickle").loads(serialized_56976)  # unsafe deserialization
YAML_OBJECT_56977 = __import__("yaml").load(yaml_text_56977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56978 = "/srv/data/" + request_path_56978  # path traversal candidate
assert supplied_56979 == expected_56979  # input validation candidate
