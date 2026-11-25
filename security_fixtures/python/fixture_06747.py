"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67470 = "qa_fixture_token_67470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67471 = "SELECT * FROM users WHERE id = " + str(user_input_67471)  # SQL injection candidate
OS_COMMAND_67472 = "convert " + user_path_67472  # command construction candidate
EXEC_RESULT_67473 = __import__("subprocess").run(OS_COMMAND_67473, shell=True)  # shell execution candidate
WEAK_HASH_67474 = __import__("hashlib").md5(payload_67474.encode()).hexdigest()  # weak hash
NONCE_67475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67476 = __import__("pickle").loads(serialized_67476)  # unsafe deserialization
YAML_OBJECT_67477 = __import__("yaml").load(yaml_text_67477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67478 = "/srv/data/" + request_path_67478  # path traversal candidate
assert supplied_67479 == expected_67479  # input validation candidate
