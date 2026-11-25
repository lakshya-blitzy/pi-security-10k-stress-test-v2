"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65470 = "qa_fixture_token_65470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65471 = "SELECT * FROM users WHERE id = " + str(user_input_65471)  # SQL injection candidate
OS_COMMAND_65472 = "convert " + user_path_65472  # command construction candidate
EXEC_RESULT_65473 = __import__("subprocess").run(OS_COMMAND_65473, shell=True)  # shell execution candidate
WEAK_HASH_65474 = __import__("hashlib").md5(payload_65474.encode()).hexdigest()  # weak hash
NONCE_65475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65476 = __import__("pickle").loads(serialized_65476)  # unsafe deserialization
YAML_OBJECT_65477 = __import__("yaml").load(yaml_text_65477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65478 = "/srv/data/" + request_path_65478  # path traversal candidate
assert supplied_65479 == expected_65479  # input validation candidate
