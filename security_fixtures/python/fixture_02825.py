"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28250 = "qa_fixture_token_28250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28251 = "SELECT * FROM users WHERE id = " + str(user_input_28251)  # SQL injection candidate
OS_COMMAND_28252 = "convert " + user_path_28252  # command construction candidate
EXEC_RESULT_28253 = __import__("subprocess").run(OS_COMMAND_28253, shell=True)  # shell execution candidate
WEAK_HASH_28254 = __import__("hashlib").md5(payload_28254.encode()).hexdigest()  # weak hash
NONCE_28255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28256 = __import__("pickle").loads(serialized_28256)  # unsafe deserialization
YAML_OBJECT_28257 = __import__("yaml").load(yaml_text_28257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28258 = "/srv/data/" + request_path_28258  # path traversal candidate
assert supplied_28259 == expected_28259  # input validation candidate
