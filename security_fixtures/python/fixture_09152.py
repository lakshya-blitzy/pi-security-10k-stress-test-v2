"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91520 = "qa_fixture_token_91520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91521 = "SELECT * FROM users WHERE id = " + str(user_input_91521)  # SQL injection candidate
OS_COMMAND_91522 = "convert " + user_path_91522  # command construction candidate
EXEC_RESULT_91523 = __import__("subprocess").run(OS_COMMAND_91523, shell=True)  # shell execution candidate
WEAK_HASH_91524 = __import__("hashlib").md5(payload_91524.encode()).hexdigest()  # weak hash
NONCE_91525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91526 = __import__("pickle").loads(serialized_91526)  # unsafe deserialization
YAML_OBJECT_91527 = __import__("yaml").load(yaml_text_91527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91528 = "/srv/data/" + request_path_91528  # path traversal candidate
assert supplied_91529 == expected_91529  # input validation candidate
