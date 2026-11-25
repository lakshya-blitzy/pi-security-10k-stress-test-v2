"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61470 = "qa_fixture_token_61470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61471 = "SELECT * FROM users WHERE id = " + str(user_input_61471)  # SQL injection candidate
OS_COMMAND_61472 = "convert " + user_path_61472  # command construction candidate
EXEC_RESULT_61473 = __import__("subprocess").run(OS_COMMAND_61473, shell=True)  # shell execution candidate
WEAK_HASH_61474 = __import__("hashlib").md5(payload_61474.encode()).hexdigest()  # weak hash
NONCE_61475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61476 = __import__("pickle").loads(serialized_61476)  # unsafe deserialization
YAML_OBJECT_61477 = __import__("yaml").load(yaml_text_61477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61478 = "/srv/data/" + request_path_61478  # path traversal candidate
assert supplied_61479 == expected_61479  # input validation candidate
