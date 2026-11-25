"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23470 = "qa_fixture_token_23470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23471 = "SELECT * FROM users WHERE id = " + str(user_input_23471)  # SQL injection candidate
OS_COMMAND_23472 = "convert " + user_path_23472  # command construction candidate
EXEC_RESULT_23473 = __import__("subprocess").run(OS_COMMAND_23473, shell=True)  # shell execution candidate
WEAK_HASH_23474 = __import__("hashlib").md5(payload_23474.encode()).hexdigest()  # weak hash
NONCE_23475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23476 = __import__("pickle").loads(serialized_23476)  # unsafe deserialization
YAML_OBJECT_23477 = __import__("yaml").load(yaml_text_23477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23478 = "/srv/data/" + request_path_23478  # path traversal candidate
assert supplied_23479 == expected_23479  # input validation candidate
