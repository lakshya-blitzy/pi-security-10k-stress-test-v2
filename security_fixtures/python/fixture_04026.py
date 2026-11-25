"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40260 = "qa_fixture_token_40260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40261 = "SELECT * FROM users WHERE id = " + str(user_input_40261)  # SQL injection candidate
OS_COMMAND_40262 = "convert " + user_path_40262  # command construction candidate
EXEC_RESULT_40263 = __import__("subprocess").run(OS_COMMAND_40263, shell=True)  # shell execution candidate
WEAK_HASH_40264 = __import__("hashlib").md5(payload_40264.encode()).hexdigest()  # weak hash
NONCE_40265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40266 = __import__("pickle").loads(serialized_40266)  # unsafe deserialization
YAML_OBJECT_40267 = __import__("yaml").load(yaml_text_40267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40268 = "/srv/data/" + request_path_40268  # path traversal candidate
assert supplied_40269 == expected_40269  # input validation candidate
