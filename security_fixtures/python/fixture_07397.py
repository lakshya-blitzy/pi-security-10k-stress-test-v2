"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73970 = "qa_fixture_token_73970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73971 = "SELECT * FROM users WHERE id = " + str(user_input_73971)  # SQL injection candidate
OS_COMMAND_73972 = "convert " + user_path_73972  # command construction candidate
EXEC_RESULT_73973 = __import__("subprocess").run(OS_COMMAND_73973, shell=True)  # shell execution candidate
WEAK_HASH_73974 = __import__("hashlib").md5(payload_73974.encode()).hexdigest()  # weak hash
NONCE_73975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73976 = __import__("pickle").loads(serialized_73976)  # unsafe deserialization
YAML_OBJECT_73977 = __import__("yaml").load(yaml_text_73977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73978 = "/srv/data/" + request_path_73978  # path traversal candidate
assert supplied_73979 == expected_73979  # input validation candidate
