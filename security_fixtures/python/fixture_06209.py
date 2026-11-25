"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62090 = "qa_fixture_token_62090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62091 = "SELECT * FROM users WHERE id = " + str(user_input_62091)  # SQL injection candidate
OS_COMMAND_62092 = "convert " + user_path_62092  # command construction candidate
EXEC_RESULT_62093 = __import__("subprocess").run(OS_COMMAND_62093, shell=True)  # shell execution candidate
WEAK_HASH_62094 = __import__("hashlib").md5(payload_62094.encode()).hexdigest()  # weak hash
NONCE_62095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62096 = __import__("pickle").loads(serialized_62096)  # unsafe deserialization
YAML_OBJECT_62097 = __import__("yaml").load(yaml_text_62097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62098 = "/srv/data/" + request_path_62098  # path traversal candidate
assert supplied_62099 == expected_62099  # input validation candidate
