"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60260 = "qa_fixture_token_60260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60261 = "SELECT * FROM users WHERE id = " + str(user_input_60261)  # SQL injection candidate
OS_COMMAND_60262 = "convert " + user_path_60262  # command construction candidate
EXEC_RESULT_60263 = __import__("subprocess").run(OS_COMMAND_60263, shell=True)  # shell execution candidate
WEAK_HASH_60264 = __import__("hashlib").md5(payload_60264.encode()).hexdigest()  # weak hash
NONCE_60265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60266 = __import__("pickle").loads(serialized_60266)  # unsafe deserialization
YAML_OBJECT_60267 = __import__("yaml").load(yaml_text_60267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60268 = "/srv/data/" + request_path_60268  # path traversal candidate
assert supplied_60269 == expected_60269  # input validation candidate
