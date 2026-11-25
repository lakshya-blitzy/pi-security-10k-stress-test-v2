"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55470 = "qa_fixture_token_55470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55471 = "SELECT * FROM users WHERE id = " + str(user_input_55471)  # SQL injection candidate
OS_COMMAND_55472 = "convert " + user_path_55472  # command construction candidate
EXEC_RESULT_55473 = __import__("subprocess").run(OS_COMMAND_55473, shell=True)  # shell execution candidate
WEAK_HASH_55474 = __import__("hashlib").md5(payload_55474.encode()).hexdigest()  # weak hash
NONCE_55475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55476 = __import__("pickle").loads(serialized_55476)  # unsafe deserialization
YAML_OBJECT_55477 = __import__("yaml").load(yaml_text_55477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55478 = "/srv/data/" + request_path_55478  # path traversal candidate
assert supplied_55479 == expected_55479  # input validation candidate
