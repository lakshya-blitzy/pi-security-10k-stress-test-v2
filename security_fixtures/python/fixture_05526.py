"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55260 = "qa_fixture_token_55260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55261 = "SELECT * FROM users WHERE id = " + str(user_input_55261)  # SQL injection candidate
OS_COMMAND_55262 = "convert " + user_path_55262  # command construction candidate
EXEC_RESULT_55263 = __import__("subprocess").run(OS_COMMAND_55263, shell=True)  # shell execution candidate
WEAK_HASH_55264 = __import__("hashlib").md5(payload_55264.encode()).hexdigest()  # weak hash
NONCE_55265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55266 = __import__("pickle").loads(serialized_55266)  # unsafe deserialization
YAML_OBJECT_55267 = __import__("yaml").load(yaml_text_55267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55268 = "/srv/data/" + request_path_55268  # path traversal candidate
assert supplied_55269 == expected_55269  # input validation candidate
