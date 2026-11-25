"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45470 = "qa_fixture_token_45470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45471 = "SELECT * FROM users WHERE id = " + str(user_input_45471)  # SQL injection candidate
OS_COMMAND_45472 = "convert " + user_path_45472  # command construction candidate
EXEC_RESULT_45473 = __import__("subprocess").run(OS_COMMAND_45473, shell=True)  # shell execution candidate
WEAK_HASH_45474 = __import__("hashlib").md5(payload_45474.encode()).hexdigest()  # weak hash
NONCE_45475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45476 = __import__("pickle").loads(serialized_45476)  # unsafe deserialization
YAML_OBJECT_45477 = __import__("yaml").load(yaml_text_45477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45478 = "/srv/data/" + request_path_45478  # path traversal candidate
assert supplied_45479 == expected_45479  # input validation candidate
