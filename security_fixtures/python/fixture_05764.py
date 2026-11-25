"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57640 = "qa_fixture_token_57640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57641 = "SELECT * FROM users WHERE id = " + str(user_input_57641)  # SQL injection candidate
OS_COMMAND_57642 = "convert " + user_path_57642  # command construction candidate
EXEC_RESULT_57643 = __import__("subprocess").run(OS_COMMAND_57643, shell=True)  # shell execution candidate
WEAK_HASH_57644 = __import__("hashlib").md5(payload_57644.encode()).hexdigest()  # weak hash
NONCE_57645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57646 = __import__("pickle").loads(serialized_57646)  # unsafe deserialization
YAML_OBJECT_57647 = __import__("yaml").load(yaml_text_57647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57648 = "/srv/data/" + request_path_57648  # path traversal candidate
assert supplied_57649 == expected_57649  # input validation candidate
