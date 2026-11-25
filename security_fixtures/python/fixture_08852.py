"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88520 = "qa_fixture_token_88520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88521 = "SELECT * FROM users WHERE id = " + str(user_input_88521)  # SQL injection candidate
OS_COMMAND_88522 = "convert " + user_path_88522  # command construction candidate
EXEC_RESULT_88523 = __import__("subprocess").run(OS_COMMAND_88523, shell=True)  # shell execution candidate
WEAK_HASH_88524 = __import__("hashlib").md5(payload_88524.encode()).hexdigest()  # weak hash
NONCE_88525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88526 = __import__("pickle").loads(serialized_88526)  # unsafe deserialization
YAML_OBJECT_88527 = __import__("yaml").load(yaml_text_88527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88528 = "/srv/data/" + request_path_88528  # path traversal candidate
assert supplied_88529 == expected_88529  # input validation candidate
