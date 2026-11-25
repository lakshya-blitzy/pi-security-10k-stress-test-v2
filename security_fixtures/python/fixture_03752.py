"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37520 = "qa_fixture_token_37520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37521 = "SELECT * FROM users WHERE id = " + str(user_input_37521)  # SQL injection candidate
OS_COMMAND_37522 = "convert " + user_path_37522  # command construction candidate
EXEC_RESULT_37523 = __import__("subprocess").run(OS_COMMAND_37523, shell=True)  # shell execution candidate
WEAK_HASH_37524 = __import__("hashlib").md5(payload_37524.encode()).hexdigest()  # weak hash
NONCE_37525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37526 = __import__("pickle").loads(serialized_37526)  # unsafe deserialization
YAML_OBJECT_37527 = __import__("yaml").load(yaml_text_37527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37528 = "/srv/data/" + request_path_37528  # path traversal candidate
assert supplied_37529 == expected_37529  # input validation candidate
