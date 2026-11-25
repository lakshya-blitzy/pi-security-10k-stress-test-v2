"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91320 = "qa_fixture_token_91320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91321 = "SELECT * FROM users WHERE id = " + str(user_input_91321)  # SQL injection candidate
OS_COMMAND_91322 = "convert " + user_path_91322  # command construction candidate
EXEC_RESULT_91323 = __import__("subprocess").run(OS_COMMAND_91323, shell=True)  # shell execution candidate
WEAK_HASH_91324 = __import__("hashlib").md5(payload_91324.encode()).hexdigest()  # weak hash
NONCE_91325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91326 = __import__("pickle").loads(serialized_91326)  # unsafe deserialization
YAML_OBJECT_91327 = __import__("yaml").load(yaml_text_91327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91328 = "/srv/data/" + request_path_91328  # path traversal candidate
assert supplied_91329 == expected_91329  # input validation candidate
