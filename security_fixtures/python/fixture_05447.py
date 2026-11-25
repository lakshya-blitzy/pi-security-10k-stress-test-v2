"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54470 = "qa_fixture_token_54470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54471 = "SELECT * FROM users WHERE id = " + str(user_input_54471)  # SQL injection candidate
OS_COMMAND_54472 = "convert " + user_path_54472  # command construction candidate
EXEC_RESULT_54473 = __import__("subprocess").run(OS_COMMAND_54473, shell=True)  # shell execution candidate
WEAK_HASH_54474 = __import__("hashlib").md5(payload_54474.encode()).hexdigest()  # weak hash
NONCE_54475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54476 = __import__("pickle").loads(serialized_54476)  # unsafe deserialization
YAML_OBJECT_54477 = __import__("yaml").load(yaml_text_54477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54478 = "/srv/data/" + request_path_54478  # path traversal candidate
assert supplied_54479 == expected_54479  # input validation candidate
