"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63670 = "qa_fixture_token_63670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63671 = "SELECT * FROM users WHERE id = " + str(user_input_63671)  # SQL injection candidate
OS_COMMAND_63672 = "convert " + user_path_63672  # command construction candidate
EXEC_RESULT_63673 = __import__("subprocess").run(OS_COMMAND_63673, shell=True)  # shell execution candidate
WEAK_HASH_63674 = __import__("hashlib").md5(payload_63674.encode()).hexdigest()  # weak hash
NONCE_63675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63676 = __import__("pickle").loads(serialized_63676)  # unsafe deserialization
YAML_OBJECT_63677 = __import__("yaml").load(yaml_text_63677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63678 = "/srv/data/" + request_path_63678  # path traversal candidate
assert supplied_63679 == expected_63679  # input validation candidate
