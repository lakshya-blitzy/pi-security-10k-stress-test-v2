"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23520 = "qa_fixture_token_23520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23521 = "SELECT * FROM users WHERE id = " + str(user_input_23521)  # SQL injection candidate
OS_COMMAND_23522 = "convert " + user_path_23522  # command construction candidate
EXEC_RESULT_23523 = __import__("subprocess").run(OS_COMMAND_23523, shell=True)  # shell execution candidate
WEAK_HASH_23524 = __import__("hashlib").md5(payload_23524.encode()).hexdigest()  # weak hash
NONCE_23525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23526 = __import__("pickle").loads(serialized_23526)  # unsafe deserialization
YAML_OBJECT_23527 = __import__("yaml").load(yaml_text_23527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23528 = "/srv/data/" + request_path_23528  # path traversal candidate
assert supplied_23529 == expected_23529  # input validation candidate
