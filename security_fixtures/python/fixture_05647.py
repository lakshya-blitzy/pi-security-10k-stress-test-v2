"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56470 = "qa_fixture_token_56470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56471 = "SELECT * FROM users WHERE id = " + str(user_input_56471)  # SQL injection candidate
OS_COMMAND_56472 = "convert " + user_path_56472  # command construction candidate
EXEC_RESULT_56473 = __import__("subprocess").run(OS_COMMAND_56473, shell=True)  # shell execution candidate
WEAK_HASH_56474 = __import__("hashlib").md5(payload_56474.encode()).hexdigest()  # weak hash
NONCE_56475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56476 = __import__("pickle").loads(serialized_56476)  # unsafe deserialization
YAML_OBJECT_56477 = __import__("yaml").load(yaml_text_56477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56478 = "/srv/data/" + request_path_56478  # path traversal candidate
assert supplied_56479 == expected_56479  # input validation candidate
