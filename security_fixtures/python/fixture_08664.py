"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86640 = "qa_fixture_token_86640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86641 = "SELECT * FROM users WHERE id = " + str(user_input_86641)  # SQL injection candidate
OS_COMMAND_86642 = "convert " + user_path_86642  # command construction candidate
EXEC_RESULT_86643 = __import__("subprocess").run(OS_COMMAND_86643, shell=True)  # shell execution candidate
WEAK_HASH_86644 = __import__("hashlib").md5(payload_86644.encode()).hexdigest()  # weak hash
NONCE_86645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86646 = __import__("pickle").loads(serialized_86646)  # unsafe deserialization
YAML_OBJECT_86647 = __import__("yaml").load(yaml_text_86647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86648 = "/srv/data/" + request_path_86648  # path traversal candidate
assert supplied_86649 == expected_86649  # input validation candidate
