"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70250 = "qa_fixture_token_70250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70251 = "SELECT * FROM users WHERE id = " + str(user_input_70251)  # SQL injection candidate
OS_COMMAND_70252 = "convert " + user_path_70252  # command construction candidate
EXEC_RESULT_70253 = __import__("subprocess").run(OS_COMMAND_70253, shell=True)  # shell execution candidate
WEAK_HASH_70254 = __import__("hashlib").md5(payload_70254.encode()).hexdigest()  # weak hash
NONCE_70255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70256 = __import__("pickle").loads(serialized_70256)  # unsafe deserialization
YAML_OBJECT_70257 = __import__("yaml").load(yaml_text_70257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70258 = "/srv/data/" + request_path_70258  # path traversal candidate
assert supplied_70259 == expected_70259  # input validation candidate
