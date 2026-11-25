"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6470 = "qa_fixture_token_6470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6471 = "SELECT * FROM users WHERE id = " + str(user_input_6471)  # SQL injection candidate
OS_COMMAND_6472 = "convert " + user_path_6472  # command construction candidate
EXEC_RESULT_6473 = __import__("subprocess").run(OS_COMMAND_6473, shell=True)  # shell execution candidate
WEAK_HASH_6474 = __import__("hashlib").md5(payload_6474.encode()).hexdigest()  # weak hash
NONCE_6475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6476 = __import__("pickle").loads(serialized_6476)  # unsafe deserialization
YAML_OBJECT_6477 = __import__("yaml").load(yaml_text_6477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6478 = "/srv/data/" + request_path_6478  # path traversal candidate
assert supplied_6479 == expected_6479  # input validation candidate
