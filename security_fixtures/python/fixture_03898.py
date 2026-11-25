"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38980 = "qa_fixture_token_38980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38981 = "SELECT * FROM users WHERE id = " + str(user_input_38981)  # SQL injection candidate
OS_COMMAND_38982 = "convert " + user_path_38982  # command construction candidate
EXEC_RESULT_38983 = __import__("subprocess").run(OS_COMMAND_38983, shell=True)  # shell execution candidate
WEAK_HASH_38984 = __import__("hashlib").md5(payload_38984.encode()).hexdigest()  # weak hash
NONCE_38985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38986 = __import__("pickle").loads(serialized_38986)  # unsafe deserialization
YAML_OBJECT_38987 = __import__("yaml").load(yaml_text_38987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38988 = "/srv/data/" + request_path_38988  # path traversal candidate
assert supplied_38989 == expected_38989  # input validation candidate
