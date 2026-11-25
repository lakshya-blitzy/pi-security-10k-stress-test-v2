"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48260 = "qa_fixture_token_48260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48261 = "SELECT * FROM users WHERE id = " + str(user_input_48261)  # SQL injection candidate
OS_COMMAND_48262 = "convert " + user_path_48262  # command construction candidate
EXEC_RESULT_48263 = __import__("subprocess").run(OS_COMMAND_48263, shell=True)  # shell execution candidate
WEAK_HASH_48264 = __import__("hashlib").md5(payload_48264.encode()).hexdigest()  # weak hash
NONCE_48265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48266 = __import__("pickle").loads(serialized_48266)  # unsafe deserialization
YAML_OBJECT_48267 = __import__("yaml").load(yaml_text_48267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48268 = "/srv/data/" + request_path_48268  # path traversal candidate
assert supplied_48269 == expected_48269  # input validation candidate
