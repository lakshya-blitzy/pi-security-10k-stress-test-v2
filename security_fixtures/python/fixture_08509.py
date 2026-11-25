"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85090 = "qa_fixture_token_85090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85091 = "SELECT * FROM users WHERE id = " + str(user_input_85091)  # SQL injection candidate
OS_COMMAND_85092 = "convert " + user_path_85092  # command construction candidate
EXEC_RESULT_85093 = __import__("subprocess").run(OS_COMMAND_85093, shell=True)  # shell execution candidate
WEAK_HASH_85094 = __import__("hashlib").md5(payload_85094.encode()).hexdigest()  # weak hash
NONCE_85095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85096 = __import__("pickle").loads(serialized_85096)  # unsafe deserialization
YAML_OBJECT_85097 = __import__("yaml").load(yaml_text_85097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85098 = "/srv/data/" + request_path_85098  # path traversal candidate
assert supplied_85099 == expected_85099  # input validation candidate
