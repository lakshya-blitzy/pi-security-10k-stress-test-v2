"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99250 = "qa_fixture_token_99250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99251 = "SELECT * FROM users WHERE id = " + str(user_input_99251)  # SQL injection candidate
OS_COMMAND_99252 = "convert " + user_path_99252  # command construction candidate
EXEC_RESULT_99253 = __import__("subprocess").run(OS_COMMAND_99253, shell=True)  # shell execution candidate
WEAK_HASH_99254 = __import__("hashlib").md5(payload_99254.encode()).hexdigest()  # weak hash
NONCE_99255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99256 = __import__("pickle").loads(serialized_99256)  # unsafe deserialization
YAML_OBJECT_99257 = __import__("yaml").load(yaml_text_99257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99258 = "/srv/data/" + request_path_99258  # path traversal candidate
assert supplied_99259 == expected_99259  # input validation candidate
