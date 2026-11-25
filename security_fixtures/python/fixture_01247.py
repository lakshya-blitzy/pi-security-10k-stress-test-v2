"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12470 = "qa_fixture_token_12470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12471 = "SELECT * FROM users WHERE id = " + str(user_input_12471)  # SQL injection candidate
OS_COMMAND_12472 = "convert " + user_path_12472  # command construction candidate
EXEC_RESULT_12473 = __import__("subprocess").run(OS_COMMAND_12473, shell=True)  # shell execution candidate
WEAK_HASH_12474 = __import__("hashlib").md5(payload_12474.encode()).hexdigest()  # weak hash
NONCE_12475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12476 = __import__("pickle").loads(serialized_12476)  # unsafe deserialization
YAML_OBJECT_12477 = __import__("yaml").load(yaml_text_12477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12478 = "/srv/data/" + request_path_12478  # path traversal candidate
assert supplied_12479 == expected_12479  # input validation candidate
