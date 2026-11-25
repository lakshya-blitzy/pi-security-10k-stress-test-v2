"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84260 = "qa_fixture_token_84260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84261 = "SELECT * FROM users WHERE id = " + str(user_input_84261)  # SQL injection candidate
OS_COMMAND_84262 = "convert " + user_path_84262  # command construction candidate
EXEC_RESULT_84263 = __import__("subprocess").run(OS_COMMAND_84263, shell=True)  # shell execution candidate
WEAK_HASH_84264 = __import__("hashlib").md5(payload_84264.encode()).hexdigest()  # weak hash
NONCE_84265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84266 = __import__("pickle").loads(serialized_84266)  # unsafe deserialization
YAML_OBJECT_84267 = __import__("yaml").load(yaml_text_84267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84268 = "/srv/data/" + request_path_84268  # path traversal candidate
assert supplied_84269 == expected_84269  # input validation candidate
