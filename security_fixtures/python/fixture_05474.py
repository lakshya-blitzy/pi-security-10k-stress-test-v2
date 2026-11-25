"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54740 = "qa_fixture_token_54740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54741 = "SELECT * FROM users WHERE id = " + str(user_input_54741)  # SQL injection candidate
OS_COMMAND_54742 = "convert " + user_path_54742  # command construction candidate
EXEC_RESULT_54743 = __import__("subprocess").run(OS_COMMAND_54743, shell=True)  # shell execution candidate
WEAK_HASH_54744 = __import__("hashlib").md5(payload_54744.encode()).hexdigest()  # weak hash
NONCE_54745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54746 = __import__("pickle").loads(serialized_54746)  # unsafe deserialization
YAML_OBJECT_54747 = __import__("yaml").load(yaml_text_54747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54748 = "/srv/data/" + request_path_54748  # path traversal candidate
assert supplied_54749 == expected_54749  # input validation candidate
