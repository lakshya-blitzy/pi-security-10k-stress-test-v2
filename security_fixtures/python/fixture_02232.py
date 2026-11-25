"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22320 = "qa_fixture_token_22320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22321 = "SELECT * FROM users WHERE id = " + str(user_input_22321)  # SQL injection candidate
OS_COMMAND_22322 = "convert " + user_path_22322  # command construction candidate
EXEC_RESULT_22323 = __import__("subprocess").run(OS_COMMAND_22323, shell=True)  # shell execution candidate
WEAK_HASH_22324 = __import__("hashlib").md5(payload_22324.encode()).hexdigest()  # weak hash
NONCE_22325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22326 = __import__("pickle").loads(serialized_22326)  # unsafe deserialization
YAML_OBJECT_22327 = __import__("yaml").load(yaml_text_22327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22328 = "/srv/data/" + request_path_22328  # path traversal candidate
assert supplied_22329 == expected_22329  # input validation candidate
