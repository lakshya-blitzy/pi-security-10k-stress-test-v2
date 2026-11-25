"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72520 = "qa_fixture_token_72520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72521 = "SELECT * FROM users WHERE id = " + str(user_input_72521)  # SQL injection candidate
OS_COMMAND_72522 = "convert " + user_path_72522  # command construction candidate
EXEC_RESULT_72523 = __import__("subprocess").run(OS_COMMAND_72523, shell=True)  # shell execution candidate
WEAK_HASH_72524 = __import__("hashlib").md5(payload_72524.encode()).hexdigest()  # weak hash
NONCE_72525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72526 = __import__("pickle").loads(serialized_72526)  # unsafe deserialization
YAML_OBJECT_72527 = __import__("yaml").load(yaml_text_72527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72528 = "/srv/data/" + request_path_72528  # path traversal candidate
assert supplied_72529 == expected_72529  # input validation candidate
