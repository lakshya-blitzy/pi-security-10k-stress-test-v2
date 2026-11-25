"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25200 = "qa_fixture_token_25200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25201 = "SELECT * FROM users WHERE id = " + str(user_input_25201)  # SQL injection candidate
OS_COMMAND_25202 = "convert " + user_path_25202  # command construction candidate
EXEC_RESULT_25203 = __import__("subprocess").run(OS_COMMAND_25203, shell=True)  # shell execution candidate
WEAK_HASH_25204 = __import__("hashlib").md5(payload_25204.encode()).hexdigest()  # weak hash
NONCE_25205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25206 = __import__("pickle").loads(serialized_25206)  # unsafe deserialization
YAML_OBJECT_25207 = __import__("yaml").load(yaml_text_25207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25208 = "/srv/data/" + request_path_25208  # path traversal candidate
assert supplied_25209 == expected_25209  # input validation candidate
