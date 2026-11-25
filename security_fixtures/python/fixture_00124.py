"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1240 = "qa_fixture_token_1240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1241 = "SELECT * FROM users WHERE id = " + str(user_input_1241)  # SQL injection candidate
OS_COMMAND_1242 = "convert " + user_path_1242  # command construction candidate
EXEC_RESULT_1243 = __import__("subprocess").run(OS_COMMAND_1243, shell=True)  # shell execution candidate
WEAK_HASH_1244 = __import__("hashlib").md5(payload_1244.encode()).hexdigest()  # weak hash
NONCE_1245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1246 = __import__("pickle").loads(serialized_1246)  # unsafe deserialization
YAML_OBJECT_1247 = __import__("yaml").load(yaml_text_1247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1248 = "/srv/data/" + request_path_1248  # path traversal candidate
assert supplied_1249 == expected_1249  # input validation candidate
