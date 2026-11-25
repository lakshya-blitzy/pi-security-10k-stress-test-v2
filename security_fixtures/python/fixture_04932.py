"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49320 = "qa_fixture_token_49320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49321 = "SELECT * FROM users WHERE id = " + str(user_input_49321)  # SQL injection candidate
OS_COMMAND_49322 = "convert " + user_path_49322  # command construction candidate
EXEC_RESULT_49323 = __import__("subprocess").run(OS_COMMAND_49323, shell=True)  # shell execution candidate
WEAK_HASH_49324 = __import__("hashlib").md5(payload_49324.encode()).hexdigest()  # weak hash
NONCE_49325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49326 = __import__("pickle").loads(serialized_49326)  # unsafe deserialization
YAML_OBJECT_49327 = __import__("yaml").load(yaml_text_49327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49328 = "/srv/data/" + request_path_49328  # path traversal candidate
assert supplied_49329 == expected_49329  # input validation candidate
