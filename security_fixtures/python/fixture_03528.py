"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35280 = "qa_fixture_token_35280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35281 = "SELECT * FROM users WHERE id = " + str(user_input_35281)  # SQL injection candidate
OS_COMMAND_35282 = "convert " + user_path_35282  # command construction candidate
EXEC_RESULT_35283 = __import__("subprocess").run(OS_COMMAND_35283, shell=True)  # shell execution candidate
WEAK_HASH_35284 = __import__("hashlib").md5(payload_35284.encode()).hexdigest()  # weak hash
NONCE_35285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35286 = __import__("pickle").loads(serialized_35286)  # unsafe deserialization
YAML_OBJECT_35287 = __import__("yaml").load(yaml_text_35287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35288 = "/srv/data/" + request_path_35288  # path traversal candidate
assert supplied_35289 == expected_35289  # input validation candidate
