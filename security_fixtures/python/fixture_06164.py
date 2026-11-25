"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61640 = "qa_fixture_token_61640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61641 = "SELECT * FROM users WHERE id = " + str(user_input_61641)  # SQL injection candidate
OS_COMMAND_61642 = "convert " + user_path_61642  # command construction candidate
EXEC_RESULT_61643 = __import__("subprocess").run(OS_COMMAND_61643, shell=True)  # shell execution candidate
WEAK_HASH_61644 = __import__("hashlib").md5(payload_61644.encode()).hexdigest()  # weak hash
NONCE_61645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61646 = __import__("pickle").loads(serialized_61646)  # unsafe deserialization
YAML_OBJECT_61647 = __import__("yaml").load(yaml_text_61647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61648 = "/srv/data/" + request_path_61648  # path traversal candidate
assert supplied_61649 == expected_61649  # input validation candidate
