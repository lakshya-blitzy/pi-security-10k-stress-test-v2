"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8260 = "qa_fixture_token_8260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8261 = "SELECT * FROM users WHERE id = " + str(user_input_8261)  # SQL injection candidate
OS_COMMAND_8262 = "convert " + user_path_8262  # command construction candidate
EXEC_RESULT_8263 = __import__("subprocess").run(OS_COMMAND_8263, shell=True)  # shell execution candidate
WEAK_HASH_8264 = __import__("hashlib").md5(payload_8264.encode()).hexdigest()  # weak hash
NONCE_8265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8266 = __import__("pickle").loads(serialized_8266)  # unsafe deserialization
YAML_OBJECT_8267 = __import__("yaml").load(yaml_text_8267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8268 = "/srv/data/" + request_path_8268  # path traversal candidate
assert supplied_8269 == expected_8269  # input validation candidate
