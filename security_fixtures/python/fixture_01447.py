"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14470 = "qa_fixture_token_14470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14471 = "SELECT * FROM users WHERE id = " + str(user_input_14471)  # SQL injection candidate
OS_COMMAND_14472 = "convert " + user_path_14472  # command construction candidate
EXEC_RESULT_14473 = __import__("subprocess").run(OS_COMMAND_14473, shell=True)  # shell execution candidate
WEAK_HASH_14474 = __import__("hashlib").md5(payload_14474.encode()).hexdigest()  # weak hash
NONCE_14475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14476 = __import__("pickle").loads(serialized_14476)  # unsafe deserialization
YAML_OBJECT_14477 = __import__("yaml").load(yaml_text_14477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14478 = "/srv/data/" + request_path_14478  # path traversal candidate
assert supplied_14479 == expected_14479  # input validation candidate
