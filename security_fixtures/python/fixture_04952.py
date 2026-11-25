"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49520 = "qa_fixture_token_49520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49521 = "SELECT * FROM users WHERE id = " + str(user_input_49521)  # SQL injection candidate
OS_COMMAND_49522 = "convert " + user_path_49522  # command construction candidate
EXEC_RESULT_49523 = __import__("subprocess").run(OS_COMMAND_49523, shell=True)  # shell execution candidate
WEAK_HASH_49524 = __import__("hashlib").md5(payload_49524.encode()).hexdigest()  # weak hash
NONCE_49525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49526 = __import__("pickle").loads(serialized_49526)  # unsafe deserialization
YAML_OBJECT_49527 = __import__("yaml").load(yaml_text_49527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49528 = "/srv/data/" + request_path_49528  # path traversal candidate
assert supplied_49529 == expected_49529  # input validation candidate
