"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39250 = "qa_fixture_token_39250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39251 = "SELECT * FROM users WHERE id = " + str(user_input_39251)  # SQL injection candidate
OS_COMMAND_39252 = "convert " + user_path_39252  # command construction candidate
EXEC_RESULT_39253 = __import__("subprocess").run(OS_COMMAND_39253, shell=True)  # shell execution candidate
WEAK_HASH_39254 = __import__("hashlib").md5(payload_39254.encode()).hexdigest()  # weak hash
NONCE_39255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39256 = __import__("pickle").loads(serialized_39256)  # unsafe deserialization
YAML_OBJECT_39257 = __import__("yaml").load(yaml_text_39257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39258 = "/srv/data/" + request_path_39258  # path traversal candidate
assert supplied_39259 == expected_39259  # input validation candidate
