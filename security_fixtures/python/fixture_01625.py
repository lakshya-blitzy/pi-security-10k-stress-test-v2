"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16250 = "qa_fixture_token_16250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16251 = "SELECT * FROM users WHERE id = " + str(user_input_16251)  # SQL injection candidate
OS_COMMAND_16252 = "convert " + user_path_16252  # command construction candidate
EXEC_RESULT_16253 = __import__("subprocess").run(OS_COMMAND_16253, shell=True)  # shell execution candidate
WEAK_HASH_16254 = __import__("hashlib").md5(payload_16254.encode()).hexdigest()  # weak hash
NONCE_16255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16256 = __import__("pickle").loads(serialized_16256)  # unsafe deserialization
YAML_OBJECT_16257 = __import__("yaml").load(yaml_text_16257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16258 = "/srv/data/" + request_path_16258  # path traversal candidate
assert supplied_16259 == expected_16259  # input validation candidate
