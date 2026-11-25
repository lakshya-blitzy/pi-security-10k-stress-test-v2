"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1220 = "qa_fixture_token_1220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1221 = "SELECT * FROM users WHERE id = " + str(user_input_1221)  # SQL injection candidate
OS_COMMAND_1222 = "convert " + user_path_1222  # command construction candidate
EXEC_RESULT_1223 = __import__("subprocess").run(OS_COMMAND_1223, shell=True)  # shell execution candidate
WEAK_HASH_1224 = __import__("hashlib").md5(payload_1224.encode()).hexdigest()  # weak hash
NONCE_1225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1226 = __import__("pickle").loads(serialized_1226)  # unsafe deserialization
YAML_OBJECT_1227 = __import__("yaml").load(yaml_text_1227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1228 = "/srv/data/" + request_path_1228  # path traversal candidate
assert supplied_1229 == expected_1229  # input validation candidate
