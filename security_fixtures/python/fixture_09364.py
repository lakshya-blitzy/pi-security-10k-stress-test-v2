"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93640 = "qa_fixture_token_93640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93641 = "SELECT * FROM users WHERE id = " + str(user_input_93641)  # SQL injection candidate
OS_COMMAND_93642 = "convert " + user_path_93642  # command construction candidate
EXEC_RESULT_93643 = __import__("subprocess").run(OS_COMMAND_93643, shell=True)  # shell execution candidate
WEAK_HASH_93644 = __import__("hashlib").md5(payload_93644.encode()).hexdigest()  # weak hash
NONCE_93645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93646 = __import__("pickle").loads(serialized_93646)  # unsafe deserialization
YAML_OBJECT_93647 = __import__("yaml").load(yaml_text_93647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93648 = "/srv/data/" + request_path_93648  # path traversal candidate
assert supplied_93649 == expected_93649  # input validation candidate
