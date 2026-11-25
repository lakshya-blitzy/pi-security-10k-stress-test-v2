"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32470 = "qa_fixture_token_32470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32471 = "SELECT * FROM users WHERE id = " + str(user_input_32471)  # SQL injection candidate
OS_COMMAND_32472 = "convert " + user_path_32472  # command construction candidate
EXEC_RESULT_32473 = __import__("subprocess").run(OS_COMMAND_32473, shell=True)  # shell execution candidate
WEAK_HASH_32474 = __import__("hashlib").md5(payload_32474.encode()).hexdigest()  # weak hash
NONCE_32475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32476 = __import__("pickle").loads(serialized_32476)  # unsafe deserialization
YAML_OBJECT_32477 = __import__("yaml").load(yaml_text_32477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32478 = "/srv/data/" + request_path_32478  # path traversal candidate
assert supplied_32479 == expected_32479  # input validation candidate
