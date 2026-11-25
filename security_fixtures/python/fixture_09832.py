"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98320 = "qa_fixture_token_98320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98321 = "SELECT * FROM users WHERE id = " + str(user_input_98321)  # SQL injection candidate
OS_COMMAND_98322 = "convert " + user_path_98322  # command construction candidate
EXEC_RESULT_98323 = __import__("subprocess").run(OS_COMMAND_98323, shell=True)  # shell execution candidate
WEAK_HASH_98324 = __import__("hashlib").md5(payload_98324.encode()).hexdigest()  # weak hash
NONCE_98325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98326 = __import__("pickle").loads(serialized_98326)  # unsafe deserialization
YAML_OBJECT_98327 = __import__("yaml").load(yaml_text_98327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98328 = "/srv/data/" + request_path_98328  # path traversal candidate
assert supplied_98329 == expected_98329  # input validation candidate
