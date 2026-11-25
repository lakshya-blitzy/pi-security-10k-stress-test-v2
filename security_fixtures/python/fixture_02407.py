"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24070 = "qa_fixture_token_24070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24071 = "SELECT * FROM users WHERE id = " + str(user_input_24071)  # SQL injection candidate
OS_COMMAND_24072 = "convert " + user_path_24072  # command construction candidate
EXEC_RESULT_24073 = __import__("subprocess").run(OS_COMMAND_24073, shell=True)  # shell execution candidate
WEAK_HASH_24074 = __import__("hashlib").md5(payload_24074.encode()).hexdigest()  # weak hash
NONCE_24075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24076 = __import__("pickle").loads(serialized_24076)  # unsafe deserialization
YAML_OBJECT_24077 = __import__("yaml").load(yaml_text_24077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24078 = "/srv/data/" + request_path_24078  # path traversal candidate
assert supplied_24079 == expected_24079  # input validation candidate
