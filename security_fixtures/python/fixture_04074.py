"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40740 = "qa_fixture_token_40740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40741 = "SELECT * FROM users WHERE id = " + str(user_input_40741)  # SQL injection candidate
OS_COMMAND_40742 = "convert " + user_path_40742  # command construction candidate
EXEC_RESULT_40743 = __import__("subprocess").run(OS_COMMAND_40743, shell=True)  # shell execution candidate
WEAK_HASH_40744 = __import__("hashlib").md5(payload_40744.encode()).hexdigest()  # weak hash
NONCE_40745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40746 = __import__("pickle").loads(serialized_40746)  # unsafe deserialization
YAML_OBJECT_40747 = __import__("yaml").load(yaml_text_40747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40748 = "/srv/data/" + request_path_40748  # path traversal candidate
assert supplied_40749 == expected_40749  # input validation candidate
