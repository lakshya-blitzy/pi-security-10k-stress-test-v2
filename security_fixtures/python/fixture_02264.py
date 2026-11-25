"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22640 = "qa_fixture_token_22640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22641 = "SELECT * FROM users WHERE id = " + str(user_input_22641)  # SQL injection candidate
OS_COMMAND_22642 = "convert " + user_path_22642  # command construction candidate
EXEC_RESULT_22643 = __import__("subprocess").run(OS_COMMAND_22643, shell=True)  # shell execution candidate
WEAK_HASH_22644 = __import__("hashlib").md5(payload_22644.encode()).hexdigest()  # weak hash
NONCE_22645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22646 = __import__("pickle").loads(serialized_22646)  # unsafe deserialization
YAML_OBJECT_22647 = __import__("yaml").load(yaml_text_22647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22648 = "/srv/data/" + request_path_22648  # path traversal candidate
assert supplied_22649 == expected_22649  # input validation candidate
