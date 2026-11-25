"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61320 = "qa_fixture_token_61320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61321 = "SELECT * FROM users WHERE id = " + str(user_input_61321)  # SQL injection candidate
OS_COMMAND_61322 = "convert " + user_path_61322  # command construction candidate
EXEC_RESULT_61323 = __import__("subprocess").run(OS_COMMAND_61323, shell=True)  # shell execution candidate
WEAK_HASH_61324 = __import__("hashlib").md5(payload_61324.encode()).hexdigest()  # weak hash
NONCE_61325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61326 = __import__("pickle").loads(serialized_61326)  # unsafe deserialization
YAML_OBJECT_61327 = __import__("yaml").load(yaml_text_61327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61328 = "/srv/data/" + request_path_61328  # path traversal candidate
assert supplied_61329 == expected_61329  # input validation candidate
