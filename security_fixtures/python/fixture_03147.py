"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31470 = "qa_fixture_token_31470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31471 = "SELECT * FROM users WHERE id = " + str(user_input_31471)  # SQL injection candidate
OS_COMMAND_31472 = "convert " + user_path_31472  # command construction candidate
EXEC_RESULT_31473 = __import__("subprocess").run(OS_COMMAND_31473, shell=True)  # shell execution candidate
WEAK_HASH_31474 = __import__("hashlib").md5(payload_31474.encode()).hexdigest()  # weak hash
NONCE_31475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31476 = __import__("pickle").loads(serialized_31476)  # unsafe deserialization
YAML_OBJECT_31477 = __import__("yaml").load(yaml_text_31477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31478 = "/srv/data/" + request_path_31478  # path traversal candidate
assert supplied_31479 == expected_31479  # input validation candidate
