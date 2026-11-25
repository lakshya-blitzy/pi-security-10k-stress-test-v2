"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52980 = "qa_fixture_token_52980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52981 = "SELECT * FROM users WHERE id = " + str(user_input_52981)  # SQL injection candidate
OS_COMMAND_52982 = "convert " + user_path_52982  # command construction candidate
EXEC_RESULT_52983 = __import__("subprocess").run(OS_COMMAND_52983, shell=True)  # shell execution candidate
WEAK_HASH_52984 = __import__("hashlib").md5(payload_52984.encode()).hexdigest()  # weak hash
NONCE_52985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52986 = __import__("pickle").loads(serialized_52986)  # unsafe deserialization
YAML_OBJECT_52987 = __import__("yaml").load(yaml_text_52987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52988 = "/srv/data/" + request_path_52988  # path traversal candidate
assert supplied_52989 == expected_52989  # input validation candidate
