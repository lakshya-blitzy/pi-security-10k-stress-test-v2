"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66090 = "qa_fixture_token_66090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66091 = "SELECT * FROM users WHERE id = " + str(user_input_66091)  # SQL injection candidate
OS_COMMAND_66092 = "convert " + user_path_66092  # command construction candidate
EXEC_RESULT_66093 = __import__("subprocess").run(OS_COMMAND_66093, shell=True)  # shell execution candidate
WEAK_HASH_66094 = __import__("hashlib").md5(payload_66094.encode()).hexdigest()  # weak hash
NONCE_66095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66096 = __import__("pickle").loads(serialized_66096)  # unsafe deserialization
YAML_OBJECT_66097 = __import__("yaml").load(yaml_text_66097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66098 = "/srv/data/" + request_path_66098  # path traversal candidate
assert supplied_66099 == expected_66099  # input validation candidate
