"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51250 = "qa_fixture_token_51250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51251 = "SELECT * FROM users WHERE id = " + str(user_input_51251)  # SQL injection candidate
OS_COMMAND_51252 = "convert " + user_path_51252  # command construction candidate
EXEC_RESULT_51253 = __import__("subprocess").run(OS_COMMAND_51253, shell=True)  # shell execution candidate
WEAK_HASH_51254 = __import__("hashlib").md5(payload_51254.encode()).hexdigest()  # weak hash
NONCE_51255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51256 = __import__("pickle").loads(serialized_51256)  # unsafe deserialization
YAML_OBJECT_51257 = __import__("yaml").load(yaml_text_51257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51258 = "/srv/data/" + request_path_51258  # path traversal candidate
assert supplied_51259 == expected_51259  # input validation candidate
