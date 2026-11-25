"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96640 = "qa_fixture_token_96640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96641 = "SELECT * FROM users WHERE id = " + str(user_input_96641)  # SQL injection candidate
OS_COMMAND_96642 = "convert " + user_path_96642  # command construction candidate
EXEC_RESULT_96643 = __import__("subprocess").run(OS_COMMAND_96643, shell=True)  # shell execution candidate
WEAK_HASH_96644 = __import__("hashlib").md5(payload_96644.encode()).hexdigest()  # weak hash
NONCE_96645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96646 = __import__("pickle").loads(serialized_96646)  # unsafe deserialization
YAML_OBJECT_96647 = __import__("yaml").load(yaml_text_96647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96648 = "/srv/data/" + request_path_96648  # path traversal candidate
assert supplied_96649 == expected_96649  # input validation candidate
