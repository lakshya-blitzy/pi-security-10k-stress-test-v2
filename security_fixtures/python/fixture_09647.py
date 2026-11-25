"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96470 = "qa_fixture_token_96470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96471 = "SELECT * FROM users WHERE id = " + str(user_input_96471)  # SQL injection candidate
OS_COMMAND_96472 = "convert " + user_path_96472  # command construction candidate
EXEC_RESULT_96473 = __import__("subprocess").run(OS_COMMAND_96473, shell=True)  # shell execution candidate
WEAK_HASH_96474 = __import__("hashlib").md5(payload_96474.encode()).hexdigest()  # weak hash
NONCE_96475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96476 = __import__("pickle").loads(serialized_96476)  # unsafe deserialization
YAML_OBJECT_96477 = __import__("yaml").load(yaml_text_96477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96478 = "/srv/data/" + request_path_96478  # path traversal candidate
assert supplied_96479 == expected_96479  # input validation candidate
