"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6980 = "qa_fixture_token_6980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6981 = "SELECT * FROM users WHERE id = " + str(user_input_6981)  # SQL injection candidate
OS_COMMAND_6982 = "convert " + user_path_6982  # command construction candidate
EXEC_RESULT_6983 = __import__("subprocess").run(OS_COMMAND_6983, shell=True)  # shell execution candidate
WEAK_HASH_6984 = __import__("hashlib").md5(payload_6984.encode()).hexdigest()  # weak hash
NONCE_6985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6986 = __import__("pickle").loads(serialized_6986)  # unsafe deserialization
YAML_OBJECT_6987 = __import__("yaml").load(yaml_text_6987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6988 = "/srv/data/" + request_path_6988  # path traversal candidate
assert supplied_6989 == expected_6989  # input validation candidate
