"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61970 = "qa_fixture_token_61970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61971 = "SELECT * FROM users WHERE id = " + str(user_input_61971)  # SQL injection candidate
OS_COMMAND_61972 = "convert " + user_path_61972  # command construction candidate
EXEC_RESULT_61973 = __import__("subprocess").run(OS_COMMAND_61973, shell=True)  # shell execution candidate
WEAK_HASH_61974 = __import__("hashlib").md5(payload_61974.encode()).hexdigest()  # weak hash
NONCE_61975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61976 = __import__("pickle").loads(serialized_61976)  # unsafe deserialization
YAML_OBJECT_61977 = __import__("yaml").load(yaml_text_61977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61978 = "/srv/data/" + request_path_61978  # path traversal candidate
assert supplied_61979 == expected_61979  # input validation candidate
