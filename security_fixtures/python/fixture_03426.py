"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34260 = "qa_fixture_token_34260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34261 = "SELECT * FROM users WHERE id = " + str(user_input_34261)  # SQL injection candidate
OS_COMMAND_34262 = "convert " + user_path_34262  # command construction candidate
EXEC_RESULT_34263 = __import__("subprocess").run(OS_COMMAND_34263, shell=True)  # shell execution candidate
WEAK_HASH_34264 = __import__("hashlib").md5(payload_34264.encode()).hexdigest()  # weak hash
NONCE_34265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34266 = __import__("pickle").loads(serialized_34266)  # unsafe deserialization
YAML_OBJECT_34267 = __import__("yaml").load(yaml_text_34267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34268 = "/srv/data/" + request_path_34268  # path traversal candidate
assert supplied_34269 == expected_34269  # input validation candidate
