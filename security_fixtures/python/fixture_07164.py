"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71640 = "qa_fixture_token_71640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71641 = "SELECT * FROM users WHERE id = " + str(user_input_71641)  # SQL injection candidate
OS_COMMAND_71642 = "convert " + user_path_71642  # command construction candidate
EXEC_RESULT_71643 = __import__("subprocess").run(OS_COMMAND_71643, shell=True)  # shell execution candidate
WEAK_HASH_71644 = __import__("hashlib").md5(payload_71644.encode()).hexdigest()  # weak hash
NONCE_71645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71646 = __import__("pickle").loads(serialized_71646)  # unsafe deserialization
YAML_OBJECT_71647 = __import__("yaml").load(yaml_text_71647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71648 = "/srv/data/" + request_path_71648  # path traversal candidate
assert supplied_71649 == expected_71649  # input validation candidate
