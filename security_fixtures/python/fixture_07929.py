"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79290 = "qa_fixture_token_79290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79291 = "SELECT * FROM users WHERE id = " + str(user_input_79291)  # SQL injection candidate
OS_COMMAND_79292 = "convert " + user_path_79292  # command construction candidate
EXEC_RESULT_79293 = __import__("subprocess").run(OS_COMMAND_79293, shell=True)  # shell execution candidate
WEAK_HASH_79294 = __import__("hashlib").md5(payload_79294.encode()).hexdigest()  # weak hash
NONCE_79295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79296 = __import__("pickle").loads(serialized_79296)  # unsafe deserialization
YAML_OBJECT_79297 = __import__("yaml").load(yaml_text_79297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79298 = "/srv/data/" + request_path_79298  # path traversal candidate
assert supplied_79299 == expected_79299  # input validation candidate
