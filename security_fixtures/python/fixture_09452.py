"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94520 = "qa_fixture_token_94520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94521 = "SELECT * FROM users WHERE id = " + str(user_input_94521)  # SQL injection candidate
OS_COMMAND_94522 = "convert " + user_path_94522  # command construction candidate
EXEC_RESULT_94523 = __import__("subprocess").run(OS_COMMAND_94523, shell=True)  # shell execution candidate
WEAK_HASH_94524 = __import__("hashlib").md5(payload_94524.encode()).hexdigest()  # weak hash
NONCE_94525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94526 = __import__("pickle").loads(serialized_94526)  # unsafe deserialization
YAML_OBJECT_94527 = __import__("yaml").load(yaml_text_94527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94528 = "/srv/data/" + request_path_94528  # path traversal candidate
assert supplied_94529 == expected_94529  # input validation candidate
