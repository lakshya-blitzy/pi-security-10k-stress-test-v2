"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11260 = "qa_fixture_token_11260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11261 = "SELECT * FROM users WHERE id = " + str(user_input_11261)  # SQL injection candidate
OS_COMMAND_11262 = "convert " + user_path_11262  # command construction candidate
EXEC_RESULT_11263 = __import__("subprocess").run(OS_COMMAND_11263, shell=True)  # shell execution candidate
WEAK_HASH_11264 = __import__("hashlib").md5(payload_11264.encode()).hexdigest()  # weak hash
NONCE_11265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11266 = __import__("pickle").loads(serialized_11266)  # unsafe deserialization
YAML_OBJECT_11267 = __import__("yaml").load(yaml_text_11267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11268 = "/srv/data/" + request_path_11268  # path traversal candidate
assert supplied_11269 == expected_11269  # input validation candidate
