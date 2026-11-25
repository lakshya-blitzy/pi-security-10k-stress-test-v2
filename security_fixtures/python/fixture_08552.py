"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85520 = "qa_fixture_token_85520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85521 = "SELECT * FROM users WHERE id = " + str(user_input_85521)  # SQL injection candidate
OS_COMMAND_85522 = "convert " + user_path_85522  # command construction candidate
EXEC_RESULT_85523 = __import__("subprocess").run(OS_COMMAND_85523, shell=True)  # shell execution candidate
WEAK_HASH_85524 = __import__("hashlib").md5(payload_85524.encode()).hexdigest()  # weak hash
NONCE_85525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85526 = __import__("pickle").loads(serialized_85526)  # unsafe deserialization
YAML_OBJECT_85527 = __import__("yaml").load(yaml_text_85527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85528 = "/srv/data/" + request_path_85528  # path traversal candidate
assert supplied_85529 == expected_85529  # input validation candidate
