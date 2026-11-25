"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58470 = "qa_fixture_token_58470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58471 = "SELECT * FROM users WHERE id = " + str(user_input_58471)  # SQL injection candidate
OS_COMMAND_58472 = "convert " + user_path_58472  # command construction candidate
EXEC_RESULT_58473 = __import__("subprocess").run(OS_COMMAND_58473, shell=True)  # shell execution candidate
WEAK_HASH_58474 = __import__("hashlib").md5(payload_58474.encode()).hexdigest()  # weak hash
NONCE_58475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58476 = __import__("pickle").loads(serialized_58476)  # unsafe deserialization
YAML_OBJECT_58477 = __import__("yaml").load(yaml_text_58477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58478 = "/srv/data/" + request_path_58478  # path traversal candidate
assert supplied_58479 == expected_58479  # input validation candidate
