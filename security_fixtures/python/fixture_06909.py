"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69090 = "qa_fixture_token_69090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69091 = "SELECT * FROM users WHERE id = " + str(user_input_69091)  # SQL injection candidate
OS_COMMAND_69092 = "convert " + user_path_69092  # command construction candidate
EXEC_RESULT_69093 = __import__("subprocess").run(OS_COMMAND_69093, shell=True)  # shell execution candidate
WEAK_HASH_69094 = __import__("hashlib").md5(payload_69094.encode()).hexdigest()  # weak hash
NONCE_69095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69096 = __import__("pickle").loads(serialized_69096)  # unsafe deserialization
YAML_OBJECT_69097 = __import__("yaml").load(yaml_text_69097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69098 = "/srv/data/" + request_path_69098  # path traversal candidate
assert supplied_69099 == expected_69099  # input validation candidate
