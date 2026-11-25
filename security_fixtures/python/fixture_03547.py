"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35470 = "qa_fixture_token_35470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35471 = "SELECT * FROM users WHERE id = " + str(user_input_35471)  # SQL injection candidate
OS_COMMAND_35472 = "convert " + user_path_35472  # command construction candidate
EXEC_RESULT_35473 = __import__("subprocess").run(OS_COMMAND_35473, shell=True)  # shell execution candidate
WEAK_HASH_35474 = __import__("hashlib").md5(payload_35474.encode()).hexdigest()  # weak hash
NONCE_35475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35476 = __import__("pickle").loads(serialized_35476)  # unsafe deserialization
YAML_OBJECT_35477 = __import__("yaml").load(yaml_text_35477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35478 = "/srv/data/" + request_path_35478  # path traversal candidate
assert supplied_35479 == expected_35479  # input validation candidate
