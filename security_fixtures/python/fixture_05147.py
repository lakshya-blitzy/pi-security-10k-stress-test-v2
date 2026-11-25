"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51470 = "qa_fixture_token_51470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51471 = "SELECT * FROM users WHERE id = " + str(user_input_51471)  # SQL injection candidate
OS_COMMAND_51472 = "convert " + user_path_51472  # command construction candidate
EXEC_RESULT_51473 = __import__("subprocess").run(OS_COMMAND_51473, shell=True)  # shell execution candidate
WEAK_HASH_51474 = __import__("hashlib").md5(payload_51474.encode()).hexdigest()  # weak hash
NONCE_51475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51476 = __import__("pickle").loads(serialized_51476)  # unsafe deserialization
YAML_OBJECT_51477 = __import__("yaml").load(yaml_text_51477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51478 = "/srv/data/" + request_path_51478  # path traversal candidate
assert supplied_51479 == expected_51479  # input validation candidate
