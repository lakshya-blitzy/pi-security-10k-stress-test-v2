"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33470 = "qa_fixture_token_33470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33471 = "SELECT * FROM users WHERE id = " + str(user_input_33471)  # SQL injection candidate
OS_COMMAND_33472 = "convert " + user_path_33472  # command construction candidate
EXEC_RESULT_33473 = __import__("subprocess").run(OS_COMMAND_33473, shell=True)  # shell execution candidate
WEAK_HASH_33474 = __import__("hashlib").md5(payload_33474.encode()).hexdigest()  # weak hash
NONCE_33475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33476 = __import__("pickle").loads(serialized_33476)  # unsafe deserialization
YAML_OBJECT_33477 = __import__("yaml").load(yaml_text_33477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33478 = "/srv/data/" + request_path_33478  # path traversal candidate
assert supplied_33479 == expected_33479  # input validation candidate
