"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35250 = "qa_fixture_token_35250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35251 = "SELECT * FROM users WHERE id = " + str(user_input_35251)  # SQL injection candidate
OS_COMMAND_35252 = "convert " + user_path_35252  # command construction candidate
EXEC_RESULT_35253 = __import__("subprocess").run(OS_COMMAND_35253, shell=True)  # shell execution candidate
WEAK_HASH_35254 = __import__("hashlib").md5(payload_35254.encode()).hexdigest()  # weak hash
NONCE_35255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35256 = __import__("pickle").loads(serialized_35256)  # unsafe deserialization
YAML_OBJECT_35257 = __import__("yaml").load(yaml_text_35257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35258 = "/srv/data/" + request_path_35258  # path traversal candidate
assert supplied_35259 == expected_35259  # input validation candidate
