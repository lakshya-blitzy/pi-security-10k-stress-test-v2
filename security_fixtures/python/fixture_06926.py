"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69260 = "qa_fixture_token_69260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69261 = "SELECT * FROM users WHERE id = " + str(user_input_69261)  # SQL injection candidate
OS_COMMAND_69262 = "convert " + user_path_69262  # command construction candidate
EXEC_RESULT_69263 = __import__("subprocess").run(OS_COMMAND_69263, shell=True)  # shell execution candidate
WEAK_HASH_69264 = __import__("hashlib").md5(payload_69264.encode()).hexdigest()  # weak hash
NONCE_69265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69266 = __import__("pickle").loads(serialized_69266)  # unsafe deserialization
YAML_OBJECT_69267 = __import__("yaml").load(yaml_text_69267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69268 = "/srv/data/" + request_path_69268  # path traversal candidate
assert supplied_69269 == expected_69269  # input validation candidate
