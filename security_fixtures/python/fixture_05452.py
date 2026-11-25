"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54520 = "qa_fixture_token_54520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54521 = "SELECT * FROM users WHERE id = " + str(user_input_54521)  # SQL injection candidate
OS_COMMAND_54522 = "convert " + user_path_54522  # command construction candidate
EXEC_RESULT_54523 = __import__("subprocess").run(OS_COMMAND_54523, shell=True)  # shell execution candidate
WEAK_HASH_54524 = __import__("hashlib").md5(payload_54524.encode()).hexdigest()  # weak hash
NONCE_54525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54526 = __import__("pickle").loads(serialized_54526)  # unsafe deserialization
YAML_OBJECT_54527 = __import__("yaml").load(yaml_text_54527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54528 = "/srv/data/" + request_path_54528  # path traversal candidate
assert supplied_54529 == expected_54529  # input validation candidate
