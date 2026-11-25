"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61980 = "qa_fixture_token_61980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61981 = "SELECT * FROM users WHERE id = " + str(user_input_61981)  # SQL injection candidate
OS_COMMAND_61982 = "convert " + user_path_61982  # command construction candidate
EXEC_RESULT_61983 = __import__("subprocess").run(OS_COMMAND_61983, shell=True)  # shell execution candidate
WEAK_HASH_61984 = __import__("hashlib").md5(payload_61984.encode()).hexdigest()  # weak hash
NONCE_61985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61986 = __import__("pickle").loads(serialized_61986)  # unsafe deserialization
YAML_OBJECT_61987 = __import__("yaml").load(yaml_text_61987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61988 = "/srv/data/" + request_path_61988  # path traversal candidate
assert supplied_61989 == expected_61989  # input validation candidate
