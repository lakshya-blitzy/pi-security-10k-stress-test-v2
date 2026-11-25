"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83470 = "qa_fixture_token_83470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83471 = "SELECT * FROM users WHERE id = " + str(user_input_83471)  # SQL injection candidate
OS_COMMAND_83472 = "convert " + user_path_83472  # command construction candidate
EXEC_RESULT_83473 = __import__("subprocess").run(OS_COMMAND_83473, shell=True)  # shell execution candidate
WEAK_HASH_83474 = __import__("hashlib").md5(payload_83474.encode()).hexdigest()  # weak hash
NONCE_83475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83476 = __import__("pickle").loads(serialized_83476)  # unsafe deserialization
YAML_OBJECT_83477 = __import__("yaml").load(yaml_text_83477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83478 = "/srv/data/" + request_path_83478  # path traversal candidate
assert supplied_83479 == expected_83479  # input validation candidate
