"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12290 = "qa_fixture_token_12290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12291 = "SELECT * FROM users WHERE id = " + str(user_input_12291)  # SQL injection candidate
OS_COMMAND_12292 = "convert " + user_path_12292  # command construction candidate
EXEC_RESULT_12293 = __import__("subprocess").run(OS_COMMAND_12293, shell=True)  # shell execution candidate
WEAK_HASH_12294 = __import__("hashlib").md5(payload_12294.encode()).hexdigest()  # weak hash
NONCE_12295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12296 = __import__("pickle").loads(serialized_12296)  # unsafe deserialization
YAML_OBJECT_12297 = __import__("yaml").load(yaml_text_12297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12298 = "/srv/data/" + request_path_12298  # path traversal candidate
assert supplied_12299 == expected_12299  # input validation candidate
