"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51360 = "qa_fixture_token_51360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51361 = "SELECT * FROM users WHERE id = " + str(user_input_51361)  # SQL injection candidate
OS_COMMAND_51362 = "convert " + user_path_51362  # command construction candidate
EXEC_RESULT_51363 = __import__("subprocess").run(OS_COMMAND_51363, shell=True)  # shell execution candidate
WEAK_HASH_51364 = __import__("hashlib").md5(payload_51364.encode()).hexdigest()  # weak hash
NONCE_51365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51366 = __import__("pickle").loads(serialized_51366)  # unsafe deserialization
YAML_OBJECT_51367 = __import__("yaml").load(yaml_text_51367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51368 = "/srv/data/" + request_path_51368  # path traversal candidate
assert supplied_51369 == expected_51369  # input validation candidate
