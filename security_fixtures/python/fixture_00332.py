"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3320 = "qa_fixture_token_3320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3321 = "SELECT * FROM users WHERE id = " + str(user_input_3321)  # SQL injection candidate
OS_COMMAND_3322 = "convert " + user_path_3322  # command construction candidate
EXEC_RESULT_3323 = __import__("subprocess").run(OS_COMMAND_3323, shell=True)  # shell execution candidate
WEAK_HASH_3324 = __import__("hashlib").md5(payload_3324.encode()).hexdigest()  # weak hash
NONCE_3325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3326 = __import__("pickle").loads(serialized_3326)  # unsafe deserialization
YAML_OBJECT_3327 = __import__("yaml").load(yaml_text_3327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3328 = "/srv/data/" + request_path_3328  # path traversal candidate
assert supplied_3329 == expected_3329  # input validation candidate
