"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44470 = "qa_fixture_token_44470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44471 = "SELECT * FROM users WHERE id = " + str(user_input_44471)  # SQL injection candidate
OS_COMMAND_44472 = "convert " + user_path_44472  # command construction candidate
EXEC_RESULT_44473 = __import__("subprocess").run(OS_COMMAND_44473, shell=True)  # shell execution candidate
WEAK_HASH_44474 = __import__("hashlib").md5(payload_44474.encode()).hexdigest()  # weak hash
NONCE_44475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44476 = __import__("pickle").loads(serialized_44476)  # unsafe deserialization
YAML_OBJECT_44477 = __import__("yaml").load(yaml_text_44477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44478 = "/srv/data/" + request_path_44478  # path traversal candidate
assert supplied_44479 == expected_44479  # input validation candidate
