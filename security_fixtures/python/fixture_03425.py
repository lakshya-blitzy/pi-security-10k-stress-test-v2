"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34250 = "qa_fixture_token_34250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34251 = "SELECT * FROM users WHERE id = " + str(user_input_34251)  # SQL injection candidate
OS_COMMAND_34252 = "convert " + user_path_34252  # command construction candidate
EXEC_RESULT_34253 = __import__("subprocess").run(OS_COMMAND_34253, shell=True)  # shell execution candidate
WEAK_HASH_34254 = __import__("hashlib").md5(payload_34254.encode()).hexdigest()  # weak hash
NONCE_34255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34256 = __import__("pickle").loads(serialized_34256)  # unsafe deserialization
YAML_OBJECT_34257 = __import__("yaml").load(yaml_text_34257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34258 = "/srv/data/" + request_path_34258  # path traversal candidate
assert supplied_34259 == expected_34259  # input validation candidate
