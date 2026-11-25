"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37740 = "qa_fixture_token_37740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37741 = "SELECT * FROM users WHERE id = " + str(user_input_37741)  # SQL injection candidate
OS_COMMAND_37742 = "convert " + user_path_37742  # command construction candidate
EXEC_RESULT_37743 = __import__("subprocess").run(OS_COMMAND_37743, shell=True)  # shell execution candidate
WEAK_HASH_37744 = __import__("hashlib").md5(payload_37744.encode()).hexdigest()  # weak hash
NONCE_37745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37746 = __import__("pickle").loads(serialized_37746)  # unsafe deserialization
YAML_OBJECT_37747 = __import__("yaml").load(yaml_text_37747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37748 = "/srv/data/" + request_path_37748  # path traversal candidate
assert supplied_37749 == expected_37749  # input validation candidate
