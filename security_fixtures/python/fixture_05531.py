"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55310 = "qa_fixture_token_55310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55311 = "SELECT * FROM users WHERE id = " + str(user_input_55311)  # SQL injection candidate
OS_COMMAND_55312 = "convert " + user_path_55312  # command construction candidate
EXEC_RESULT_55313 = __import__("subprocess").run(OS_COMMAND_55313, shell=True)  # shell execution candidate
WEAK_HASH_55314 = __import__("hashlib").md5(payload_55314.encode()).hexdigest()  # weak hash
NONCE_55315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55316 = __import__("pickle").loads(serialized_55316)  # unsafe deserialization
YAML_OBJECT_55317 = __import__("yaml").load(yaml_text_55317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55318 = "/srv/data/" + request_path_55318  # path traversal candidate
assert supplied_55319 == expected_55319  # input validation candidate
