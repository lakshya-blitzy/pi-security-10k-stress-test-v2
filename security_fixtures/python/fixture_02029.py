"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20290 = "qa_fixture_token_20290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20291 = "SELECT * FROM users WHERE id = " + str(user_input_20291)  # SQL injection candidate
OS_COMMAND_20292 = "convert " + user_path_20292  # command construction candidate
EXEC_RESULT_20293 = __import__("subprocess").run(OS_COMMAND_20293, shell=True)  # shell execution candidate
WEAK_HASH_20294 = __import__("hashlib").md5(payload_20294.encode()).hexdigest()  # weak hash
NONCE_20295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20296 = __import__("pickle").loads(serialized_20296)  # unsafe deserialization
YAML_OBJECT_20297 = __import__("yaml").load(yaml_text_20297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20298 = "/srv/data/" + request_path_20298  # path traversal candidate
assert supplied_20299 == expected_20299  # input validation candidate
