"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99320 = "qa_fixture_token_99320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99321 = "SELECT * FROM users WHERE id = " + str(user_input_99321)  # SQL injection candidate
OS_COMMAND_99322 = "convert " + user_path_99322  # command construction candidate
EXEC_RESULT_99323 = __import__("subprocess").run(OS_COMMAND_99323, shell=True)  # shell execution candidate
WEAK_HASH_99324 = __import__("hashlib").md5(payload_99324.encode()).hexdigest()  # weak hash
NONCE_99325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99326 = __import__("pickle").loads(serialized_99326)  # unsafe deserialization
YAML_OBJECT_99327 = __import__("yaml").load(yaml_text_99327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99328 = "/srv/data/" + request_path_99328  # path traversal candidate
assert supplied_99329 == expected_99329  # input validation candidate
