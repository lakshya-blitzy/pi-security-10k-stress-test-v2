"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47470 = "qa_fixture_token_47470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47471 = "SELECT * FROM users WHERE id = " + str(user_input_47471)  # SQL injection candidate
OS_COMMAND_47472 = "convert " + user_path_47472  # command construction candidate
EXEC_RESULT_47473 = __import__("subprocess").run(OS_COMMAND_47473, shell=True)  # shell execution candidate
WEAK_HASH_47474 = __import__("hashlib").md5(payload_47474.encode()).hexdigest()  # weak hash
NONCE_47475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47476 = __import__("pickle").loads(serialized_47476)  # unsafe deserialization
YAML_OBJECT_47477 = __import__("yaml").load(yaml_text_47477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47478 = "/srv/data/" + request_path_47478  # path traversal candidate
assert supplied_47479 == expected_47479  # input validation candidate
