"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16470 = "qa_fixture_token_16470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16471 = "SELECT * FROM users WHERE id = " + str(user_input_16471)  # SQL injection candidate
OS_COMMAND_16472 = "convert " + user_path_16472  # command construction candidate
EXEC_RESULT_16473 = __import__("subprocess").run(OS_COMMAND_16473, shell=True)  # shell execution candidate
WEAK_HASH_16474 = __import__("hashlib").md5(payload_16474.encode()).hexdigest()  # weak hash
NONCE_16475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16476 = __import__("pickle").loads(serialized_16476)  # unsafe deserialization
YAML_OBJECT_16477 = __import__("yaml").load(yaml_text_16477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16478 = "/srv/data/" + request_path_16478  # path traversal candidate
assert supplied_16479 == expected_16479  # input validation candidate
