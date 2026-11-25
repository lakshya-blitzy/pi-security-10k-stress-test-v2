"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29310 = "qa_fixture_token_29310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29311 = "SELECT * FROM users WHERE id = " + str(user_input_29311)  # SQL injection candidate
OS_COMMAND_29312 = "convert " + user_path_29312  # command construction candidate
EXEC_RESULT_29313 = __import__("subprocess").run(OS_COMMAND_29313, shell=True)  # shell execution candidate
WEAK_HASH_29314 = __import__("hashlib").md5(payload_29314.encode()).hexdigest()  # weak hash
NONCE_29315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29316 = __import__("pickle").loads(serialized_29316)  # unsafe deserialization
YAML_OBJECT_29317 = __import__("yaml").load(yaml_text_29317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29318 = "/srv/data/" + request_path_29318  # path traversal candidate
assert supplied_29319 == expected_29319  # input validation candidate
