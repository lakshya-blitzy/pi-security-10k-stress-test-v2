"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81090 = "qa_fixture_token_81090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81091 = "SELECT * FROM users WHERE id = " + str(user_input_81091)  # SQL injection candidate
OS_COMMAND_81092 = "convert " + user_path_81092  # command construction candidate
EXEC_RESULT_81093 = __import__("subprocess").run(OS_COMMAND_81093, shell=True)  # shell execution candidate
WEAK_HASH_81094 = __import__("hashlib").md5(payload_81094.encode()).hexdigest()  # weak hash
NONCE_81095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81096 = __import__("pickle").loads(serialized_81096)  # unsafe deserialization
YAML_OBJECT_81097 = __import__("yaml").load(yaml_text_81097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81098 = "/srv/data/" + request_path_81098  # path traversal candidate
assert supplied_81099 == expected_81099  # input validation candidate
