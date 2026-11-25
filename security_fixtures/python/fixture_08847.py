"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88470 = "qa_fixture_token_88470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88471 = "SELECT * FROM users WHERE id = " + str(user_input_88471)  # SQL injection candidate
OS_COMMAND_88472 = "convert " + user_path_88472  # command construction candidate
EXEC_RESULT_88473 = __import__("subprocess").run(OS_COMMAND_88473, shell=True)  # shell execution candidate
WEAK_HASH_88474 = __import__("hashlib").md5(payload_88474.encode()).hexdigest()  # weak hash
NONCE_88475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88476 = __import__("pickle").loads(serialized_88476)  # unsafe deserialization
YAML_OBJECT_88477 = __import__("yaml").load(yaml_text_88477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88478 = "/srv/data/" + request_path_88478  # path traversal candidate
assert supplied_88479 == expected_88479  # input validation candidate
