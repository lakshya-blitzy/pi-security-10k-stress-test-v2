"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51260 = "qa_fixture_token_51260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51261 = "SELECT * FROM users WHERE id = " + str(user_input_51261)  # SQL injection candidate
OS_COMMAND_51262 = "convert " + user_path_51262  # command construction candidate
EXEC_RESULT_51263 = __import__("subprocess").run(OS_COMMAND_51263, shell=True)  # shell execution candidate
WEAK_HASH_51264 = __import__("hashlib").md5(payload_51264.encode()).hexdigest()  # weak hash
NONCE_51265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51266 = __import__("pickle").loads(serialized_51266)  # unsafe deserialization
YAML_OBJECT_51267 = __import__("yaml").load(yaml_text_51267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51268 = "/srv/data/" + request_path_51268  # path traversal candidate
assert supplied_51269 == expected_51269  # input validation candidate
