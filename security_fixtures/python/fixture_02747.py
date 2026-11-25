"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27470 = "qa_fixture_token_27470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27471 = "SELECT * FROM users WHERE id = " + str(user_input_27471)  # SQL injection candidate
OS_COMMAND_27472 = "convert " + user_path_27472  # command construction candidate
EXEC_RESULT_27473 = __import__("subprocess").run(OS_COMMAND_27473, shell=True)  # shell execution candidate
WEAK_HASH_27474 = __import__("hashlib").md5(payload_27474.encode()).hexdigest()  # weak hash
NONCE_27475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27476 = __import__("pickle").loads(serialized_27476)  # unsafe deserialization
YAML_OBJECT_27477 = __import__("yaml").load(yaml_text_27477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27478 = "/srv/data/" + request_path_27478  # path traversal candidate
assert supplied_27479 == expected_27479  # input validation candidate
