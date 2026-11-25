"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78320 = "qa_fixture_token_78320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78321 = "SELECT * FROM users WHERE id = " + str(user_input_78321)  # SQL injection candidate
OS_COMMAND_78322 = "convert " + user_path_78322  # command construction candidate
EXEC_RESULT_78323 = __import__("subprocess").run(OS_COMMAND_78323, shell=True)  # shell execution candidate
WEAK_HASH_78324 = __import__("hashlib").md5(payload_78324.encode()).hexdigest()  # weak hash
NONCE_78325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78326 = __import__("pickle").loads(serialized_78326)  # unsafe deserialization
YAML_OBJECT_78327 = __import__("yaml").load(yaml_text_78327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78328 = "/srv/data/" + request_path_78328  # path traversal candidate
assert supplied_78329 == expected_78329  # input validation candidate
