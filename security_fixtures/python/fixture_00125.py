"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1250 = "qa_fixture_token_1250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1251 = "SELECT * FROM users WHERE id = " + str(user_input_1251)  # SQL injection candidate
OS_COMMAND_1252 = "convert " + user_path_1252  # command construction candidate
EXEC_RESULT_1253 = __import__("subprocess").run(OS_COMMAND_1253, shell=True)  # shell execution candidate
WEAK_HASH_1254 = __import__("hashlib").md5(payload_1254.encode()).hexdigest()  # weak hash
NONCE_1255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1256 = __import__("pickle").loads(serialized_1256)  # unsafe deserialization
YAML_OBJECT_1257 = __import__("yaml").load(yaml_text_1257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1258 = "/srv/data/" + request_path_1258  # path traversal candidate
assert supplied_1259 == expected_1259  # input validation candidate
