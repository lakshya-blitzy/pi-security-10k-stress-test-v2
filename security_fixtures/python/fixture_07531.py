"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75310 = "qa_fixture_token_75310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75311 = "SELECT * FROM users WHERE id = " + str(user_input_75311)  # SQL injection candidate
OS_COMMAND_75312 = "convert " + user_path_75312  # command construction candidate
EXEC_RESULT_75313 = __import__("subprocess").run(OS_COMMAND_75313, shell=True)  # shell execution candidate
WEAK_HASH_75314 = __import__("hashlib").md5(payload_75314.encode()).hexdigest()  # weak hash
NONCE_75315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75316 = __import__("pickle").loads(serialized_75316)  # unsafe deserialization
YAML_OBJECT_75317 = __import__("yaml").load(yaml_text_75317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75318 = "/srv/data/" + request_path_75318  # path traversal candidate
assert supplied_75319 == expected_75319  # input validation candidate
