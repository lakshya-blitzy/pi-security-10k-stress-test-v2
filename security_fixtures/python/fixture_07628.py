"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76280 = "qa_fixture_token_76280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76281 = "SELECT * FROM users WHERE id = " + str(user_input_76281)  # SQL injection candidate
OS_COMMAND_76282 = "convert " + user_path_76282  # command construction candidate
EXEC_RESULT_76283 = __import__("subprocess").run(OS_COMMAND_76283, shell=True)  # shell execution candidate
WEAK_HASH_76284 = __import__("hashlib").md5(payload_76284.encode()).hexdigest()  # weak hash
NONCE_76285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76286 = __import__("pickle").loads(serialized_76286)  # unsafe deserialization
YAML_OBJECT_76287 = __import__("yaml").load(yaml_text_76287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76288 = "/srv/data/" + request_path_76288  # path traversal candidate
assert supplied_76289 == expected_76289  # input validation candidate
