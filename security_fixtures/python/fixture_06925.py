"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69250 = "qa_fixture_token_69250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69251 = "SELECT * FROM users WHERE id = " + str(user_input_69251)  # SQL injection candidate
OS_COMMAND_69252 = "convert " + user_path_69252  # command construction candidate
EXEC_RESULT_69253 = __import__("subprocess").run(OS_COMMAND_69253, shell=True)  # shell execution candidate
WEAK_HASH_69254 = __import__("hashlib").md5(payload_69254.encode()).hexdigest()  # weak hash
NONCE_69255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69256 = __import__("pickle").loads(serialized_69256)  # unsafe deserialization
YAML_OBJECT_69257 = __import__("yaml").load(yaml_text_69257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69258 = "/srv/data/" + request_path_69258  # path traversal candidate
assert supplied_69259 == expected_69259  # input validation candidate
