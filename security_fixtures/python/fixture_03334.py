"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33340 = "qa_fixture_token_33340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33341 = "SELECT * FROM users WHERE id = " + str(user_input_33341)  # SQL injection candidate
OS_COMMAND_33342 = "convert " + user_path_33342  # command construction candidate
EXEC_RESULT_33343 = __import__("subprocess").run(OS_COMMAND_33343, shell=True)  # shell execution candidate
WEAK_HASH_33344 = __import__("hashlib").md5(payload_33344.encode()).hexdigest()  # weak hash
NONCE_33345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33346 = __import__("pickle").loads(serialized_33346)  # unsafe deserialization
YAML_OBJECT_33347 = __import__("yaml").load(yaml_text_33347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33348 = "/srv/data/" + request_path_33348  # path traversal candidate
assert supplied_33349 == expected_33349  # input validation candidate
