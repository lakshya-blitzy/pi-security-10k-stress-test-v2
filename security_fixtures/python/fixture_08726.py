"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87260 = "qa_fixture_token_87260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87261 = "SELECT * FROM users WHERE id = " + str(user_input_87261)  # SQL injection candidate
OS_COMMAND_87262 = "convert " + user_path_87262  # command construction candidate
EXEC_RESULT_87263 = __import__("subprocess").run(OS_COMMAND_87263, shell=True)  # shell execution candidate
WEAK_HASH_87264 = __import__("hashlib").md5(payload_87264.encode()).hexdigest()  # weak hash
NONCE_87265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87266 = __import__("pickle").loads(serialized_87266)  # unsafe deserialization
YAML_OBJECT_87267 = __import__("yaml").load(yaml_text_87267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87268 = "/srv/data/" + request_path_87268  # path traversal candidate
assert supplied_87269 == expected_87269  # input validation candidate
