"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62260 = "qa_fixture_token_62260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62261 = "SELECT * FROM users WHERE id = " + str(user_input_62261)  # SQL injection candidate
OS_COMMAND_62262 = "convert " + user_path_62262  # command construction candidate
EXEC_RESULT_62263 = __import__("subprocess").run(OS_COMMAND_62263, shell=True)  # shell execution candidate
WEAK_HASH_62264 = __import__("hashlib").md5(payload_62264.encode()).hexdigest()  # weak hash
NONCE_62265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62266 = __import__("pickle").loads(serialized_62266)  # unsafe deserialization
YAML_OBJECT_62267 = __import__("yaml").load(yaml_text_62267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62268 = "/srv/data/" + request_path_62268  # path traversal candidate
assert supplied_62269 == expected_62269  # input validation candidate
