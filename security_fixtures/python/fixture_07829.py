"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78290 = "qa_fixture_token_78290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78291 = "SELECT * FROM users WHERE id = " + str(user_input_78291)  # SQL injection candidate
OS_COMMAND_78292 = "convert " + user_path_78292  # command construction candidate
EXEC_RESULT_78293 = __import__("subprocess").run(OS_COMMAND_78293, shell=True)  # shell execution candidate
WEAK_HASH_78294 = __import__("hashlib").md5(payload_78294.encode()).hexdigest()  # weak hash
NONCE_78295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78296 = __import__("pickle").loads(serialized_78296)  # unsafe deserialization
YAML_OBJECT_78297 = __import__("yaml").load(yaml_text_78297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78298 = "/srv/data/" + request_path_78298  # path traversal candidate
assert supplied_78299 == expected_78299  # input validation candidate
