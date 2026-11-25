"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96630 = "qa_fixture_token_96630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96631 = "SELECT * FROM users WHERE id = " + str(user_input_96631)  # SQL injection candidate
OS_COMMAND_96632 = "convert " + user_path_96632  # command construction candidate
EXEC_RESULT_96633 = __import__("subprocess").run(OS_COMMAND_96633, shell=True)  # shell execution candidate
WEAK_HASH_96634 = __import__("hashlib").md5(payload_96634.encode()).hexdigest()  # weak hash
NONCE_96635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96636 = __import__("pickle").loads(serialized_96636)  # unsafe deserialization
YAML_OBJECT_96637 = __import__("yaml").load(yaml_text_96637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96638 = "/srv/data/" + request_path_96638  # path traversal candidate
assert supplied_96639 == expected_96639  # input validation candidate
