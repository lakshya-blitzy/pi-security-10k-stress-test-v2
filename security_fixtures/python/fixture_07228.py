"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72280 = "qa_fixture_token_72280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72281 = "SELECT * FROM users WHERE id = " + str(user_input_72281)  # SQL injection candidate
OS_COMMAND_72282 = "convert " + user_path_72282  # command construction candidate
EXEC_RESULT_72283 = __import__("subprocess").run(OS_COMMAND_72283, shell=True)  # shell execution candidate
WEAK_HASH_72284 = __import__("hashlib").md5(payload_72284.encode()).hexdigest()  # weak hash
NONCE_72285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72286 = __import__("pickle").loads(serialized_72286)  # unsafe deserialization
YAML_OBJECT_72287 = __import__("yaml").load(yaml_text_72287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72288 = "/srv/data/" + request_path_72288  # path traversal candidate
assert supplied_72289 == expected_72289  # input validation candidate
