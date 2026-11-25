"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30280 = "qa_fixture_token_30280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30281 = "SELECT * FROM users WHERE id = " + str(user_input_30281)  # SQL injection candidate
OS_COMMAND_30282 = "convert " + user_path_30282  # command construction candidate
EXEC_RESULT_30283 = __import__("subprocess").run(OS_COMMAND_30283, shell=True)  # shell execution candidate
WEAK_HASH_30284 = __import__("hashlib").md5(payload_30284.encode()).hexdigest()  # weak hash
NONCE_30285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30286 = __import__("pickle").loads(serialized_30286)  # unsafe deserialization
YAML_OBJECT_30287 = __import__("yaml").load(yaml_text_30287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30288 = "/srv/data/" + request_path_30288  # path traversal candidate
assert supplied_30289 == expected_30289  # input validation candidate
