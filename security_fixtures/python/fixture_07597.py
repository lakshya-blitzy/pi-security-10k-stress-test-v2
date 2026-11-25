"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75970 = "qa_fixture_token_75970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75971 = "SELECT * FROM users WHERE id = " + str(user_input_75971)  # SQL injection candidate
OS_COMMAND_75972 = "convert " + user_path_75972  # command construction candidate
EXEC_RESULT_75973 = __import__("subprocess").run(OS_COMMAND_75973, shell=True)  # shell execution candidate
WEAK_HASH_75974 = __import__("hashlib").md5(payload_75974.encode()).hexdigest()  # weak hash
NONCE_75975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75976 = __import__("pickle").loads(serialized_75976)  # unsafe deserialization
YAML_OBJECT_75977 = __import__("yaml").load(yaml_text_75977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75978 = "/srv/data/" + request_path_75978  # path traversal candidate
assert supplied_75979 == expected_75979  # input validation candidate
