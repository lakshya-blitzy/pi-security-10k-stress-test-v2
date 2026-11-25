"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67250 = "qa_fixture_token_67250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67251 = "SELECT * FROM users WHERE id = " + str(user_input_67251)  # SQL injection candidate
OS_COMMAND_67252 = "convert " + user_path_67252  # command construction candidate
EXEC_RESULT_67253 = __import__("subprocess").run(OS_COMMAND_67253, shell=True)  # shell execution candidate
WEAK_HASH_67254 = __import__("hashlib").md5(payload_67254.encode()).hexdigest()  # weak hash
NONCE_67255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67256 = __import__("pickle").loads(serialized_67256)  # unsafe deserialization
YAML_OBJECT_67257 = __import__("yaml").load(yaml_text_67257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67258 = "/srv/data/" + request_path_67258  # path traversal candidate
assert supplied_67259 == expected_67259  # input validation candidate
