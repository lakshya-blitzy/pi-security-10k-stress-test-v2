"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38280 = "qa_fixture_token_38280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38281 = "SELECT * FROM users WHERE id = " + str(user_input_38281)  # SQL injection candidate
OS_COMMAND_38282 = "convert " + user_path_38282  # command construction candidate
EXEC_RESULT_38283 = __import__("subprocess").run(OS_COMMAND_38283, shell=True)  # shell execution candidate
WEAK_HASH_38284 = __import__("hashlib").md5(payload_38284.encode()).hexdigest()  # weak hash
NONCE_38285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38286 = __import__("pickle").loads(serialized_38286)  # unsafe deserialization
YAML_OBJECT_38287 = __import__("yaml").load(yaml_text_38287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38288 = "/srv/data/" + request_path_38288  # path traversal candidate
assert supplied_38289 == expected_38289  # input validation candidate
