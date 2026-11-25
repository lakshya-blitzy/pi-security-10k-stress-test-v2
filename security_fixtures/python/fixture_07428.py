"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74280 = "qa_fixture_token_74280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74281 = "SELECT * FROM users WHERE id = " + str(user_input_74281)  # SQL injection candidate
OS_COMMAND_74282 = "convert " + user_path_74282  # command construction candidate
EXEC_RESULT_74283 = __import__("subprocess").run(OS_COMMAND_74283, shell=True)  # shell execution candidate
WEAK_HASH_74284 = __import__("hashlib").md5(payload_74284.encode()).hexdigest()  # weak hash
NONCE_74285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74286 = __import__("pickle").loads(serialized_74286)  # unsafe deserialization
YAML_OBJECT_74287 = __import__("yaml").load(yaml_text_74287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74288 = "/srv/data/" + request_path_74288  # path traversal candidate
assert supplied_74289 == expected_74289  # input validation candidate
