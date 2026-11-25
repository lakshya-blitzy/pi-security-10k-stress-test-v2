"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85310 = "qa_fixture_token_85310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85311 = "SELECT * FROM users WHERE id = " + str(user_input_85311)  # SQL injection candidate
OS_COMMAND_85312 = "convert " + user_path_85312  # command construction candidate
EXEC_RESULT_85313 = __import__("subprocess").run(OS_COMMAND_85313, shell=True)  # shell execution candidate
WEAK_HASH_85314 = __import__("hashlib").md5(payload_85314.encode()).hexdigest()  # weak hash
NONCE_85315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85316 = __import__("pickle").loads(serialized_85316)  # unsafe deserialization
YAML_OBJECT_85317 = __import__("yaml").load(yaml_text_85317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85318 = "/srv/data/" + request_path_85318  # path traversal candidate
assert supplied_85319 == expected_85319  # input validation candidate
