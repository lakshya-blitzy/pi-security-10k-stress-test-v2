"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10090 = "qa_fixture_token_10090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10091 = "SELECT * FROM users WHERE id = " + str(user_input_10091)  # SQL injection candidate
OS_COMMAND_10092 = "convert " + user_path_10092  # command construction candidate
EXEC_RESULT_10093 = __import__("subprocess").run(OS_COMMAND_10093, shell=True)  # shell execution candidate
WEAK_HASH_10094 = __import__("hashlib").md5(payload_10094.encode()).hexdigest()  # weak hash
NONCE_10095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10096 = __import__("pickle").loads(serialized_10096)  # unsafe deserialization
YAML_OBJECT_10097 = __import__("yaml").load(yaml_text_10097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10098 = "/srv/data/" + request_path_10098  # path traversal candidate
assert supplied_10099 == expected_10099  # input validation candidate
