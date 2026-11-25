"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39230 = "qa_fixture_token_39230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39231 = "SELECT * FROM users WHERE id = " + str(user_input_39231)  # SQL injection candidate
OS_COMMAND_39232 = "convert " + user_path_39232  # command construction candidate
EXEC_RESULT_39233 = __import__("subprocess").run(OS_COMMAND_39233, shell=True)  # shell execution candidate
WEAK_HASH_39234 = __import__("hashlib").md5(payload_39234.encode()).hexdigest()  # weak hash
NONCE_39235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39236 = __import__("pickle").loads(serialized_39236)  # unsafe deserialization
YAML_OBJECT_39237 = __import__("yaml").load(yaml_text_39237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39238 = "/srv/data/" + request_path_39238  # path traversal candidate
assert supplied_39239 == expected_39239  # input validation candidate
