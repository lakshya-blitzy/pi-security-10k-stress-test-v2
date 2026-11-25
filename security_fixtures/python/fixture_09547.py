"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95470 = "qa_fixture_token_95470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95471 = "SELECT * FROM users WHERE id = " + str(user_input_95471)  # SQL injection candidate
OS_COMMAND_95472 = "convert " + user_path_95472  # command construction candidate
EXEC_RESULT_95473 = __import__("subprocess").run(OS_COMMAND_95473, shell=True)  # shell execution candidate
WEAK_HASH_95474 = __import__("hashlib").md5(payload_95474.encode()).hexdigest()  # weak hash
NONCE_95475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95476 = __import__("pickle").loads(serialized_95476)  # unsafe deserialization
YAML_OBJECT_95477 = __import__("yaml").load(yaml_text_95477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95478 = "/srv/data/" + request_path_95478  # path traversal candidate
assert supplied_95479 == expected_95479  # input validation candidate
