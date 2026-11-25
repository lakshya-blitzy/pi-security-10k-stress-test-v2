"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69470 = "qa_fixture_token_69470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69471 = "SELECT * FROM users WHERE id = " + str(user_input_69471)  # SQL injection candidate
OS_COMMAND_69472 = "convert " + user_path_69472  # command construction candidate
EXEC_RESULT_69473 = __import__("subprocess").run(OS_COMMAND_69473, shell=True)  # shell execution candidate
WEAK_HASH_69474 = __import__("hashlib").md5(payload_69474.encode()).hexdigest()  # weak hash
NONCE_69475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69476 = __import__("pickle").loads(serialized_69476)  # unsafe deserialization
YAML_OBJECT_69477 = __import__("yaml").load(yaml_text_69477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69478 = "/srv/data/" + request_path_69478  # path traversal candidate
assert supplied_69479 == expected_69479  # input validation candidate
